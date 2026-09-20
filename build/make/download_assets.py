#!/usr/bin/env python3
"""
Download 3rd party web assets vendored by the MindForger documentation build.

Fetches the Tabler CSS framework and the KaTeX math renderer (npm tarballs) and the Lato web font (Google
Fonts) into build/assets/ so that the generated site at www.mindforger.com/docs is
self-contained - no CDN is needed at build time nor by the site visitors.

The downloaded files are meant to be committed to this repository: run this
script only when a dependency should be upgraded.
"""

import argparse
import io
import re
import shutil
import sys
import tarfile
import urllib.request
from datetime import date
from pathlib import Path


# Configuration
TABLER_VERSION = "1.5.1"
TABLER_TARBALL = "https://registry.npmjs.org/@tabler/core/-/core-{version}.tgz"

# Tabler files vendored from the tarball: the framework itself, its CSS custom
# properties and the light/dark theme support. The 20+ MB dist/libs/ folder with
# charting and form plugins is deliberately NOT vendored - docs don't use it.
TABLER_FILES = [
    "dist/css/tabler.min.css",
    "dist/css/tabler-props.min.css",
    "dist/css/tabler-themes.min.css",
    "dist/js/tabler.min.js",
    "dist/js/tabler-theme.min.js",
]

# KaTeX renders the math in the pages; the version matches the MindForger app
KATEX_VERSION = "0.18.7"
KATEX_TARBALL = "https://registry.npmjs.org/katex/-/katex-{version}.tgz"
KATEX_FILES = [
    "dist/katex.min.css",
    "dist/katex.min.js",
    "dist/contrib/auto-render.min.js",
]
# the stylesheet references fonts/*.woff2 relative to itself; woff2 is supported
# by every current browser so the ttf/woff fallbacks are not vendored
KATEX_FONTS_PREFIX = "package/dist/fonts/"

# fonts of the comics: (family, Google Fonts query, file name)
GOOGLE_FONTS_API = "https://fonts.googleapis.com/css2?family={query}&display=swap"
COMIC_FONTS = [
    ("Bangers", "Bangers", "bangers.woff2"),
    ("Comic Neue", "Comic+Neue:wght@700", "comic-neue-700.woff2"),
]

# Lato: the font of www.mindforger.com
GOOGLE_FONTS_CSS = "https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap"
# a modern browser UA is required, otherwise Google Fonts serves legacy formats
BROWSER_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


def fetch(url: str, accept_any_format: bool = False) -> bytes:
    """Download an URL and return its body."""
    print(f"  GET {url}")
    headers = {"User-Agent": BROWSER_UA} if accept_any_format else {}
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def download_tabler(version: str, assets_dir: Path) -> str:
    """
    Download the Tabler npm tarball and extract the vendored files.

    Args:
        version: Tabler version to download
        assets_dir: build/assets directory

    Returns:
        Version string of the Tabler release written to disk
    """
    print(f"Tabler {version}:")
    tarball = fetch(TABLER_TARBALL.format(version=version))

    tabler_dir = assets_dir / "tabler"
    if tabler_dir.exists():
        shutil.rmtree(tabler_dir)

    with tarfile.open(fileobj=io.BytesIO(tarball), mode="r:gz") as tar:
        for wanted in TABLER_FILES:
            # npm tarballs put everything below a 'package/' prefix
            member = tar.getmember(f"package/{wanted}")
            source = tar.extractfile(member)
            if source is None:
                raise RuntimeError(f"Not a file in the Tabler tarball: {wanted}")

            # dist/css/tabler.min.css -> build/assets/tabler/css/tabler.min.css
            target = tabler_dir / Path(wanted).relative_to("dist")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read())
            print(f"  {target.relative_to(assets_dir)} ({target.stat().st_size:,} B)")

    return version


def download_katex(version: str, assets_dir: Path) -> str:
    """
    Download the KaTeX npm tarball and extract the vendored files.

    Args:
        version: KaTeX version to download
        assets_dir: build/assets directory

    Returns:
        Version string of the KaTeX release written to disk
    """
    print(f"KaTeX {version}:")
    tarball = fetch(KATEX_TARBALL.format(version=version))

    katex_dir = assets_dir / "katex"
    if katex_dir.exists():
        shutil.rmtree(katex_dir)

    with tarfile.open(fileobj=io.BytesIO(tarball), mode="r:gz") as tar:
        wanted = {f"package/{name}": name for name in KATEX_FILES}
        for member in tar.getmembers():
            if member.name in wanted:
                # dist/katex.min.css -> build/assets/katex/katex.min.css
                # dist/contrib/auto-render.min.js -> build/assets/katex/auto-render.min.js
                target = katex_dir / Path(wanted[member.name]).name
            elif member.name.startswith(KATEX_FONTS_PREFIX) and member.name.endswith(".woff2"):
                target = katex_dir / "fonts" / Path(member.name).name
            else:
                continue
            source = tar.extractfile(member)
            if source is None:
                raise RuntimeError(f"Not a file in the KaTeX tarball: {member.name}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read())
            print(f"  {target.relative_to(assets_dir)} ({target.stat().st_size:,} B)")

    if not (katex_dir / "katex.min.js").exists() or not (katex_dir / "auto-render.min.js").exists():
        raise RuntimeError("KaTeX files not found in the tarball")

    return version


def download_lato(assets_dir: Path) -> str:
    """
    Download the Lato woff2 files referenced by the Google Fonts stylesheet.

    Only the latin subsets of the regular (400) and bold (700) weights are kept
    - that is what the documentation pages use.

    Args:
        assets_dir: build/assets directory

    Returns:
        Description of what was written to disk
    """
    print("Lato (Google Fonts):")
    css = fetch(GOOGLE_FONTS_CSS, accept_any_format=True).decode("utf-8")

    fonts_dir = assets_dir / "fonts"
    fonts_dir.mkdir(parents=True, exist_ok=True)

    # the stylesheet lists one @font-face per weight and unicode subset, the
    # latin one always comes last => keep the last URL seen for each weight
    weight_to_url: dict[str, str] = {}
    for block in css.split("@font-face")[1:]:
        weight = re.search(r"font-weight:\s*(\d+)", block)
        url = re.search(r"url\((https://[^)]+\.woff2)\)", block)
        if weight and url and weight.group(1) in ("400", "700"):
            weight_to_url[weight.group(1)] = url.group(1)

    if set(weight_to_url) != {"400", "700"}:
        raise RuntimeError(f"Lato woff2 not found for both weights: {sorted(weight_to_url)}")

    for weight, url in sorted(weight_to_url.items()):
        target = fonts_dir / f"lato-{weight}.woff2"
        target.write_bytes(fetch(url, accept_any_format=True))
        print(f"  {target.relative_to(assets_dir)} ({target.stat().st_size:,} B)")

    return "latin 400, 700"


def download_comic_fonts(assets_dir: Path) -> str:
    """
    Download the display fonts of the comics (Bangers and Comic Neue Bold).

    Only the latin subset is kept, the fonts are referenced from
    build/assets/comics/comics.css.

    Args:
        assets_dir: build/assets directory

    Returns:
        Description of what was written to disk
    """
    print("Comics fonts (Google Fonts):")
    fonts_dir = assets_dir / "comics" / "fonts"
    fonts_dir.mkdir(parents=True, exist_ok=True)

    for family, query, target_name in COMIC_FONTS:
        css = fetch(GOOGLE_FONTS_API.format(query=query), accept_any_format=True).decode("utf-8")
        # the latin subset comes last in the stylesheet
        urls = re.findall(r"url\((https://[^)]+\.woff2)\)", css)
        if not urls:
            raise RuntimeError(f"woff2 not found for {family}")
        target = fonts_dir / target_name
        target.write_bytes(fetch(urls[-1], accept_any_format=True))
        print(f"  {target.relative_to(assets_dir)} ({target.stat().st_size:,} B)")

    return "Bangers, Comic Neue 700"


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Download web assets vendored by the documentation build"
    )
    parser.add_argument(
        "--assets-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "assets",
        help="Target directory (default: build/assets)",
    )
    parser.add_argument(
        "--tabler-version",
        default=TABLER_VERSION,
        help=f"Tabler version to download (default: {TABLER_VERSION})",
    )
    args = parser.parse_args()

    assets_dir: Path = args.assets_dir
    assets_dir.mkdir(parents=True, exist_ok=True)

    try:
        tabler = download_tabler(args.tabler_version, assets_dir)
        katex = download_katex(KATEX_VERSION, assets_dir)
        lato = download_lato(assets_dir)
        comic_fonts = download_comic_fonts(assets_dir)
    except Exception as exception:  # network, tarball layout, Google Fonts change
        print(f"Error: failed to download assets: {exception}", file=sys.stderr)
        return 1

    versions = assets_dir / "VERSIONS.txt"
    versions.write_text(
        "MindForger documentation - vendored 3rd party web assets\n"
        f"Updated: {date.today().isoformat()}\n"
        "\n"
        f"Tabler: {tabler} (MIT) - https://tabler.io\n"
        f"KaTeX:  {katex} (MIT) - https://katex.org\n"
        f"Comics: {comic_fonts} (OFL) - https://fonts.google.com\n"
        f"Lato:   {lato} (OFL) - https://fonts.google.com/specimen/Lato\n",
        encoding="utf-8",
    )
    print(f"\nDONE assets written to {assets_dir} - commit them to git")
    print(versions.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
