# MindForger Documentation Repository
This **private** repository is where MindForger documentation is written. 

* [Sidebar](./memory/_Sidebar.md)
* [Home](./memory/Home.md)
* [History](./memory/History.md)
* [Installation](./memory/Installation.md)
* [Getting started](./memory/Getting-started.md)
* [User documentation](./memory/User-documentation.md)
* [Developer documentation](./memory/Developer-documentation.md)
* [FAQ](./memory/FAQs.md)
* [Footer](./memory/_Footer.md)


## docs.mindforger.com

The https://docs.mindforger.com website is generated from `memory/` by the
build in `build/`:

```bash
cd build

make               # show all targets
make doc           # generate the website to distro/docs.mindforger.com
make doc-live      # generate and preview at http://localhost:8080
make doc-check     # check the generated site for broken links and images
make doc-clean     # delete the generated site
make doc-assets    # re-download the vendored Tabler and Lato assets
```

`make doc` renders Tabler styled HTML pages, copies the images and the assets,
and writes `sitemap.xml` and `robots.txt`. The result in
`distro/docs.mindforger.com/` (git ignored, purged on every build) is what is
uploaded to the web hosting.

* `build/sitemap.md` defines the site structure - the `Home`,
  `User Documentation` and `Technical Documentation` menus.
* `build/assets/` holds the vendored 3rd party assets (Tabler, Lato) and the
  MindForger branding - they are committed to this repository.
* `build/make/` holds the Python scripts used by the `Makefile`. They require
  the `markdown` and `pygments` Python packages.

`make doc-check` reports dead links of the Markdown sources as warnings - they
are broken in `memory/` and should be fixed there.


The content of this repository is processed as follows:

* `git:mindforger.wiki` is generated from 
  `git:mindforger-documentation/memory`
    - pages headers are removed (Wiki does NOT have them)
    - metadata are stripped using `mindforger --strip-meta FILE.md`
* `git:mindforger/README.md#Documentation` section is generated 
  from `git:mindforger-documentation/_Sidebar.md`
* `git:mindforger-repository/README.md#Documentation` section is
  generated from `git:mindforger-documentation/_Sidebar.md`
* `www.mindforger.com/index.html#Documentation` section is 
  generated from `git:mindforger-documentation/_Sidebar.md`

`git:mindforger.wiki` hosts **public** documentation and is linked from:

* MindForger application menu `Help/Documentation`
* MindForger application menu `Help/About MindForger` (Credits)
* MindForger preferences dialog `Spellcheck`
* `git:mindforger/README.md#Documentation`
* `git:mindforger-repository/README.md#Documentation`
* `www.mindforger.com/index.html#Documentation`

^ must be updated whenever this repository is changed.
