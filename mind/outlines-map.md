# Notebooks Map <!-- Metadata: type: Outline; created: 2024-02-13 08:03:10; reads: 52; read: 2024-02-13 08:09:09; revision: 62; modified: 2024-02-13 08:15:47; importance: 0/5; urgency: 0/5; -->
# Table of Contents <!-- Metadata: type: Outline; tags: mindforger-home; links: [Outline key](/home/dvorka/p/mindforger/git/mindforger-documentation/memory/_Sidebar.md),[Outline path](_Sidebar.md); created: 2022-01-27 08:45:44; reads: 202; read: 2024-02-12 11:12:33; revision: 202; modified: 2024-02-12 11:12:33; -->
<!-- Hint: links must NOT have .md extension as with .md is shown source of the page -->

<!-- wiki file -->
**Getting started**:

* What is workspace, notebook and note?
* How to edit Markdown file?
* How to open directory with (many) Markdown files?
* How to open MindForger workspace?
* FAQs

<!-- wiki file -->
**About**:

* [Why MindForger?](GETTING_STARTED.md#why-mindforger)
    - [Unique](GETTING_STARTED.md#unique)
    - [Inspired by human mind](GETTING_STARTED.md#inspired-by-human-mind)
    - [Open, free and fast](GETTING_STARTED.md#open--free-and-fast)
* Presentations: 
    - Prezi: [Thinking notebook](https://prezi.com/view/pMJ7bmdpTYDBi7nMKFdU/)
* Tutorials
    - Video: [Getting started](https://www.youtube.com/watch?v=PlW2e1X3O-I)
    - Video: [First steps](https://www.youtube.com/watch?v=UR49y3uNurs)
* [History](HISTORY.md)
    - [RDF Spiders](HISTORY.md#rdf-spiders)
	- [MindRaider](HISTORY.md#mindraider)
	- [Coaching Notebook](HISTORY.md#coaching-notebook)
	- [MindForger](HISTORY.md#mindforger)
* [In the news](GETTING_STARTED.md#in-the-news)
* [Bugs and feature requests](GETTING_STARTED.md#bugs-and-feature-requests)
* [Community](GETTING_STARTED.md#community)

<!-- wiki file -->
**Installation**:

* [Install](INSTALLATION.md)
    - [macOS](INSTALLATION.md#macos)
    - [Windows](INSTALLATION.md#windows)
    - [Ubuntu](INSTALLATION.md#ubuntu)
    - [Debian](INSTALLATION.md#debian)
    - [Fedora](INSTALLATION.md#fedora)
    - [FreeBSD](INSTALLATION.md#freebsd)
    - [Arch Linux](INSTALLATION.md#arch-linux)
    - [NixOS](INSTALLATION.md#nixos)
    - [openSUSE](INSTALLATION.md#opensuse)
    - [WSL](INSTALLATION.md#wsl)
* [Configure](INSTALLATION.md#configure)
    - [Appearance and themes](INSTALLATION.md#appearance-and-themes)
    - [Custom HTML Preview CSS](INSTALLATION.md#custom-html-preview-css)
    - [Spell check](INSTALLATION.md#spell-check)
    - [Think vs. Sleep mode](INSTALLATION.md#think-vs--sleep-mode)
* [Releases](INSTALLATION.md#releases)
* [Changelog](INSTALLATION.md#changelog)
* [Nightly builds](INSTALLATION.md#nightly-builds)

<!-- wiki file -->
**User documentation**:

* Basics
    - Notebook
    - Note
    - Repository
* Notebook editor
    - New Notebok
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
* [Credits](USER_DOCUMENTATION.md#credits)

<!-- wiki file -->
**Developer documentation**: 

* [Contribute](DEVELOPER_DOCUMENTATION.md#contribute)
* [Build](INSTALLATION.md#build-from-source-code)
    - [Build on macOS](INSTALLATION.md#build-on-macos)
    - [Build on Windows](INSTALLATION.md#build-on-windows)
    - [Build on Ubuntu](INSTALLATION.md#build-on-ubuntu)
    - [Build on Debian](INSTALLATION.md#build-on-debian)
    - [Build on Fedora](INSTALLATION.md#build-on-fedora)
    - [Build on Gentoo](INSTALLATION.md#build-on-gentoo)
    - [Build on NixOS](INSTALLATION.md#build-on-nixos)
    - [Build on WSL](INSTALLATION.md#build-on-wsl)
    - [Build and run Docker](INSTALLATION.md#docker)
* Development environment
    - [Linux development environment](DEVELOPER_DOCUMENTATION.md#linux-development-environment)
    - [Windows development environment](DEVELOPER_DOCUMENTATION.md#windows-development-environment)
    - macOS development environment
* Automation
    - Makefile and build/ directory
* [Continuous Integration (CI)](DEVELOPER_DOCUMENTATION.md#continuous-integration--ci)
    - [GitHub Actions](DEVELOPER_DOCUMENTATION.md#github-actions)
    - [AppVeyor](DEVELOPER_DOCUMENTATION.md#appveyor)
    - nightly builds: [.dmg](https://github.com/dvorka/mindforger/actions/workflows/build_macos.yml) | [Win installer](https://ci.appveyor.com/project/dvorka/mindforger) 
* Implementation
    - Incremental Markdown recursive descent parser
    - Magnets and rubbers: Force-directed Graph
    - [Model View Presenter front-end pattern](DEVELOPER_DOCUMENTATION.md#model-view-presenter)
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
* [FAQs](FAQS.md)
## Home <!-- Metadata: type: Outline; links: [Outline key](/home/dvorka/p/mindforger/git/mindforger-documentation/memory/Home.md),[Outline path](HOME.md); created: 2022-01-12 09:45:45; reads: 133; read: 2024-02-12 11:14:46; revision: 124; modified: 2024-02-12 11:14:46; -->

## Getting Started <!-- Metadata: type: Outline; links: [Outline key](/home/dvorka/p/mindforger/git/mindforger-documentation/memory/Getting-started.md),[Outline path](GETTING_STARTED.md); created: 2022-01-26 23:41:16; reads: 90; read: 2024-02-13 08:10:54; revision: 86; modified: 2024-02-13 08:10:54; -->
Getting started with MindForger:

* [Why MindForger?](#why-mindforger)
    * [Unique](#unique)
    * [Inspired by human mind](#inspired-by-human-mind)
    * [Open, free and fast](#open--free-and-fast)
* [In the news](#in-the-news)
* [Bugs and feature requests](#bugs-and-feature-requests)
* [Community](#community)
## Installation <!-- Metadata: type: Outline; links: [Outline key](/home/dvorka/p/mindforger/git/mindforger-documentation/memory/Installation.md),[Outline path](INSTALLATION.md); created: 2018-03-20 16:19:07; reads: 1538; read: 2023-11-19 18:33:09; revision: 1533; modified: 2023-11-19 18:33:09; -->
Install:

* [macOS](#macos)
* [Windows](#windows)
* [Ubuntu](#ubuntu)
* [Debian](#debian)
* [Fedora](#fedora)
* [FreeBSD](#freebsd)
* [Arch Linux](#arch-linux)
* [NixOS](#nixos-)
* [openSUSE](#opensuse)
* [WSL](#wsl)

Build:

* [build on macOS](#build-on-macos)
* [build on Windows](#build-on-windows)
* [build on Ubuntu](#build-on-ubuntu)
* [build on Debian](#build-on-debian)
* [build on Fedora](#build-on-fedora)
* [build on Gentoo](#build-on-gentoo)
* [build on NixOS](#build-on-nixos)
* [build on WSL](#build-on-wsl)
* [build and run container](#build-and-run-in-container)

Configure:

* [Appearance and themes](#appearance-and-themes)
* [Custom HTML Preview CSS](#custom-html-preview-css)
* [Spell check](#spell-check)
* [Think vs. Sleep mode](#think-vs--sleep-mode)

Package for a new distribution or OS:

* [download tarball](https://github.com/dvorka/mindforger/releases)

Look up:

* [release](#releases)
* [change](#changelog)
## User documentation <!-- Metadata: type: Outline; tags: important,urgent,todo; links: [Outline key](/home/dvorka/p/mindforger/git/mindforger-documentation/memory/User-documentation.md),[Outline path](USER_DOCUMENTATION.md); created: 2022-02-26 08:27:46; reads: 158; read: 2024-02-13 08:14:00; revision: 155; modified: 2024-02-13 08:14:00; -->
Table of contents:

* [Basics](#basics)
    * [Notebook](#notebook)
    * [Note](#note)
    * [Repository](#repository)
* [Notebook editor](#notebook-editor)
    * [Open Notebook file](#open-notebook-file)
    * [Outliner](#outliner)
        * [Promote note](#promote-note)
        * [Demote note](#demote-note)
        * [Top](#top)
        * [Up](#up)
        * [Down](#down)
        * [Move note to bottom](#move-note-to-bottom)
        * [Hoisting](#hoisting)
    * [Live Preview](#live-preview)
        * [Live preview](#live-preview)
        * [View and Edit mode](#view-and-edit-mode)
* [Markdown editor](#markdown-editor)
    * [Markdown markup](#markdown-markup)
        * [Markdown specification](#markdown-specification)
        * [Markdown document](#markdown-document)
    * [Markdown mapping](#markdown-mapping)
        * [Document ~ Notebook](#document---notebook)
        * [Section ~ Note](#section---note)
    * [Markdown file](#markdown-file)
        * [Open Markdown file](#open-markdown-file)
    * [Outline](#outline)
        * [Markdown outline](#markdown-outline)
    * [Editor](#editor)
        * [Markdown format](#markdown-format)
            * [Text](#text)
            * [Keyboard keys](#keyboard-keys)
            * [Images](#images)
            * [Links](#links)
            * [Smarty pants](#smarty-pants)
            * [HR](#hr)
            * [List](#list)
            * [Tasks](#tasks)
            * [Blockquote](#blockquote)
            * [Tables](#tables)
            * [Source code with syntax highlighting](#source-code-with-syntax-highlighting)
            * [Math](#math)
                * [MathJax](#mathjax)
            * [Diagrams](#diagrams)
            * [Comments](#comments)
        * [Drag & Drop Images and Files](#drag---drop-images-and-files)
            * [DnD: Drag & Drop](#dnd--drag---drop)
        * [ToC generator](#toc-generator)
        * [Link completion](#link-completion)
* [Markdown IDE](#markdown-ide)
    * [Open Markdown directory](#open-markdown-directory)
        * [Open directory with Markdowns](#open-directory-with-markdowns)
            * [Multiple documents](#multiple-documents)
    * [Stencils](#stencils)
    * [Refactoring](#refactoring)
        * [Note refactoring](#note-refactoring)
    * [Home notebook](#home-notebook)
* [Search](#search)
    * [Fulltext](#fulltext)
    * [Name](#name)
    * [Tag](#tag)
* [Thinking Notebook](#thinking-notebook)
    * [Learning](#learning)
        * [MindForger repository](#mindforger-repository)
    * [Metadata](#metadata)
        * [Tags](#tags)
        * [Read/write statistics](#read-write-statistics)
        * [Progress](#progress)
        * [Deadlines](#deadlines)
        * [Things and types](#things-and-types)
        * [Relationships](#relationships)
    * [Auto-linking](#auto-linking)
    * [TaYR: Think as you Read](#tayr--think-as-you-read)
    * [TaYW: Think as you Write](#tayw--think-as-you-write)
    * [TaYS: Think as you Search](#tays--think-as-you-search)
    * [TaYB: Think as you Browse](#tayb--think-as-you-browse)
        * [Knowledge graph navigator](#knowledge-graph-navigator)
    * [Scopes](#scopes)
        * [Time Scope](#time-scope)
        * [Tag Scope](#tag-scope)
    * [Recognize what matters](#recognize-what-matters)
        * [Named-entity recognition](#named-entity-recognition)
        * [Semantic search and domains](#semantic-search-and-domains)
    * [Forgetting](#forgetting)
        * [Limbo](#limbo)
* [Productivity](#productivity)
    * [Urgency and Importance](#urgency-and-importance)
        * [Eisenhower matrix](#eisenhower-matrix)
    * [Tag-based aspects](#tag-based-aspects)
        * [Eisenhower matrix on tags](#eisenhower-matrix-on-tags)
        * [Kanban on Tags](#kanban-on-tags)
* [Machine learning: NLP](#machine-learning--nlp)
    * [CSV export](#csv-export)
* [Coaching](#coaching)
    * [GROW model](#grow-model)
    * [SMARTER goals](#smarter-goals)
* [Tools](#tools)
    * [Terminal](#terminal)
    * [CLI](#cli)
* [Cheatsheets](#cheatsheets)
    * [Markdown cheatsheet](#markdown-cheatsheet)
    * [MathJax cheatsheet](#mathjax-cheatsheet)
* [Keyboard shortcuts](#keyboard-shortcuts)
* [Command line and man](#command-line-and-man)
* [Content library](#content-library)
* [Credits](#credits)

This document _briefly_ describes key MindForger features.
## Developer documentation <!-- Metadata: type: Outline; links: [Outline key](/home/dvorka/p/mindforger/git/mindforger-documentation/memory/Developer-documentation.md),[Outline path](DEVELOPER_DOCUMENTATION.md); created: 2022-01-30 18:02:38; reads: 321; read: 2022-08-27 07:45:38; revision: 321; modified: 2022-08-27 07:45:38; -->
> _"There are only two kinds of languages: the ones people complain about and the ones nobody uses" -- [Bjarne Stroustrup](https://www.stroustrup.com/quotes.html)_

MindForger is written in **C++** programming language.

Contribute:

* [Source code](https://github.com/dvorka/mindforger)
* [Build](#development-environment)
* [Technical architecture](#technical-architecture)

Specifications:

* [Repository Structure](#repository-layout)
* [Outline Format - Markdown hosted DSL](#markdown-hosted-dsl)

In case that you have any question or want to learn more about technical details 
please don't hesitate to contact [me](mailto:martin.dvorak@mindforger.com).

## FAQs <!-- Metadata: type: Outline; links: [Outline key](/home/dvorka/p/mindforger/git/mindforger-documentation/memory/FAQs.md),[Outline path](FAQS.md); created: 2022-02-26 08:27:46; reads: 42; read: 2022-08-27 07:56:04; revision: 41; modified: 2022-08-27 07:56:04; -->
<!-- find all GitHub issues with "question" label (even closed) and turn them to questions in this Notebook -->

Frequently asked questions:


* [How can I open notebook title section?](#how-can-i-open-notebook-title-section) <kbd>todo</kbd>
* [How can I quickly edit viewed note?](#how-can-i-quickly-edit-viewed-note) <kbd>todo</kbd> <kbd>macos</kbd>
* [How can I stop Note HTML preview "bouncing" while editing its text?](#how-can-i-stop-note-html-preview--bouncing--while-editing-its-text)
* [How can I open Markdown file in MindForger?](#how-can-i-open-markdown-file-in-mindforger)
* [How can I delete tag?](#how-can-i-delete-tag)
* [Why is not line starting with # turned into section when editing a note?](#why-is-not-line-starting-with---turned-into-section-when-editing-a-note)
* [How can I change font size/color/... in HTML preview?](#how-can-i-change-font-size-color-----in-html-preview)
* [How can I manually add Markdown files to MindForger repository?](#how-can-i-manually-add-markdown-files-to-mindforger-repository)
## About <!-- Metadata: type: Outline; links: [Outline key](/home/dvorka/p/mindforger/git/mindforger-documentation/memory/About.md),[Outline path](ABOUT.md); created: 2022-01-26 23:41:16; reads: 90; read: 2024-02-13 08:07:31; revision: 87; modified: 2024-02-13 08:15:36; -->
Getting started with MindForger:

* [Why MindForger?](#why-mindforger)
    * [Unique](#unique)
    * [Inspired by human mind](#inspired-by-human-mind)
    * [Open, free and fast](#open--free-and-fast)
* [In the news](#in-the-news)
* [Bugs and feature requests](#bugs-and-feature-requests)
* [Community](#community)
## History <!-- Metadata: type: Outline; links: [Outline key](/home/dvorka/p/mindforger/git/mindforger-documentation/memory/History.md),[Outline path](HISTORY.md); created: 2022-01-26 23:42:26; reads: 364; read: 2022-03-10 08:34:42; revision: 363; modified: 2022-03-10 08:34:42; -->
The story of the human mind inspired outliner is also an important
chapter in the story of my life.

It's the year 1996. It's early in the morning. I sit on a sofa and wait
for a college exercise to begin. Thinking about an interesting topic 
and a piece of software to implement. How can I use what I learned in 
recent two years at the college? It should be exciting, it should be 
something from my domain, it must be something I will be using every 
day... as a student.

A strange pale guy is limping through the corridor and sits
next to me. I have never seen him before and cannot remind him from any
past lecture. He stares at me through thick glasses and we start to talk about 
this and that, about what exciting we have seen recently, getting to the 
topics of our interest and finding that we actually have a lot in common...
and interest in the human mind in particular. We talk about old school
AI, and about an obvious gap in contemporary Office suites. We skip
the lecture and keep talking about the exciting ideas in a guild clubhouse.
We say goodbye excited, inspired and passionate. I don't remember his name,
but I remember that day until today very well. This was the last time
we met.

It's the year 1998. I'm waiting in from of a session room for an
old professor whose lectures I will be attending in the following 4 semesters
to come. He excels in mathematical analysis, received the highest academic awards,
then he got fascinated by the human mind, gave up mathematics, turned into a rebel
and started to study his own mind and also the mind of his 4 years old grandson. 
Discussing various aspects of the human mind, cell model, neural networks
four hours every week for two years. He is skeptical, he often enters the
room smiling aloud while having Nature magazine in his hand - making fun 
of an experiment of US scientists who sliced the brain of a poor prisoner who was
sentenced to death and trying to understand how the mind works. He compares
it to the experiments with his grandson, self-observation, emotions analysis
and primitive reflex backgrounds.

It's the year 2003. I'm joining my colleagues at work and we make a big Amazon
order to make it cheaper. I order [Pinker](https://stevenpinker.com/)'s 
[How the Mind Work](https://en.wikipedia.org/wiki/How_the_Mind_Works) and 
Gärdenfors's [Conceptual Spaces: The Geometry of Thought](https://mitpress.mit.edu/books/conceptual-spaces). 
Great books, but this is not what I'm looking for...

It's the year 2004. I'm excited by the semantics web. Reading all available
literature, articles (including the one in
[Scientific American](https://www.scientificamerican.com/article/the-semantic-web/)
and web pages written by Tim Berners-Lee, going deep 
into RDF, ontologies and DARPA-funded technologies and specs. Reminding 
my college encounter thinking about putting the technology and ideas together.

I'm googling, [putting together various libraries](#rdf-spiders),
learning about force-directed graphs, coding overnight and
in early mornings while my girlfriend sleeps next to me. Happy days.

It's the year 2005. I just released [MindRaider](#mindraider) with buzzwordish pitch
"semantic web outliner" on SourceForge. My first open-source project. 
I have a good feeling of being able to do something myself without any help.
I don't expect any response - the project is fresh meat, unstable,
with no documentation and UI that nobody (except the author ~ me) can 
understand. I'm afraid that someone will be using it... but 
at the same time I'm curious. I got a splash of emails - getting 10s of 
emails in 2 weeks after the release. People from around 
the world - including postgraduates and researchers - are writing about 
MindRaider, asking questions, want to understand it, integrate and cooperate.

It's the year 2006 and I just gave a speech to a small audience at a university
about the project. More feedback, more interest in the project, more ideas
on how to extend it. Two months later my older son is born and my life 
priorities are changed.

The project lives its own life. I use it on an everyday basis as a normal
end user. It's reviewed on various servers, there is an article on Lifehacker
and the project gets 10k downloads in one day, I'm getting emails from students
to whom MindRaider 'saved their ...' (you know what) when they needed to 
prepare for a tough exam, from software and marketing companies that 
use it to deliver projects. I'm getting emails from interesting verticals
like automotive and even NASA employees.

It's the year 2010. I just bought Kindle, 3rd generation. I spent my first
money on books on memo athletics. I also download a few
cognitive psychology articles by coincidence. This is it! This is what 
I discussed years ago with the pale student, this is what human mind 
addicted professor has been researching. I enjoy reading formal 
definitions of concepts I discovered myself and planned to 
incorporate into my projects.

It's 2011 and MindRaider on Google App Engine PaaS (which was just born)
is evaluated by the first invited users - it's [Coaching Notebook](#coaching-notebook) SaaS
and it goes much further. It's auto-coaching tool atop abstractions,
I verified in the past, which is trying to help in making
life more balanced and happier. But life cannot be planned...

...it's the year 2013. I'm lying and shaking on the bed<!-- within opened pavilion
of psychiatric sanatorium -->. Anxiety, depression and nightmares. Scared and
unable to sleep for a few weeks. Having personal problems and 
taking my work way too much seriously.

It's the year 2014 and I believe that this is a new beginning. I just opened 
a text editor and started to write a book on the human mind,
memory, intelligence, knowledge, memo athletics, remembering,
forgetting, subliminal learning, organized super-organisms and
information waves ... which is shaping the vision of thinking notebook.

It's 2017 and I just decided to leave my full-time job - inspired
by [talk which Andy Weir gave at LLNL](https://www.youtube.com/watch?v=2tfh6OUUYUw) - to 
enjoy my very own and self-sponsored sabbatical whose ultimate goal is to 
research and prototype my new project - MindForger.

[Donald Knuth](https://cs.wikipedia.org/wiki/Donald_Ervin_Knuth)
implemented [TeX](https://en.wikipedia.org/wiki/TeX) because he was 
not satisfied with existing typesetting systems and he wanted to write
beautiful research articles and books. 
[Linux Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) 
implemented [Git](https://en.wikipedia.org/wiki/Git) because he was
not satisfied with existing version-control systems and he wanted to
efficiently maintain Linux kernel source code. I admire both of these men. 
Both of them stopped the work and implemented a tool which they were
desperately missing. Then they returned back to do what they know best.
My motivation is exactly the same.

Forger part of the [MindForger](https://www.mindforger.com) project name
is inspired by _forger_ character
from [Inception (2018)](https://www.imdb.com/title/tt1375666/fullcredits)
movie by Christopher Nolan (Tom Hardy as dream property forger). This is
also why the first release screenshot and the web page will be based on Eddie
character from [Venom](https://www.imdb.com/title/tt1270797/) movie 
(Tom Hardy w/ symbiont).

![42nd birthday](HISTORY.42nd-birthday.jpg)

It's my [42nd](https://en.wikipedia.org/wiki/42_(number)#The_Hitchhiker's_Guide_to_the_Galaxy) 
birthday and I just announced the first public release - `MindForger 0.42.0` - to
confirm [answer](https://www.youtube.com/watch?v=aboZctrHfK8) to 
the Ultimate Question of life, the Universe, and Everything. 
Sabbatical mission accomplished, but I believe that this is just 
a beginning - _Adventure is out there!_
# Footer <!-- Metadata: type: Outline; links: [Outline key](/home/dvorka/p/mindforger/git/mindforger-documentation/memory/_Footer.md),[Outline path](_Footer.md); created: 2022-01-30 15:59:38; reads: 19; read: 2024-02-12 11:12:54; revision: 19; modified: 2024-02-12 11:12:54; -->
<!-- CREDITS link is broken by removal of .md extension - find a way how to protect it (possibly in the conversion script) -->

Created with passion for my personal pleasure.
<br/>
Released on the day of my [42nd](https://en.wikipedia.org/wiki/42_(number)#The_Hitchhiker's_Guide_to_the_Galaxy) birthday to confirm [answer](https://www.youtube.com/watch?v=aboZctrHfK8) to the Ultimate Question of life, the Universe, and Everything.
<br/>
[Martin.Dvorak@mindforger.com](http://me.mindforger.com) and [contributors](https://github.com/dvorka/mindforger/blob/master/CREDITS.md)
<br/>
2018-2024
