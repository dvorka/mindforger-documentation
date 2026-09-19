# MindForger Documentation Sitemap

This document defines the structure of the https://docs.mindforger.com website
which is generated from the Markdown notebooks in `memory/` - see `build/Makefile`.

Format:

* `## Section` ... top level menu (navbar dropdown)
* `### Item` ... menu item, `### ---` is a menu separator
* `* [source](Notebook.md)` ... Markdown source of the item in `memory/`
* `* [output](notebook.html)` ... optional output file name override
* `* [title](Page Title)` ... optional page title override

## Home

### Documentation
* [source](Home.md)
* [output](index.html)
* [title](MindForger Documentation)

### Project History
* [source](History.md)

### ---

### About
* [source](About.md)

## User Documentation

### Installation
* [source](Installation.md)

### Getting Started
* [source](Getting-started.md)

### User Documentation
* [source](User-documentation.md)

### ---

### FAQs
* [source](FAQs.md)

## Technical Documentation

### Developer Guide
* [source](Developer-documentation.md)
