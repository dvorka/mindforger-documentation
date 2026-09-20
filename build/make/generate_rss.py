#!/usr/bin/env python3
"""
Generate the RSS feed of the MindForger blog.

Every '## ' section of the BLOG.md notebook is a blog post: the heading is the
title of the post and the first line of the section starts with the date of the
post in the '*YYYY-MM-DD*' form. The feed is written to rss.xml in the root of
the generated site, run it after generate_docs.py - see build/Makefile.
"""

import argparse
import datetime
import re
import sys
from dataclasses import dataclass
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape

# generate_docs.py lives next to this script
sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_docs as docs  # noqa: E402


# Configuration
BLOG_MD = "BLOG.md"
BLOG_PAGE = "blog.html"
FEED_FILE = "rss.xml"
FEED_TITLE = "MindForger Blog"
FEED_DESCRIPTION = "News and articles about MindForger - thinking notebook and Markdown editor."


@dataclass
class Post:
    """Blog post - one section of BLOG.md."""
    title: str
    date: datetime.date
    markdown: str

    @property
    def link(self) -> str:
        # the page ids are made from the rendered heading, e.g. '&' is '&amp;'
        return f"{docs.SITE_BASE_URL}/{BLOG_PAGE}#{docs.slugify(escape(self.title))}"


def parse_posts(md_content: str) -> list[Post]:
    """
    Split the blog Markdown to posts.

    Args:
        md_content: BLOG.md content without metadata

    Returns:
        Posts in the order they have in the notebook, sections without a date
        are skipped with a warning
    """
    posts: list[Post] = []
    # sections start with '## ', the '#' inside fenced code blocks is ignored
    sections: list[list[str]] = []
    fenced = False
    for line in md_content.splitlines():
        if line.startswith(("```", "~~~")):
            fenced = not fenced
        if not fenced and re.match(r"^##\s+\S", line):
            sections.append([line])
        elif sections:
            sections[-1].append(line)

    for lines in sections:
        title = re.sub(r"^##\s+", "", lines[0]).strip()
        body = "\n".join(lines[1:]).strip()
        match = re.match(r"^\*(\d{4}-\d{2}-\d{2})\*", body)
        if not match:
            print(f"Warning: blog post without '*YYYY-MM-DD*' date skipped: {title}",
                  file=sys.stderr)
            continue
        posts.append(Post(title, datetime.date.fromisoformat(match.group(1)), body))
    return posts


def absolutize_urls(html_content: str) -> str:
    """Make the links and images of a post absolute - feed readers have no base URL."""
    def replace(match: re.Match) -> str:
        attribute, url = match.group(1), match.group(2)
        if url.startswith("#"):
            url = f"{docs.SITE_BASE_URL}/{BLOG_PAGE}{url}"
        elif not re.match(r"^([a-z][a-z0-9+.-]*:|//)", url, re.IGNORECASE):
            url = f"{docs.SITE_BASE_URL}/{url.removeprefix('./')}"
        return f'{attribute}="{url}"'

    return re.sub(r'\b(href|src)="([^"]*)"', replace, html_content)


def post_to_html(post: Post, page_map: dict[str, str]) -> str:
    """Render the post (without its title) to HTML for the feed."""
    md_content = docs.rewrite_links(post.markdown, page_map, BLOG_MD)
    md_content, math = docs.protect_math(md_content)
    html_content = docs.markdown_to_html(md_content)
    return absolutize_urls(docs.restore_math(html_content, math))


def generate_rss(posts: list[Post], page_map: dict[str, str]) -> str:
    """
    Generate RSS 2.0 feed.

    Args:
        posts: Blog posts
        page_map: Markdown file name -> HTML file name

    Returns:
        RSS XML
    """
    def rfc822(date: datetime.date) -> str:
        return format_datetime(datetime.datetime.combine(
            date, datetime.time(12, 0), tzinfo=datetime.timezone.utc))

    newest = max(post.date for post in posts)
    items = []
    for post in posts:
        html_content = post_to_html(post, page_map).replace("]]>", "]]&gt;")
        items.append(f"""    <item>
      <title>{escape(post.title)}</title>
      <link>{escape(post.link)}</link>
      <guid isPermaLink="true">{escape(post.link)}</guid>
      <pubDate>{rfc822(post.date)}</pubDate>
      <description><![CDATA[{html_content}]]></description>
    </item>""")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{escape(FEED_TITLE)}</title>
    <link>{docs.SITE_BASE_URL}/{BLOG_PAGE}</link>
    <description>{escape(FEED_DESCRIPTION)}</description>
    <language>en</language>
    <lastBuildDate>{rfc822(newest)}</lastBuildDate>
    <atom:link href="{docs.SITE_BASE_URL}/{FEED_FILE}" rel="self" type="application/rss+xml" />
{chr(10).join(items)}
  </channel>
</rss>
"""


def main() -> int:
    """Main entry point."""
    root_dir = Path(__file__).resolve().parent.parent.parent
    parser = argparse.ArgumentParser(description="Generate the RSS feed of the blog")
    parser.add_argument("--source-dir", type=Path, default=root_dir / "memory",
                        help="Directory with the Markdown sources (default: memory)")
    parser.add_argument("--sitemap", type=Path, default=root_dir / "build" / "sitemap.md",
                        help="Sitemap defining the pages (default: build/sitemap.md)")
    parser.add_argument("--output-dir", type=Path,
                        default=root_dir / "distro" / "www.mindforger.com" / "docs",
                        help="Site root directory (default: distro/www.mindforger.com/docs)")
    args = parser.parse_args()

    blog = args.source_dir / BLOG_MD
    if not blog.exists():
        print(f"Error: blog not found: {blog}", file=sys.stderr)
        return 1

    page_map = docs.build_page_map(docs.parse_sitemap(args.sitemap))
    md_content = docs.strip_metadata(blog.read_text(encoding="utf-8"))
    posts = parse_posts(md_content)
    if not posts:
        print("Error: no blog post found", file=sys.stderr)
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)
    feed = args.output_dir / FEED_FILE
    feed.write_text(generate_rss(posts, page_map), encoding="utf-8")
    print(f"Generated: {FEED_FILE} ({len(posts)} post(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
