# Table of Contents <!-- Metadata: type: Outline; tags: mindforger-home; created: 2022-01-27 08:45:44; reads: 222; read: 2024-02-14 09:05:35; revision: 218; modified: 2024-02-14 09:05:35; importance: 0/5; urgency: 0/5; -->
<!-- Hint: links must NOT have .md extension as with .md is shown source of the page -->

<!-- wiki file -->
**Getting started**:

* [Basics](#basics)
    * [Workspace](Getting-started.md#workspace)
    * [Notebook](Getting-started.md#notebook)
    * [Note](Getting-started.md#note)
* [Create Workspace](Getting-started.md#create-workspace)
    * [Create Notebook](Getting-started.md#create-notebook)
        * [Create Note](Getting-started.md#create-note)
        * [Edit Note](Getting-started.md#edit-note)
        * [Fix Grammar with Wingman](Getting-started.md#fix-grammar-with-wingman)
* [Notes Outliner](Getting-started.md#notes-outliner)
* [Find Note](Getting-started.md#find-note)
* [Delete Notebook](Getting-started.md#delete-notebook)
* [Video tutorials](Getting-started.md#video-tutorials)
    * Video: [Getting started](https://www.youtube.com/watch?v=PlW2e1X3O-I)
    * Video: [First steps](https://www.youtube.com/watch?v=UR49y3uNurs)

<!-- wiki file -->
**About**:

* [Why MindForger?](About.md#why-mindforger)
    - [Unique](About.md#unique)
    - [Inspired by human mind](About.md#inspired-by-human-mind)
    - [Open, free and fast](About.md#open--free-and-fast)
* Presentations: 
    - Prezi: [Thinking notebook](https://prezi.com/view/pMJ7bmdpTYDBi7nMKFdU/)
* [History](History.md)
    - [RDF Spiders](History.md#rdf-spiders)
	- [MindRaider](History.md#mindraider)
	- [Coaching Notebook](History.md#coaching-notebook)
	- [MindForger](History.md#mindforger)
* [In the news](About.md#in-the-news)
* [Bugs and feature requests](About.md#bugs-and-feature-requests)
* [Community](About.md#community)

<!-- wiki file -->
**Installation**:

* [Install](Installation.md)
    - [macOS](Installation.md#macos)
    - [Windows](Installation.md#windows)
    - [Ubuntu](Installation.md#ubuntu)
    - [Debian](Installation.md#debian)
    - [Fedora](Installation.md#fedora)
    - [FreeBSD](Installation.md#freebsd)
    - [Arch Linux](Installation.md#arch-linux)
    - [NixOS](Installation.md#nixos)
    - [openSUSE](Installation.md#opensuse)
    - [WSL](Installation.md#wsl)
* [Configure](Installation.md#configure)
    - [Appearance and themes](Installation.md#appearance-and-themes)
    - [Custom HTML Preview CSS](Installation.md#custom-html-preview-css)
    - [Spell check](Installation.md#spell-check)
    - [Think vs. Sleep mode](Installation.md#think-vs--sleep-mode)
* [Releases](Installation.md#releases)
* [Changelog](Installation.md#changelog)
* [Nightly builds](Installation.md#nightly-builds)

<!-- wiki file -->
**User documentation**:

* Basics
    - Notebook
    - Note
    - Repository
* Notebook editor
    - New Notebook
    - Open existing Notebook
    - Edit Notebook and it's description
    - Deprecate Notebook and Limbo
* Markdown editor
    - From Markdown to MindForger
        - Markdown document
        - Document ~ Notebook
        - Section ~ Note
    - Open Markdown file
    - New Markdown file
    - Open directory with Markdowns
        - Example Markdown content
    - Markdown
        - Markdown cheat sheet and specification
        - `Format` menu
        - Images
        - Links
        - Math
        - Diagrams
        - Interesting documents and examples
    - Live preview
    - Outlining
    - Hoisting
    - Spellcheck
* Markdown IDE
    - Templates
    - Refactoring
    - Cloning
    - Link completion
* Search
    - Find . by .
    - Full text search (scope)
    - Recent
* Thinking notebook
    - MindForger repository
    - Metadata
        - Tags
        - Statistics (RW)
        - Deadlines
        - Progress
        - Types (thing)
    - Auto-linking
    - Think as you read
    - Think as you write
    - Associations
    - Scopes
        - Time-based scopes
        - Tag-based scopes
    - Knowledge graph navigator
    - Limbo
* Study tools
    - Kanban
    - Eisenhower matrix
* Coaching
    - GROW
* Integrations
    - Mobile phone (Git)
* Machine learning: NLP
    - CSV export
        - Tags OHE
* Tooling
    - Terminal
    - CLI
* Configuration
    - Appearance themes
        - Native with fixed fonts
        - ...
    - Fonts
    - Spellcheck (Win)
    - AA poller
* [Credits](User-documentation.md#credits)

<!-- wiki file -->
**Developer documentation**: 

* [Contribute](Developer-documentation.md#contribute)
* [Build](Installation.md#build-from-source-code)
    - [Build on macOS](Installation.md#build-on-macos)
    - [Build on Windows](Installation.md#build-on-windows)
    - [Build on Ubuntu](Installation.md#build-on-ubuntu)
    - [Build on Debian](Installation.md#build-on-debian)
    - [Build on Fedora](Installation.md#build-on-fedora)
    - [Build on Gentoo](Installation.md#build-on-gentoo)
    - [Build on NixOS](Installation.md#build-on-nixos)
    - [Build on WSL](Installation.md#build-on-wsl)
    - [Build and run Docker](Installation.md#docker)
* Development environment
    - [Linux development environment](Developer-documentation.md#linux-development-environment)
    - [Windows development environment](Developer-documentation.md#windows-development-environment)
    - macOS development environment
* Automation
    - Makefile and build/ directory
* [Continuous Integration (CI)](Developer-documentation.md#continuous-integration--ci)
    - [GitHub Actions](Developer-documentation.md#github-actions)
    - [AppVeyor](Developer-documentation.md#appveyor)
    - nightly builds: [.dmg](https://github.com/dvorka/mindforger/actions/workflows/build_macos.yml) | [Win installer](https://ci.appveyor.com/project/dvorka/mindforger) 
* Implementation
    - Incremental Markdown recursive descent parser
    - Magnets and rubbers: Force-directed Graph
    - [Model View Presenter front-end pattern](Developer-documentation.md#model-view-presenter)
    - NLP: stemmer, lexicon and bag of words
    - Repository layout specification
    - Outline document format specification (Markdown hosted DSL)
    - Localization
    - API reference (dOxygen generated documentation @ www.mindforger.com)
* Licensing
    - [MindForger license](https://github.com/dvorka/mindforger/blob/master/LICENSE)
    - [3rd party dependencies licenses](https://github.com/dvorka/mindforger/tree/master/licenses)
* Testing
    - Library unit tests
    - Frontend testing
* Packaging
    - Packaging flow and build environments (CI + VMs)
        - GitHub Actions (macOS Disk ImaGe, Linux tarball)
        - AppVeyor (Windows installer)
* Conventions and best practices
    - Branching conventions
    - Code format conventions
* [Security policy](https://github.com/dvorka/mindforger/blob/master/SECURITY.md)

<!-- wiki file -->
**Frequently Asked Questions**
* [FAQs](FAQs.md)
