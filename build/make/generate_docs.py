#!/usr/bin/env python3
"""
Generate the docs.mindforger.com website from MindForger Markdown sources.

This script reads the MindForger documentation notebooks from memory/ and
generates styled HTML pages using the Tabler CSS framework - the same approach
as MyTraL's make/generate_docs_from_markdown.py, adapted to the MindForger
Markdown dialect (metadata comments, notes written as '#' headings).

The navigation structure is defined by build/sitemap.md, the result is written
to distro/docs.mindforger.com/ and uploaded to https://docs.mindforger.com
"""

import argparse
import datetime
import re
import shutil
import sys
from dataclasses import dataclass, field
from html import escape
from pathlib import Path
from typing import Optional

import markdown
from pygments.formatters import HtmlFormatter


# Configuration
SITE_NAME = "MindForger Documentation"
SITE_BASE_URL = "https://docs.mindforger.com"
SITE_TAGLINE = "Thinking notebook and Markdown editor."
PROJECT_URL = "https://www.mindforger.com"
GITHUB_DOC_EDIT = "https://github.com/dvorka/mindforger-documentation/edit/main/memory/"
GITHUB_DOC_VIEW = "https://github.com/dvorka/mindforger-documentation/blob/main/memory/"
COPYRIGHT = "Copyright &copy; 2018-2026 MindForger "
PRODUCT = "Thinking Notebook"

# Pygments styles used for source code highlighting in light and dark theme
PYGMENTS_STYLE_LIGHT = "friendly"
PYGMENTS_STYLE_DARK = "monokai"

# image formats copied from the source directory next to the generated pages
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico"}

# Tabler icons used by the navigation menu
ICON_HOME = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-1"><path d="M5 12l-2 0l9 -9l9 9l-2 0" /><path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7" /><path d="M9 21v-6a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v6" /></svg>'
ICON_BOOK = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-1"><path d="M3 19a9 9 0 0 1 9 0a9 9 0 0 1 9 0" /><path d="M3 6a9 9 0 0 1 9 0a9 9 0 0 1 9 0" /><path d="M3 6l0 13" /><path d="M12 6l0 13" /><path d="M21 6l0 13" /></svg>'
ICON_CODE = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-1"><path d="M7 8l-4 4l4 4" /><path d="M17 8l4 4l-4 4" /><path d="M14 4l-4 16" /></svg>'
ICON_NEWS = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-1"><path d="M14 3v4a1 1 0 0 0 1 1h4" /><path d="M17 21h-10a2 2 0 0 1 -2 -2v-14a2 2 0 0 1 2 -2h7l5 5v11a2 2 0 0 1 -2 2" /><path d="M12 17a3 3 0 0 0 -3 -3" /><path d="M15 17a6 6 0 0 0 -6 -6" /><path d="M9 17h.01" /></svg>'
ICON_WORLD = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-1"><path d="M3 12a9 9 0 1 0 18 0a9 9 0 0 0 -18 0" /><path d="M3.6 9h16.8" /><path d="M3.6 15h16.8" /><path d="M11.5 3a17 17 0 0 0 0 18" /><path d="M12.5 3a17 17 0 0 1 0 18" /></svg>'
ICON_MOON = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-1"><path d="M12 3c.132 0 .263 0 .393 0a7.5 7.5 0 0 0 7.92 12.446a9 9 0 1 1 -8.313 -12.454z" /></svg>'
ICON_SUN = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-1"><path d="M12 12m-4 0a4 4 0 1 0 8 0a4 4 0 1 0 -8 0" /><path d="M3 12h1m8 -9v1m8 8h1m-9 8v1m-6.4 -15.4l.7 .7m12.1 -.7l-.7 .7m0 11.4l.7 .7m-12.1 -.7l-.7 .7" /></svg>'


@dataclass
class NavItem:
    """Navigation menu item."""
    title: str
    source: Optional[str] = None
    output: Optional[str] = None
    url: Optional[str] = None
    page_title: Optional[str] = None
    is_separator: bool = False


@dataclass
class NavSection:
    """Top-level navigation section."""
    title: str
    items: list[NavItem] = field(default_factory=list)


def parse_sitemap(sitemap_path: Path) -> list[NavSection]:
    """
    Parse build/sitemap.md to extract the navigation structure.

    Format:
    - ## Section Title (top-level menu)
    - ### Item Title (menu item)
    - ### --- (menu separator)
    - * [source](Notebook.md) (Markdown source of the item)
    - * [output](notebook.html) (optional output file name override)
    - * [url](https://...) (external link instead of a generated page)
    - * [title](Page Title) (optional page title override)

    Args:
        sitemap_path: Path to the sitemap Markdown file

    Returns:
        List of NavSection objects
    """
    if not sitemap_path.exists():
        print(f"Error: Sitemap not found: {sitemap_path}", file=sys.stderr)
        sys.exit(1)

    sections: list[NavSection] = []
    current_section: Optional[NavSection] = None

    for line in sitemap_path.read_text(encoding="utf-8").splitlines():
        line = line.rstrip()

        # ## Section Title
        match = re.match(r"^##\s+(.+)$", line)
        if match:
            current_section = NavSection(title=match.group(1).strip())
            sections.append(current_section)
            continue

        # ### Item Title | ### ---
        match = re.match(r"^###\s+(.+)$", line)
        if match and current_section:
            item_title = match.group(1).strip()
            current_section.items.append(
                NavItem(title=item_title, is_separator=item_title == "---")
            )
            continue

        # * [source|output|title](value)
        match = re.match(r"^\*\s*\[(source|output|url|title)\]\(([^)]+)\)", line)
        if match and current_section and current_section.items:
            key, value = match.group(1), match.group(2).strip()
            item = current_section.items[-1]
            if key == "source":
                item.source = value
            elif key == "output":
                item.output = value
            elif key == "url":
                item.url = value
            else:
                item.page_title = value

    return sections


def md_filename_to_html(md_filename: str) -> str:
    """Convert a Markdown file name to the default HTML file name."""
    # GETTING_STARTED.md -> getting-started.html: URLs of the site use hyphens
    return md_filename.replace(".md", ".html").lower().replace("_", "-")


def build_page_map(sections: list[NavSection]) -> dict[str, str]:
    """
    Map every Markdown source name to the name of the page generated from it.

    Args:
        sections: Parsed sitemap sections

    Returns:
        Dictionary of Markdown file name -> HTML file name
    """
    page_map = {}
    for section in sections:
        for item in section.items:
            if item.source:
                page_map[item.source] = item.output or md_filename_to_html(item.source)
    return page_map


def slugify(text: str) -> str:
    """
    Slugify a heading the way the GitHub wiki does it.

    Every character which is not a letter or a digit becomes a dash and repeated
    dashes are NOT collapsed - this is what makes the existing cross-document
    links like '#tayr--think-as-you-read' or '#open--free-and-fast' work.

    Args:
        text: Heading text, may contain inline HTML

    Returns:
        Anchor slug
    """
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"[^a-z0-9]", "-", text.strip().lower()).strip("-")


def strip_metadata(md_content: str) -> str:
    """
    Strip MindForger metadata and authoring hints from Markdown.

    MindForger stores note metadata in HTML comments appended to headings, e.g.
    '# Note <!-- Metadata: type: Note; ... -->'. All HTML comments are removed -
    the documentation uses them for metadata and authoring hints only.

    Args:
        md_content: Markdown content

    Returns:
        Markdown content without HTML comments
    """
    return re.sub(r"<!--.*?-->", "", md_content, flags=re.DOTALL)


def split_fenced_blocks(md_content: str):
    """
    Walk Markdown lines while tracking whether they are inside a fenced code block.

    Args:
        md_content: Markdown content

    Yields:
        Tuples of (line, is_code) - is_code is True inside ``` fenced blocks
    """
    in_fence = False
    for line in md_content.split("\n"):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            yield line, True
            continue
        yield line, in_fence


def extract_title(md_content: str) -> tuple[str, str]:
    """
    Take the notebook title from the first heading and remove it from the body.

    Args:
        md_content: Markdown content (metadata already stripped)

    Returns:
        Tuple of (title, remaining Markdown content)
    """
    lines = md_content.split("\n")
    for i, line in enumerate(lines):
        if re.match(r"^#\s+\S", line.strip()):
            title = line.strip().lstrip("#").strip()
            del lines[i]
            return title, "\n".join(lines)
    return SITE_NAME, md_content


def strip_inline_toc(md_content: str) -> str:
    """
    Remove a hand written 'Table of contents:' list from a notebook.

    Some notebooks (User documentation, Getting started) start with a manually
    maintained table of contents - the generated 'On this page' sidebar renders
    the same information, so the duplicate is dropped.

    Args:
        md_content: Markdown content

    Returns:
        Markdown content without the inline table of contents
    """
    lines = md_content.split("\n")
    result = []
    skipping = False

    for line in lines:
        if re.match(r"^\s*\**table of contents\**:?\s*$", line, flags=re.IGNORECASE):
            skipping = True
            continue
        if skipping:
            # the table of contents is a (nested) list, it ends with the first
            # line which is neither a list item nor blank
            if not line.strip() or re.match(r"^\s*([*+-]|\d+\.)\s", line):
                continue
            skipping = False
        result.append(line)

    return "\n".join(result)


def strip_duplicate_title(md_content: str, title: str) -> str:
    """
    Remove a leading heading which just repeats the page title.

    The page title is rendered by the page header, the Home notebook would
    otherwise show 'MindForger Documentation' twice.

    Args:
        md_content: Markdown content
        title: Page title

    Returns:
        Markdown content without the duplicated heading
    """
    lines = md_content.split("\n")
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match and match.group(1).strip().lower() == title.strip().lower():
            del lines[i]
        break
    return "\n".join(lines)


def demote_headings(md_content: str) -> str:
    """
    Demote all headings by one level.

    In MindForger notebooks both the notebook title and its top level notes are
    written as '#' headings. The notebook title is rendered as the page <h1> by
    the page header, so the notes are demoted to <h2>, <h3>, ... to keep exactly
    one <h1> per page and to make the table of contents work.

    Headings inside fenced code blocks (shell comments!) are left alone.

    Args:
        md_content: Markdown content without its title heading

    Returns:
        Markdown content with demoted headings
    """
    result = []
    for line, is_code in split_fenced_blocks(md_content):
        if not is_code and re.match(r"^#{1,5}\s+\S", line):
            line = "#" + line
        result.append(line)
    return "\n".join(result)


def rewrite_links(md_content: str, page_map: dict[str, str], md_name: str) -> str:
    """
    Rewrite links to other Markdown notebooks so that they point to HTML pages.

    '[x](GETTING_STARTED.md#note)' becomes '[x](getting-started.html#note)'.
    External links, image links and bare '#anchor' links are left alone.

    Args:
        md_content: Markdown content
        page_map: Markdown file name -> HTML file name
        md_name: Name of the source file (for warnings)

    Returns:
        Markdown content with rewritten links
    """
    # the sources are not consistent in the case of the linked file names,
    # e.g. both 'USER_DOCUMENTATION.md' and 'user-documentation.md' are used
    lower_page_map = {name.lower(): html for name, html in page_map.items()}

    def replace(match: re.Match) -> str:
        target, anchor = match.group(1), match.group(2) or ""
        html_name = lower_page_map.get(target.lower())
        if not html_name:
            print(f"  Warning: {md_name} links to an unpublished document: {target}")
            return match.group(0)
        return f"]({html_name}{anchor})"

    result = []
    for line, is_code in split_fenced_blocks(md_content):
        if not is_code:
            line = re.sub(r"\]\((?:\./)?([A-Za-z0-9._-]+\.md)(#[^)]*)?\)", replace, line)
        result.append(line)
    return "\n".join(result)


def add_heading_ids(html_content: str) -> tuple[str, list[tuple[int, str, str]]]:
    """
    Add GitHub wiki compatible id attributes to headings and collect them.

    Args:
        html_content: HTML string

    Returns:
        Tuple of (HTML with heading ids, list of (level, text, id) tuples)
    """
    headings: list[tuple[int, str, str]] = []
    used_slugs: dict[str, int] = {}

    def replace(match: re.Match) -> str:
        level, content = int(match.group(1)), match.group(2).strip()
        slug = slugify(content)

        # GitHub numbers repeated headings: 'build', 'build-1', 'build-2', ...
        count = used_slugs.get(slug, 0)
        used_slugs[slug] = count + 1
        if count:
            slug = f"{slug}-{count}"

        headings.append((level, re.sub(r"<[^>]+>", "", content), slug))
        return f'<h{level} id="{slug}">{content}</h{level}>'

    # python-markdown's toc extension collapses repeated dashes, so ids are
    # generated here from scratch - existing heading ids are overwritten
    html_content = re.sub(r"<h([2-6])[^>]*>(.*?)</h\1>", replace, html_content)
    return html_content, headings


def style_content(html_content: str) -> str:
    """
    Apply Tabler styling to the converted Markdown: cards, tables and images.

    Every <h2> section becomes a Tabler card, which gives the page the same look
    as the MyTraL documentation.

    Args:
        html_content: HTML converted from Markdown

    Returns:
        Styled HTML string
    """
    html_content = html_content.replace(
        "<table>", '<table class="table table-bordered table-vcenter">'
    )
    html_content = re.sub(
        r"<img([^>]*?)>", r'<img\1 class="img-fluid rounded border my-2">', html_content
    )

    # wrap each <h2> section into a card
    chunks = [c for c in re.split(r"(?=<h2[ >])", html_content.strip()) if c.strip()]
    return "\n".join(
        f'<div class="card mb-3"><div class="card-body">\n{chunk}\n</div></div>'
        for chunk in chunks
    )


def extract_description(md_content: str, title: str, max_length: int = 150) -> str:
    """
    Build a plain-text meta description from the first real sentence paragraph.

    Skips headings, images, lists, tables, code and section labels; falls back to
    a clean title-based default when no prose paragraph is found.

    Args:
        md_content: Markdown content
        title: Page title, used for the fallback description
        max_length: Maximum length of the returned description

    Returns:
        Plain-text, HTML-attribute-safe description string
    """
    for block in re.split(r"\n\s*\n", md_content):
        text = block.strip()
        # skip empty blocks, headings, images, lists, tables, code and quotes
        if not text or text[0] in "#!-*+|>" or text.startswith("```"):
            continue
        if re.match(r"^\d+\.", text):
            continue
        text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)      # drop images
        text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # links -> link text
        text = re.sub(r"<[^>]+>", "", text)                   # drop inline HTML
        text = re.sub(r"[*_`#]", "", text)                    # drop md formatting
        text = re.sub(r"\s+", " ", text).strip()
        # require a real sentence, not a short label ending in a colon
        if len(text) < 40 or text.endswith(":"):
            continue
        if len(text) > max_length:
            text = text[:max_length].rsplit(" ", 1)[0] + "..."
        return text.replace("&", "&amp;").replace('"', "&quot;")
    return f"{title} - MindForger, {SITE_TAGLINE}"


MATH_PATTERN = re.compile(r"\$\$.+?\$\$|\$(?=[^\s$])[^$\n]*?[^\s$\\]\$|\$[^\s$]\$", re.DOTALL)
CODE_PATTERN = re.compile(r"(^```.*?^```|~~~.*?~~~|`[^`\n]+`)", re.DOTALL | re.MULTILINE)


def protect_math(md_content: str) -> tuple[str, list[str]]:
    """
    Replace $...$ and $$...$$ math expressions with placeholders.

    Markdown would otherwise mangle the math (e.g. `_` and `\\{`) before KaTeX
    gets a chance to render it in the browser. Code blocks and code spans are
    left untouched.

    Args:
        md_content: Markdown content

    Returns:
        Tuple of (Markdown with placeholders, math expressions)
    """
    expressions: list[str] = []

    def stash(match: re.Match) -> str:
        expressions.append(match.group(0))
        return f"MFMATHPLACEHOLDER{len(expressions) - 1}X"

    parts = CODE_PATTERN.split(md_content)
    # split() with a group: odd items are code, even items are text
    for i in range(0, len(parts), 2):
        parts[i] = MATH_PATTERN.sub(stash, parts[i])
    return "".join(parts), expressions


def restore_math(html_content: str, expressions: list[str]) -> str:
    """Put the math expressions back into the HTML (escaped for HTML text)."""
    return re.sub(
        r"MFMATHPLACEHOLDER(\d+)X",
        lambda match: escape(expressions[int(match.group(1))], quote=False),
        html_content,
    )


def markdown_to_html(md_content: str) -> str:
    """
    Convert Markdown to HTML.

    Args:
        md_content: Markdown content

    Returns:
        HTML string
    """
    converter = markdown.Markdown(
        extensions=["extra", "tables", "fenced_code", "codehilite", "sane_lists"],
        extension_configs={"codehilite": {"guess_lang": False}},
    )
    return converter.convert(md_content)


def generate_navbar_html(
    sections: list[NavSection], page_map: dict[str, str], active_page: str
) -> str:
    """
    Generate the Tabler navbar with a dropdown menu per sitemap section.

    Args:
        sections: Parsed sitemap sections
        page_map: Markdown file name -> HTML file name
        active_page: Current page file name, highlighted in the menu

    Returns:
        Navbar HTML string
    """
    dropdowns = []
    for section in sections:
        items_html = []
        for item in section.items:
            if item.is_separator:
                items_html.append('<div class="dropdown-divider"></div>')
            elif item.url:
                items_html.append(
                    f'<a class="dropdown-item" href="{item.url}" target="_blank" '
                    f'rel="noopener">{item.title}</a>'
                )
            elif item.source:
                href = page_map[item.source]
                active = " active" if href == active_page else ""
                items_html.append(
                    f'<a class="dropdown-item{active}" href="{href}">{item.title}</a>'
                )

        title = section.title.lower()
        if "technical" in title or "developer" in title:
            icon = ICON_CODE
        elif "home" in title:
            icon = ICON_HOME
        elif "news" in title:
            icon = ICON_NEWS
        else:
            icon = ICON_BOOK

        section_active = " active" if any(
            item.source and page_map[item.source] == active_page
            for item in section.items
        ) else ""

        dropdowns.append(f'''<li class="nav-item dropdown{section_active}">
                        <a class="nav-link dropdown-toggle" href="#navbar-base"
                           data-bs-toggle="dropdown" data-bs-auto-close="outside"
                           role="button" aria-expanded="false">
                          <span class="nav-link-icon d-md-none d-lg-inline-block">{icon}</span>
                          <span class="nav-link-title">{section.title}</span>
                        </a>
                        <div class="dropdown-menu">
                          <div class="dropdown-menu-columns">
                            <div class="dropdown-menu-column">
                              {chr(10).join(items_html)}
                            </div>
                          </div>
                        </div>
                      </li>''')

    return f'''<div class="sticky-top">
        <header class="navbar navbar-expand-md d-print-none">
          <div class="container-xl">
            <!-- BEGIN NAVBAR TOGGLER -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbar-menu" aria-controls="navbar-menu"
                    aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <!-- END NAVBAR TOGGLER -->
            <!-- BEGIN NAVBAR LOGO -->
            <div class="navbar-brand navbar-brand-autodark d-none-navbar-horizontal pe-0 pe-md-3">
              <a href="index.html" class="mf-brand">
                <img src="assets/mind-forger.png" alt="MindForger" class="mf-brand-logo">
                <span class="mf-brand-text">MindForger</span>
              </a>
            </div>
            <!-- END NAVBAR LOGO -->
            <div class="navbar-nav flex-row order-md-last">
              <div class="d-none d-md-flex">
                <div class="nav-item">
                  <a href="?theme=dark" class="nav-link px-0 hide-theme-dark"
                     title="Enable dark mode" data-bs-toggle="tooltip" data-bs-placement="bottom">{ICON_MOON}</a>
                  <a href="?theme=light" class="nav-link px-0 hide-theme-light"
                     title="Enable light mode" data-bs-toggle="tooltip" data-bs-placement="bottom">{ICON_SUN}</a>
                </div>
              </div>
            </div>
          </div>
        </header>
        <header class="navbar-expand-md">
          <div class="collapse navbar-collapse" id="navbar-menu">
            <div class="navbar">
              <div class="container-xl">
                <div class="row flex-column flex-md-row flex-fill align-items-center">
                  <div class="col">
                    <!-- BEGIN NAVBAR MENU -->
                    <ul class="navbar-nav" id="navbar-base">
                      {chr(10).join(dropdowns)}
                    </ul>
                    <!-- END NAVBAR MENU -->
                  </div>
                  <div class="col col-md-auto">
                    <ul class="navbar-nav">
                      <li class="nav-item">
                        <a class="nav-link" href="{PROJECT_URL}" target="_blank">
                          <span class="nav-link-icon d-md-none d-lg-inline-block">{ICON_WORLD}</span>
                          <span class="nav-link-title">mindforger.com</span>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </header>
      </div>'''


def generate_toc_html(headings: list[tuple[int, str, str]]) -> str:
    """
    Generate the 'On this page' sidebar from the page headings.

    Args:
        headings: List of (level, text, id) tuples

    Returns:
        HTML string, empty when the page has no headings
    """
    items = [
        f'<a href="#{slug}" class="nav-link{" ms-3 small" if level > 2 else ""}">{text}</a>'
        for level, text, slug in headings
        if level <= 3
    ]
    if not items:
        return ""

    return f'''<div class="mf-toc sticky-top">
              <div class="mf-toc-title">On this page</div>
              <div class="nav nav-vertical" id="toc">
                {chr(10).join(items)}
              </div>
            </div>'''


def generate_footer_html(md_filename: str) -> str:
    """
    Generate the single line page footer.

    Args:
        md_filename: Markdown source of the page, linked to GitHub

    Returns:
        Footer HTML string
    """
    return f'''<footer class="footer footer-transparent d-print-none">
          <div class="container-xl">
            <ul class="list-inline list-inline-dots mb-0 text-center">
              <li class="list-inline-item">{COPYRIGHT}</li>
              <li class="list-inline-item">{PRODUCT}</li>
              <li class="list-inline-item">Doc made with <a href="{PROJECT_URL}" target="_blank">MindForger</a></li>
              <li class="list-inline-item"><a href="{GITHUB_DOC_EDIT}{md_filename}" target="_blank">Edit on GitHub</a></li>
              <li class="list-inline-item"><a href="{GITHUB_DOC_VIEW}{md_filename}" target="_blank">Source</a></li>
            </ul>
          </div>
        </footer>'''


# KaTeX is loaded only by the pages which contain math ($...$ and $$...$$ - the
# same delimiters as in the MindForger app)
KATEX_STYLES = '<link href="assets/katex/katex.min.css" rel="stylesheet" />'
KATEX_SCRIPTS = """<script src="assets/katex/katex.min.js" defer></script>
    <script src="assets/katex/auto-render.min.js" defer></script>
    <script defer>
      document.addEventListener("DOMContentLoaded", function () {
        renderMathInElement(document.body, {
          delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "$", right: "$", display: false}
          ]
        });
      });
    </script>"""


def get_html_template() -> str:
    """
    Get the base HTML template for documentation pages.

    Returns:
        HTML template string
    """
    return '''<!doctype html>
<html lang="en" data-bs-theme="light">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
    <title>{{TITLE}} - MindForger Documentation</title>
    <meta name="description" content="{{DESCRIPTION}}" />
    <meta name="author" content="Martin.Dvorak@mindforger.com" />
    <link rel="canonical" href="{{CANONICAL}}" />
    <link rel="icon" href="assets/favicon.ico" type="image/x-icon" />
    <link rel="icon" href="assets/mind-forger.png" type="image/png" />
    <meta name="theme-color" content="#008c00" />

    <!-- BEGIN OPEN GRAPH -->
    <meta property="og:site_name" content="MindForger Documentation" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="{{TITLE}} - MindForger Documentation" />
    <meta property="og:description" content="{{DESCRIPTION}}" />
    <meta property="og:url" content="{{CANONICAL}}" />
    <meta property="og:image" content="{{OG_IMAGE}}" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{{TITLE}} - MindForger Documentation" />
    <meta name="twitter:description" content="{{DESCRIPTION}}" />
    <meta name="twitter:image" content="{{OG_IMAGE}}" />
    <!-- END OPEN GRAPH -->

    <!-- BEGIN STYLES -->
    <link href="assets/tabler/css/tabler.min.css" rel="stylesheet" />
    <link href="assets/tabler/css/tabler-props.min.css" rel="stylesheet" />
    <link href="assets/tabler/css/tabler-themes.min.css" rel="stylesheet" />
    <link href="assets/pygments.css" rel="stylesheet" />
    <link href="assets/mindforger-docs.css" rel="stylesheet" />
    {{KATEX_STYLES}}
    <!-- END STYLES -->

    <!-- BEGIN THEME SCRIPT: light/dark theme, must run before the page renders -->
    <script src="assets/tabler/js/tabler-theme.min.js"></script>
    <!-- END THEME SCRIPT -->
  </head>
  <body>
    <div class="page">
      <!-- BEGIN NAVBAR -->
      {{NAVBAR}}
      <!-- END NAVBAR -->
      <div class="page-wrapper">
        <!-- BEGIN PAGE HEADER -->
        <div class="page-header d-print-none" aria-label="Page header">
          <div class="container-xl">
            <div class="row g-2 align-items-center">
              <div class="col">
                <div class="page-pretitle">{{PRETITLE}}</div>
                <h1 class="page-title">{{TITLE}}</h1>
              </div>
            </div>
          </div>
        </div>
        <!-- END PAGE HEADER -->

        <div class="page-body">
          <div class="container-xl">
            <div class="row">
              <!-- BEGIN MAIN CONTENT -->
              <div class="col-12 col-xl-9">
                {{CONTENT}}
              </div>
              <!-- END MAIN CONTENT -->
              <!-- BEGIN TABLE OF CONTENTS -->
              <div class="col-3 d-none d-xl-block">
                {{TOC}}
              </div>
              <!-- END TABLE OF CONTENTS -->
            </div>
          </div>
        </div>

        <!-- BEGIN FOOTER -->
        {{FOOTER}}
        <!-- END FOOTER -->
      </div>
    </div>
    <script src="assets/tabler/js/tabler.min.js" defer></script>
    {{KATEX_SCRIPTS}}
  </body>
</html>
'''


def generate_page(
    item: NavItem,
    section: NavSection,
    source_dir: Path,
    output_dir: Path,
    sections: list[NavSection],
    page_map: dict[str, str],
) -> tuple[str, list[str]]:
    """
    Generate one HTML page from a Markdown notebook.

    Args:
        item: Sitemap item to generate
        section: Sitemap section the item belongs to
        source_dir: Directory with the Markdown sources
        output_dir: Directory to write the page to
        sections: All sitemap sections (navigation)
        page_map: Markdown file name -> HTML file name

    Returns:
        Tuple of (generated file name, anchors defined by the page)
    """
    md_path = source_dir / item.source
    html_name = page_map[item.source]
    print(f"Generating: {item.source} -> {html_name}")

    md_content = strip_metadata(md_path.read_text(encoding="utf-8"))
    title, md_content = extract_title(md_content)
    if item.page_title:
        title = item.page_title

    description = extract_description(md_content, title)
    md_content = strip_duplicate_title(md_content, title)
    md_content = strip_inline_toc(md_content)
    md_content = demote_headings(md_content)
    md_content = rewrite_links(md_content, page_map, item.source)

    md_content, math = protect_math(md_content)
    html_content = markdown_to_html(md_content)
    html_content = restore_math(html_content, math)
    html_content, headings = add_heading_ids(html_content)
    html_content = style_content(html_content)

    html = get_html_template()
    html = html.replace("{{KATEX_STYLES}}", KATEX_STYLES if math else "")
    html = html.replace("{{KATEX_SCRIPTS}}", KATEX_SCRIPTS if math else "")
    html = html.replace("{{NAVBAR}}", generate_navbar_html(sections, page_map, html_name))
    html = html.replace("{{TOC}}", generate_toc_html(headings))
    html = html.replace("{{FOOTER}}", generate_footer_html(item.source))
    html = html.replace("{{CONTENT}}", html_content)
    html = html.replace("{{PRETITLE}}", section.title)
    html = html.replace("{{TITLE}}", title)
    html = html.replace("{{DESCRIPTION}}", description)
    html = html.replace("{{CANONICAL}}", f"{SITE_BASE_URL}/{html_name}")
    html = html.replace("{{OG_IMAGE}}", f"{SITE_BASE_URL}/assets/mind-forger.png")

    (output_dir / html_name).write_text(html, encoding="utf-8")
    return html_name, [slug for _, _, slug in headings]


def copy_assets(assets_dir: Path, output_dir: Path) -> int:
    """
    Copy the vendored web assets and generate the source code highlighting CSS.

    Args:
        assets_dir: build/assets directory
        output_dir: Site root directory

    Returns:
        Number of asset files copied
    """
    target = output_dir / "assets"
    shutil.copytree(assets_dir, target, dirs_exist_ok=True)
    copied = sum(1 for path in target.rglob("*") if path.is_file())

    # source code highlighting: Pygments styles for the light and dark theme
    light = HtmlFormatter(style=PYGMENTS_STYLE_LIGHT).get_style_defs(".codehilite")
    dark = HtmlFormatter(style=PYGMENTS_STYLE_DARK).get_style_defs(
        '[data-bs-theme="dark"] .codehilite'
    )
    (target / "pygments.css").write_text(
        f"/* Pygments '{PYGMENTS_STYLE_LIGHT}' (light theme) */\n{light}\n"
        f"/* Pygments '{PYGMENTS_STYLE_DARK}' (dark theme) */\n{dark}\n",
        encoding="utf-8",
    )
    return copied + 1


def copy_images(source_dir: Path, output_dir: Path) -> int:
    """
    Copy the images of the documentation next to the generated pages.

    The pages reference the images by their plain file name, exactly as the
    Markdown sources do.

    Args:
        source_dir: Directory with the Markdown sources
        output_dir: Site root directory

    Returns:
        Number of images copied
    """
    images = [
        path for path in sorted(source_dir.iterdir())
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
    ]
    for image in images:
        shutil.copy2(image, output_dir / image.name)
    return len(images)


def generate_sitemap_xml(output_dir: Path, pages: list[str]) -> None:
    """
    Generate sitemap.xml and robots.txt at the site root.

    Args:
        output_dir: Site root directory
        pages: Names of the generated HTML pages
    """
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for page in pages:
        html_file = output_dir / page
        lastmod = datetime.date.fromtimestamp(html_file.stat().st_mtime).isoformat()
        loc = SITE_BASE_URL + ("/" if page == "index.html" else f"/{page}")
        lines.append("    <url>")
        lines.append(f"        <loc>{loc}</loc>")
        lines.append(f"        <lastmod>{lastmod}</lastmod>")
        lines.append("        <changefreq>monthly</changefreq>")
        lines.append(f"        <priority>{'1.0' if page == 'index.html' else '0.7'}</priority>")
        lines.append("    </url>")
    lines.append("</urlset>")

    (output_dir / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (output_dir / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_BASE_URL}/sitemap.xml\n",
        encoding="utf-8",
    )
    print(f"Generated: sitemap.xml ({len(pages)} URLs) and robots.txt")


def main() -> int:
    """Main entry point."""
    build_dir = Path(__file__).resolve().parent.parent
    root_dir = build_dir.parent

    parser = argparse.ArgumentParser(
        description="Generate the docs.mindforger.com website from Markdown sources"
    )
    parser.add_argument(
        "--source-dir", type=Path, default=root_dir / "memory",
        help="Directory with the Markdown sources (default: memory)",
    )
    parser.add_argument(
        "--sitemap", type=Path, default=build_dir / "sitemap.md",
        help="Sitemap defining the navigation (default: build/sitemap.md)",
    )
    parser.add_argument(
        "--assets-dir", type=Path, default=build_dir / "assets",
        help="Directory with the vendored web assets (default: build/assets)",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=root_dir / "distro" / "docs.mindforger.com",
        help="Site root directory (default: distro/docs.mindforger.com)",
    )
    args = parser.parse_args()

    if not args.source_dir.is_dir():
        print(f"Error: Source directory not found: {args.source_dir}", file=sys.stderr)
        return 1
    if not (args.assets_dir / "tabler" / "css" / "tabler.min.css").exists():
        print(
            f"Error: Tabler not found in {args.assets_dir} - run 'make doc-assets'",
            file=sys.stderr,
        )
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)

    sections = parse_sitemap(args.sitemap)
    page_map = build_page_map(sections)
    print(f"Sitemap: {len(sections)} section(s), {len(page_map)} page(s)\n")

    pages: list[str] = []
    anchors: dict[str, list[str]] = {}
    for section in sections:
        for item in section.items:
            if item.is_separator or not item.source:
                continue
            if not (args.source_dir / item.source).exists():
                print(f"Error: Markdown source not found: {item.source}", file=sys.stderr)
                return 1
            html_name, page_anchors = generate_page(
                item, section, args.source_dir, args.output_dir,
                sections, page_map,
            )
            pages.append(html_name)
            anchors[html_name] = page_anchors

    images = copy_images(args.source_dir, args.output_dir)
    assets = copy_assets(args.assets_dir, args.output_dir)
    generate_sitemap_xml(args.output_dir, pages)

    print(f"\nDONE {len(pages)} page(s), {images} image(s), {assets} asset file(s)")
    print(f"Output: {args.output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
