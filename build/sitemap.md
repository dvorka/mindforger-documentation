# MindForger Documentation Sitemap

This document defines the structure of the https://www.mindforger.com/docs website
which is generated from the Markdown notebooks in `memory/` - see `build/Makefile`.

Format:

* `## Section` ... top level menu (navbar dropdown)
* `### Item` ... menu item, `### ---` is a menu separator
* `* [source](Notebook.md)` ... Markdown source of the item in `memory/`
* `* [url](https://...)` ... external link (opens in a new tab) instead of a page
* `* [output](notebook.html)` ... optional output file name override
* `* [title](Page Title)` ... optional page title override

## Home

### Documentation
* [source](HOME.md)
* [output](index.html)
* [title](MindForger Documentation)

### Table of Contents
* [source](TOC.md)

### Project History
* [source](HISTORY.md)

### Credits
* [source](CREDITS.md)

### ---

### About
* [source](ABOUT.md)

## User Documentation

### Comics
* [url](assets/comics/index.html)

### Installation
* [source](INSTALLATION.md)

### Getting Started
* [source](GETTING_STARTED.md)

### User Documentation
* [source](USER_DOCUMENTATION.md)

### ---

### FAQs
* [source](FAQS.md)

## Technical Documentation

### Developer Guide
* [source](DEVELOPER_DOCUMENTATION.md)

## News

### Blog
* [source](BLOG.md)

### Releases
* [source](RELEASES.md)

### Changelog
* [url](https://github.com/dvorka/mindforger/blob/master/Changelog)

### ---

### RSS
* [url](rss.xml)
