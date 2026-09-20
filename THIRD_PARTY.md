# Third party content

This repository contains the MindForger documentation and the scripts which
generate the https://www.mindforger.com/docs website from it. The documentation
itself is licensed under [LICENSE](LICENSE). The third party components below
are **not** covered by that license - each one keeps its own.

## Web assets (vendored in `build/assets/`)

These files are copied into the generated website. They are downloaded by
`make doc-assets` (see `build/make/download_assets.py`) and the exact versions
are recorded in `build/assets/VERSIONS.txt`.

| Component | Version | License | Files | Source |
|-----------|---------|---------|-------|--------|
| Tabler (UI framework, based on Bootstrap) | 1.5.1 | MIT | `build/assets/tabler/` | https://tabler.io |
| KaTeX (math rendering) | 0.18.7 | MIT | `build/assets/katex/` | https://katex.org |
| Lato (font, latin 400 and 700) | Google Fonts v25 | SIL OFL 1.1 | `build/assets/fonts/` | https://fonts.google.com/specimen/Lato |

Copyright notices:

* **Tabler**: Copyright 2018-2026 The Tabler Authors, Copyright 2018-2026
  codecalm.net Paweł Kuna. MIT License:
  https://github.com/tabler/tabler/blob/master/LICENSE
* **KaTeX**: Copyright (c) 2013-2020 Khan Academy and other contributors. MIT
  License: https://github.com/KaTeX/KaTeX/blob/main/LICENSE. The `KaTeX_*.woff2`
  fonts are distributed as a part of the KaTeX package.
* **Lato**: Copyright (c) 2010-2014 by tyPoland Lukasz Dziedzic
  (team@latofonts.com) with Reserved Font Name "Lato". Licensed under the SIL
  Open Font License, Version 1.1: https://openfontlicense.org

## Generated content

* `assets/pygments.css` (source code highlighting) is generated at build time
  from the `friendly` and `monokai` styles of [Pygments](https://pygments.org)
  (BSD-2-Clause). Nothing else of Pygments is distributed.

## Build tools (not distributed)

The generator scripts run on the following Python libraries, which are
installed by the user (`pip3 install --user markdown pygments`) and are **not**
part of this repository nor of the generated website:

* [Python-Markdown](https://python-markdown.github.io) (BSD-3-Clause)
* [Pygments](https://pygments.org) (BSD-2-Clause)

## Documentation content

* Release notes and screenshots in `memory/BLOG.md` and the `BLOG.*` images were
  written by the MindForger author and published earlier at
  https://github.com/dvorka/mindforger/releases and
  https://blog.mindforger.com.
* The opening quote of the *Computers Need To Forget* blog post summarizes an
  Ars Technica article (linked in the post) and is used as a quotation.
* Third party projects, libraries and people MindForger itself builds upon are
  acknowledged in [CREDITS.md](memory/CREDITS.md).
