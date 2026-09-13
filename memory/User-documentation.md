# User documentation <!-- Metadata: type: Outline; created: 2022-02-26 08:27:46; reads: 847; read: 2026-09-13 15:58:05; revision: 847; modified: 2026-09-13 15:58:05; importance: 0/5; urgency: 0/5; -->
Table of contents:

* [Basics](#basics)
* [Knowledge manager](#knowledge-manager)
    * [Create Notebook](#create-notebook)
        * [Create Note](#create-note)
        * [Edit Note](#edit-note)
    * [Open Notebook](#open-notebook)
    * [Outliner](#outliner)
        * [Promote note](#promote-note)
        * [Demote note](#demote-note)
        * [Move to first](#move-to-first)
        * [Up](#up)
        * [Down](#down)
        * [Move to last](#move-to-last)
    * [Live Preview](#live-preview)
        * [View and Edit mode](#view-and-edit-mode)
* [Wingman](#wingman)
    * [Wingman LLM provider configuration](#wingman-llm-provider-configuration)
    * [Fix grammar](#fix-grammar)
    * [Translate](#translate)
    * [Rewrite](#rewrite)
    * [Complete text](#complete-text)
    * [ELI5: Explain like I'm 5](#eli5--explain-like-i-m-5)
* [Markdown editor](#markdown-editor)
    * [Open Markdown file](#open-markdown-file)
    * [Markdown markup](#markdown-markup)
    * [Markdown mapping](#markdown-mapping)
        * [Document ~ Notebook](#document---notebook)
        * [Section ~ Note](#section---note)
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
    * [Table of contents generator](#table-of-contents-generator)
    * [Link completion](#link-completion)
* [Markdown IDE](#markdown-ide)
    * [Open Markdown directory](#open-markdown-directory)
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
    * [TaYB: Think as you Browse](#tayb--think-as-you-browse)
    * [TaYS: Think as you Search](#tays--think-as-you-search)
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
    * [Organizers: tag-based aspects](#organizers--tag-based-aspects)
        * [Eisenhower matrix on tags](#eisenhower-matrix-on-tags)
        * [Kanban on Tags](#kanban-on-tags)
* [Machine learning: NLP](#machine-learning--nlp)
    * [CSV export](#csv-export)
* [Coaching](#coaching)
    * [GROW model](#grow-model)
    * [SMARTER goals](#smarter-goals)
* [Tools](#tools)
    * [CLI](#cli)
* [Cheatsheets](#cheatsheets)
    * [Markdown cheatsheet](#markdown-cheatsheet)
    * [MathJax cheatsheet](#mathjax-cheatsheet)
* [Keyboard shortcuts](#keyboard-shortcuts)
    * [Linux keyboard shortcuts](#linux-keyboard-shortcuts)
    * [macOS keyboard shortcuts](#macos-keyboard-shortcuts)
    * [Windows keyboard shortcuts](#windows-keyboard-shortcuts)
* [Command line and man](#command-line-and-man)
* [Library](#library)
* [Credits](#credits)
  
This document _briefly_ describes key MindForger features.


# Basics <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 56; read: 2024-02-16 16:17:01; revision: 7; modified: 2024-02-13 08:16:32; -->
![desktop](user-documentation.basic-concepts-overview.png)

MindForger uses the following terminology:

* [Workspace](Getting-started.md#workspace)
* [Notebook](Getting-started.md#notebook)
* [Note](Getting-started.md#note)

In short:

* The MindForger [workspace](Getting-started.md#workspace) is analogous **the desktop** of an office desk.
    * The MindForger [notebook](Getting-started.md#notebook) analogous to **a notepad** on the desktop.
        * A MindForger [note](Getting-started.md#note) is analogous to **a page with the note** from a **notepad**.

For more details see [Basics](Getting-started.md#basics) section in the [Getting Started](Getting-started.md) guide.


# Knowledge manager <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 114; read: 2024-02-16 16:17:02; revision: 10; modified: 2024-02-16 15:10:37; -->
MindForger is **knowledge management tool** which means it is a software that helps you to organize, store, and access their knowledge effectively. With MindForger, you can create and maintain a [workspace](Getting-started.md#workspace) of your thoughts, ideas, notes, and any other kind of information they want to store.

MindForger provides a range of **features** to assist in knowledge management. Youa can create [hierarchical outlines](#outliner), [mind maps](#knowledge-graph-navigator), and [tags](#tags) to categorize and structure your knowledge. You can also create [links](#auto-linking) between different pieces of information ([notes](Getting-started.md#note)), allowing for easy navigation and connections between related concepts.

In addition to organizing information, MindForger also includes powerful [search functionality](Getting-started.md#find-note). This allows you to quickly locate specific pieces of information within your knowledge workspace. Whether you are searching for a keyword, a specific note, or a particular tag, MindForger helps you to find what you need efficiently.

Overall, MindForger assists you in **organizing**, **accessing**, and **maximizing** the value of your **knowledge**, ultimately promoting **productivity** and **innovation**.


## Create Notebook <!-- Metadata: type: Note; created: 2024-02-13 07:57:40; reads: 48; read: 2024-02-16 16:17:02; revision: 5; modified: 2024-02-16 14:53:45; -->
Create **new** [notebook](#notebook) as follows:

1. open menu `Notebook`
    - 💡 if `Notebook` menu is disabled, 
      then open list of notebooks (menu `View` / `Notebooks`) or notebooks tree
      (menu `View` / `Notebooks Tree`)
1. choose `New` menu item
1. `New Notebook` dialog is opened:
   - type in notebook name 
   - feel free modify notebook creation options and tags
1. click <kbd>OK</kbd> to create the notebook


### Create Note <!-- Metadata: type: Note; created: 2024-02-13 07:57:43; reads: 34; read: 2024-02-16 16:17:02; revision: 2; modified: 2024-02-16 14:12:17; -->
Create **new** [note](#note) as follows:

1. open menu `Note`
    - 💡 if `Note` menu might is disabled, 
      then open the [notebook](#notebook) in which you want to add the note
1. choose `New` menu item
1. `New Note` dialog is opened:
   - type in note name 
   - feel free modify note creation options and tags
1. click <kbd>OK</kbd> to create the note


### Edit Note <!-- Metadata: type: Note; created: 2024-02-13 08:19:27; reads: 36; read: 2024-02-16 16:17:02; revision: 2; modified: 2024-02-16 14:12:17; -->
When you are viewing a [note](#note), you can edit it using one of the options below:

* **Double click** the mouse preview.
* Use <kbd>Ctrl-e</kbd> keyboard shortcut (Linux/Win).
* Use <kbd>Alt-n e</kbd> keyboard shortcut (Linux/Win).

Once you finish editing the [note](#note) you can save it and preview using one of the options below:

* Use <kbd>Alt-⬅</kbd> keyboard shortcut.
* Click <kbd>Save & Leave</kbd> button at the bottom of the editor.


## Open Notebook <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 91; read: 2024-02-16 16:17:02; revision: 15; modified: 2024-02-16 14:57:20; -->
**Open** [notebook](#notebook) as follows:

1. open list of notebooks (menu `View` / `Notebooks`)
   or notebooks tree (menu `View` / `Notebooks Tree`)
1. choose the notebook you want to open
1. open the notebook using one of the following options:
    * hit <kbd>Enter</kbd> key
    * double-click the notebook row in the list/tree
    

## Outliner <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 83; read: 2024-02-16 16:17:02; revision: 6; modified: 2024-02-16 15:16:13; -->
[![v](https://img.youtube.com/vi/LUqavHfKhnc/0.jpg)](https://www.youtube.com/watch?v=LUqavHfKhnc)

<!-- add section on outliners history - emphasize that that historical text is not mandatory -->

An **outliner** is a feature used in word processing, **note-taking**, and organizational software to help users outline and structure their ideas. Outlining actions in MindForger allow users to create **hierarchies** or levels of information by, making it easier to organize and navigate through a [Notebook](#notebook):

1. open a [notebook](#notebook)
1. choose and view a [note](#note) in the note tree
1. open menu `Note`
1. choose one of the **outlining actions**
    - `Promote`
        - to move note one level **up** in hierarchy (depth)
    - `Demote`
        - to move note one level **down** in hierarchy (depth)
    - `Move to first`
        - move note to **the first** from the top on its level (depth)
    - `Move up`
        - move note one position **up** on its level (depth)
    - `Move down`
        - move note one position **down** on its level (depth)
    - `Move to last`
        - move note to **the last** from the top on its level (depth)

Outlining is a powerful tool that allows you to organize your thoughts and make your remarks structured, comprehensible, and scalable.


### Promote note <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 59; read: 2024-02-16 16:17:03; revision: 4; modified: 2024-02-16 14:59:10; -->
**Promote** note as follows:

1. open a [notebook](#notebook)
1. choose and view a [note](#note) in the note tree
1. open menu `Note`
1. choose one of the **outlining actions**
    - `Promote`
        - to move note one level **up** in hierarchy (depth)


### Demote note <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 57; read: 2024-02-16 16:17:03; revision: 3; modified: 2024-02-16 14:59:16; -->
**Promote** note as follows:

1. open a [notebook](#notebook)
1. choose and view a [note](#note) in the note tree
1. open menu `Note`
1. choose one of the **outlining actions**
    - `Demote`
        - to move note one level **down** in hierarchy (depth)


### Move to first <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 62; read: 2024-02-16 16:17:03; revision: 5; modified: 2024-02-16 14:59:25; -->
**Promote** note as follows:

1. open a [notebook](#notebook)
1. choose and view a [note](#note) in the note tree
1. open menu `Note`
1. choose one of the **outlining actions**
    - `Move to first`
        - move note to **the first** from the top on its level (depth)


### Up <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 63; read: 2024-02-16 16:17:03; revision: 4; modified: 2024-02-16 14:59:35; -->
**Promote** note as follows:

1. open a [notebook](#notebook)
1. choose and view a [note](#note) in the note tree
1. open menu `Note`
1. choose one of the **outlining actions**
    - `Move up`
        - move note one position **up** on its level (depth)


### Down <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 61; read: 2024-02-16 16:17:03; revision: 4; modified: 2024-02-16 14:59:43; -->
**Promote** note as follows:

1. open a [notebook](#notebook)
1. choose and view a [note](#note) in the note tree
1. open menu `Note`
1. choose one of the **outlining actions**
    - `Move down`
        - move note one position **down** on its level (depth)


### Move to last <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 56; read: 2024-02-16 16:17:03; revision: 4; modified: 2024-02-16 14:59:48; -->
**Promote** note as follows:

1. open a [notebook](#notebook)
1. choose and view a [note](#note) in the note tree
1. open menu `Note`
1. choose one of the **outlining actions**
    - `Move to last`
        - move note to **the last** from the top on its level (depth)


## Live Preview <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 67; read: 2024-02-16 16:17:03; revision: 5; modified: 2024-02-16 15:16:32; -->
[![v](https://img.youtube.com/vi/vRDZSAHkk9Y/0.jpg)](https://www.youtube.com/watch?v=vRDZSAHkk9Y)

Easily toggle live HTML preview of edited Markdown with shortcut or edit panel buttons.


### View and Edit mode <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 56; read: 2024-02-16 16:17:15; revision: 3; modified: 2024-02-10 23:28:19; -->
<!-- new screnshot w/ overlay comments -->

![Image](user-documentation.click-to-edit.png)

If you want to **edit** a section either **double-click** anywhere in the 
rendered preview on the right (MindForger window) or choose:

*  menu `Notebook/Edit` for title section
*  menu `Note/Edit` for any sub-section
# Wingman <!-- Metadata: type: Note; created: 2024-02-13 11:34:18; reads: 64; read: 2024-02-16 16:17:15; revision: 28; modified: 2024-02-16 15:31:17; -->
[![v](https://img.youtube.com/vi/eyLV5P_Bujs/0.jpg)](https://www.youtube.com/watch?v=eyLV5P_Bujs)

Wingman is a [large language model](https://en.wikipedia.org/wiki/Large_language_model) (LLM) based MindForger's tool which brings note-taking and knowledge management to a new level. With the wingman you can easily expand your notes and knowledge by leveraging the power of artificial intelligence. Whether you need to write an **in-depth analysis**, draft a **blog post**, prepare a **plan**, or simply **generate ideas**. Wingman can also:

* summarize
* [explain](#eli5--explain-like-i-m-5)
* [translate](#translate)
* [generate](#rewrite)
* [fix grammar](#fix-grammar)
* [reformulate](#rewrite)

... and much more.


## Wingman LLM provider configuration <!-- Metadata: type: Note; created: 2024-02-13 11:34:29; reads: 107; read: 2024-02-16 16:17:15; revision: 68; modified: 2024-02-14 21:23:11; -->
Wingman tool uses OpenAI as LLM provider. Therefore the first step is to **generate API key** which will be used by Wingman:

1. open https://platform.openai.com/api-keys
1. click <kbd>+ Create new secret key</kbd> to **generate** new API key
   ![i](wingman-openai-gen-key.png)
1. save the key e.g. in your password manager

There are **two** options how to **configure** OpenAI API key in MindForger:

**Option A (safer)** - configure shell environment variable:

1. add API key to your shell configuration:
    * Linux:
        * Bash:
            * Add the following line into your `/home/${USER}/.bashrc`:
                * `export MINDFORGER_OPENAI_API_KEY="...your API key..."`
        * Zsh:
            * Add the following line into your `/home/${USER}/.zshrc`:
                * `export MINDFORGER_OPENAI_API_KEY="...your API key..."`
1. start new shell
1. run MindForger
    
**Option B** - set the API key in the MindForger configuration dialog:

1. open menu `Workspace`
1. choose `Preferences` menu item
1. select `Wingman` tab in the configuration dialog
1. paste API key to the edit line in the dialog:
   ![i](wingman-config-1.png)
1. click <kbd>OK</kbd> to save **unencrypted** API key to `.mindforger.md` in your home directory
1. restart MindForger
1. open `Preferences` dialog to check that OpenAI is selected as the LLM Provider for Wingman
   ![i](wingman-openai-done.png)


## Fix grammar <!-- Metadata: type: Note; created: 2024-02-13 11:34:51; reads: 57; read: 2024-02-16 16:17:14; revision: 6; modified: 2024-02-16 13:52:16; -->
[![v](https://img.youtube.com/vi/QLX9CWzzEa8/0.jpg)](https://www.youtube.com/watch?v=QLX9CWzzEa8)


## Translate <!-- Metadata: type: Note; created: 2024-02-14 21:23:34; reads: 43; read: 2024-02-16 16:17:14; revision: 8; modified: 2024-02-16 13:46:41; -->
[![v](https://img.youtube.com/vi/akesdLhWZ-I/0.jpg)](https://www.youtube.com/watch?v=akesdLhWZ-I)

Otto Wichterle byl světově proslulý český vědec a vynálezce, pracující zejména v oblasti makromolekulární organické chemie, mezi jejíž zakladatele patřil. Proslulý je především svými objevy a vynálezy, které vedly k zásadnímu zdokonalení a celosvětovému rozšíření měkkých kontaktních čoček. Tyto výsledky vycházely z jeho původní vědecké práce v oblasti hydrogelů. Wichterle se proslavil též objevem umělého polyamidového vlákna – silonu.


## Rewrite <!-- Metadata: type: Note; created: 2024-02-13 11:35:32; reads: 43; read: 2024-02-16 16:17:14; revision: 6; modified: 2024-02-16 13:47:33; -->
[![v](https://img.youtube.com/vi/eyLV5P_Bujs/0.jpg)](https://www.youtube.com/watch?v=eyLV5P_Bujs)


## Complete text <!-- Metadata: type: Note; created: 2024-02-13 11:35:36; reads: 40; read: 2024-02-16 16:17:13; revision: 5; modified: 2024-02-16 13:47:57; -->
[![v](https://img.youtube.com/vi/eyLV5P_Bujs/0.jpg)](https://www.youtube.com/watch?v=eyLV5P_Bujs)


## ELI5: Explain like I'm 5 <!-- Metadata: type: Note; created: 2024-02-13 11:36:24; reads: 36; read: 2024-02-16 16:17:13; revision: 4; modified: 2024-02-16 13:48:12; -->
[![v](https://img.youtube.com/vi/fln4XdnlR0A/0.jpg)](https://www.youtube.com/watch?v=fln4XdnlR0A)


# Markdown editor <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 41; read: 2024-02-16 16:17:12; revision: 1; modified: 2022-02-26 08:27:46; -->
MindForger can be used as a Markdown **editor**.

It allows you to easily write [Markdown](#markdown) 
documents in a WYSIWYG text editor with
Markdow **syntax** hints and an HTML rendered **preview**.

MindForger terminology:

* A Markdown file is a **Notebook**.
* A Markdown document section (line with leading `#`) is a **Note**.


MindForger represents any Markdown as [follows](#markdown-outline)...
## Open Markdown file <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 49; read: 2024-02-16 16:17:12; revision: 3; modified: 2024-02-16 15:22:45; -->
MindForger can be used to edit a **single** Markdown file:

```
$ mindforger analysis.md
```

If the given file exists, then it's opened for editing, otherwise a
new Markdown file with this name is **created** and opened.
## Markdown markup <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 48; read: 2024-02-16 16:17:12; revision: 2; modified: 2022-03-10 08:54:35; -->
<!-- ... Ink example with simplistic MD: title, 2 sections, funny -->

> **Markdown** is a lightweight markup language for creating formatted text using a plain-text editor. John Gruber and Aaron Swartz created Markdown in 2004 as a markup language that is appealing to human readers in its source code form.[9] Markdown is widely used in blogging, instant messaging, online forums, collaborative software, documentation pages, and readme 
files. -- [Wikipedia](https://en.wikipedia.org/wiki/Markdown)

You can write your remarks as **plain text** without any formatting in MindForger.

However, you **may** use [Markdown markup](https://daringfireball.net/projects/markdown/) to emphasize important parts of the text, make links, create lists, etc. MindForger will also use Markdown to store your remarks which enables you to use any Markdown editor or tool.

You don't have to learn [Markdown specification](https://spec.commonmark.org/) as MindForger editor and `Format` menu will help and guide you.
## Markdown mapping <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 50; read: 2024-02-16 16:17:12; revision: 2; modified: 2024-02-16 15:20:08; -->
In order to enable quick **navigation** and **refactoring** 
of Markdown documents, MindForger shows Markdown documents (**Notebooks**) 
as an **outline** of Markdown sections (**Notes**) allowing
you to efficiently choose/read/edit/refactor a particular section.

![Image](user-documentation.outliner-rules.png)

Check side-by-side Markdown document **text view**
and **MindForger view** in the image above:

* The `INSTALLATION` Markdown document is opened in a text editor (Emacs) on the **left**.
* The same Markdown document is opened in MindForger on the **right**.

As you can see, MindForger represents the hierarchy of sections 
(prefixed/underlined in Markdown syntax with/by `#`, `-` or `=`) 
as a **tree** - called an **outline**:

* The tree of sections (in the left MindForger window) reflects 
  the **depth/level** of individual sections e.g. section `UBUNTU` 
  on the second level is prefixed with `##` and shown on the second 
  level in the tree.

![Image](faq.title-section-edit.png)

* You can **open** Markdown document **title section** (`INSTALLATION`) by
  clicking its name `INSTALLATION` above **outline**.
* Any **sub-section** can be opened by clicking its name in the tree.

For switching between section (pre)view and edit mode refer to the [next section](#view-vs-edit-mode).


### Document ~ Notebook <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 49; read: 2024-02-16 16:17:11; revision: 4; modified: 2024-02-16 15:23:08; -->
**Markdown document** (file) is represented as [notebook](Getting-started.md#notebook) in MindForger.


### Section ~ Note <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 48; read: 2024-02-16 16:17:28; revision: 2; modified: 2024-02-16 15:21:32; -->
Markdown document **section** is represented as [note](Getting-started.md#note) in MindForger.


## Markdown format <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 38; read: 2024-02-16 16:17:29; revision: 3; modified: 2024-02-16 15:24:39; -->
[Markdown](https://daringfireball.net/projects/markdown/) is  a plain text formatting syntax introduced by John Gruber.
Markdown allows you to write using an easy-to-read, easy-to-write plain text 
format, easily rendered as HTML.

MindForger uses Markdown-based DSL.
There are many flavors of Markdown - for
Markdown syntax documentation please refer to:

* [John Gruber Markdown syntax](https://daringfireball.net/projects/markdown/syntax) documentation
* [GitHub Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/) documentation
* [GitHub flavored Markdown](https://github.github.com/gfm/) specification
* [Mermaid diagrams](https://mermaidjs.github.io/) documentation

Sub-sections of this section provide Markdown syntax
overview and rendering demonstration. As you read
particular Markdown syntax features, be sure to
open each section for **edit** (to check syntax) and
experiment with **menu** `Format/*`.
### Text <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 27; read: 2024-02-16 16:17:29; revision: 1; modified: 2022-02-26 08:27:46; -->
`Monospace` text, *emph* text, **bold** text, 
_italic_ text, __bold__ text, ~~deleted~~ text.

---

💡 edit this Note to see the syntax
### Keyboard keys <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 25; read: 2024-02-16 16:17:30; revision: 1; modified: 2022-02-26 08:27:46; -->
You can use <kbd>Alt+f b</kbd> to make marked text bold.

---

💡 edit this Note to see the syntax
### Images <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 23; read: 2024-02-16 16:17:31; revision: 1; modified: 2022-02-26 08:27:46; -->
See Markdown source of this Note to learn **image** syntax.

Image from web:

![MindForger logo](http://www.mindforger.com/images/mind-forger.png)

Image from current MindForger repository:

![MF screenshot](./mindforger.png)

---

💡 edit this Note to see the syntax <br/>
💡 click menu `Format/Image` or press <kbd>Alt+f m</kbd> to insert image.
### Links <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 23; read: 2024-02-16 16:17:32; revision: 1; modified: 2022-02-26 08:27:46; -->
See Markdown source of this Note to learn **link** syntax.

Link to web:

* [MindForger home page](http://www.mindforger.com)

Automatic web link:

* https://github.com/dvorka/mindforger

Link to a Notebook in active MindForger repository:

* [MF history](./history.md)

Link to a Note in active MindForger repository:

* [MF motivation](./why-mindforger.md#motivation)

Link to a file on the filesystem:

* [.bashrc](/etc/bash.bashrc)

Link to a directory on the filesystem:

* [/tmp](/tmp)

---

💡 edit this Note to see the syntax <br/>
💡 click menu `Format/Link` or press <kbd>Alt+f l</kbd> to insert link.
### Smarty pants <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 28; read: 2024-02-16 16:17:34; revision: 2; modified: 2024-02-16 13:51:20; -->

[Smarty pants like](https://daringfireball.net/projects/smartypants/) like:

* curly " and '
* ``backsticks''
* dashes a--ha and a---ha
* (tm) and (r) and (c)
* consecutive dots ...
* 1/4 1/2
* A^B and a^(b+2)

---

💡 edit this Note to see the syntax
### HR <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 29; read: 2024-02-16 16:17:35; revision: 1; modified: 2022-02-26 08:27:46; -->
Horizontal...

---
... rulers ...

***
... split screen horizontally.
___

### List <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 27; read: 2024-02-16 16:17:35; revision: 1; modified: 2022-02-26 08:27:46; -->
Bullet list:

* why
    * ?
- how
    * !
+ what
    * .

Numbered list:

1. why
    1. ?
2. how
    1. ?
3. what
    1. ?

---

💡 edit this Note to see the syntax
### Tasks <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 27; read: 2024-02-16 16:17:35; revision: 1; modified: 2022-02-26 08:27:46; -->
Task list:

* [x] skip-gram
    * [ ] bag of words
* [X] GloWe vs. word2vec
    * [ ] word embedding
* [x] stemmer

---

💡 edit this Note to see the syntax
### Blockquote <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 27; read: 2024-02-16 16:17:36; revision: 1; modified: 2022-02-26 08:27:46; -->
Riddle:

> frodo and
> glum,
>> riddles
>>> in the dark

---

💡 edit this Note to see the syntax
### Tables <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 31; read: 2024-02-16 16:17:38; revision: 5; modified: 2024-02-16 16:12:30; -->
Pets:

Snake | Turtle
 ----- | ------
Karkulka | Ema

Frontend | Backend
:----- | :------
Qt | C++

---

Columns can be **aligned** to left/right or centered:

Left | Center | Right
:----- | :------: | ------:
This is frontend | This is middle-ware | This is backend
Js | ESB | C++

---

💡 edit this Note to see the syntax
### Source code with syntax highlighting <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 29; read: 2024-02-16 16:17:38; revision: 1; modified: 2022-02-26 08:27:46; -->
There are multiple options how a block of source code can be written in Markdown.

**IMPORTANT**: note leading empty lines before code blocks.

---

1) Tab indentation w/o language spec and w/o syntax highlighting:

	public static void main(string[] args) {
    	return 0;
	}

---

2) Code block w/ language spec:

```
    ```java
    ```
```

```java
public static void main(string[] args) {
    return 0;
}
```

or w/o language spec:

```
public static void main(string[] args) {
    return 0;
}
```

---

3) Fenced block w/ language spec:

~~~java
public static void main(string[] args) {
    return 0;
}
~~~

or w/o language spec:

~~~
public static void main(string[] args) {
    return 0;
}
~~~

---

💡 edit this Note to see the syntax
### Math <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 43; read: 2026-09-13 15:49:47; revision: 6; modified: 2026-09-13 15:49:47; -->
![i](user-documentation.math.png)

[MathJax](https://www.mathjax.org/) handles **inline** expressions like: x^2 + y^2 = z^2 or **block** expressions like: $$\frac{D\rho}{Dt} = 0.$$


Check MathJax documentation and/or [cheatsheet](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference) for more examples.

Quadratic equation root: When \(a \ne 0\), there are two solutions to \(ax^2 + bx + c = 0\) and they are
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$

Sum:
$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$

Limit:
$$\lim_{x\to 0}$$

Sqrt:
$$\left(\frac{\sqrt x}{y^3}\right)$$

---

Alternatively you can use https://www.codecogs.com to render
expression to image and include it in Markdown.

---

💡 edit this Note to see the syntax <br/>
💡 if math expressions are **not** rendered, then you must **enable** MathJax using menu menu `Workspace/Preferences/Viewer/Math support`


#### MathJax <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 45; read: 2026-09-13 15:49:24; revision: 6; modified: 2026-09-13 15:33:04; -->
![i](user-documentation.mathjax.png)

MathJax [cheetsheet](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference):

* use `$` to inline expressions, and `$$` for blocks
* superscript: $x^2$
* subscript: $x_i$
* superscript and subscript: $x^2_i$
* Greek letters:
  $\alpha, \beta, \delta ... \omega, \Delta, ... \Omega$
* groups: for `10^10` you get $10^10$, but `10^{10}` gives $10^{10}$. 
* parenthesis: [, ( and use `\{` for curly braces
* fraction: $\frac{2}{3}$ $\frac{a+b}{c-d}$
* square: $\sqrt{10}$ $\sqrt[3]{\frac xy}$
* exponential: $2^8$
* absolute: $\vert{x}\vert$
* metric: $\Vert{x}\Vert$
* interval: $\langle x, y \rangle$
* sum: $\sum x_i$
* integral: $\int x_i$ $\iint x_i$ $\iiint x_i$
* union: $x \cup y$, $\bigcup x$
* intersection: $x \cap y$, $\bigcap x$
* limit: $\lim_{x\to 0}$
* goniometrical: $\sin x$
* bigger/smaller: $\lt \gt \le \leq \leqq \leqslant \ge \geq \geqq \geqslant$
* not using `n`: $\neq$
* sets: $\cup \cap \setminus \subset \subseteq \subsetneq \supset \in \notin \emptyset \varnothing$
* combinatorics: $\binom{n+1}{2k}$
* arrows: $\to \rightarrow \leftarrow \Rightarrow \Leftarrow \mapsto$
* statements and proofs: $\land \lor \lnot \forall \exists \top \bot \vdash \vDash$
* long dots: $\ldots$
* infinity: $\infty \aleph_0 \nabla \partial$
* limits: $\epsilon \varepsilon$
* vectors and hats: $\hat x, \bar y, \overline{abc}, \vec x$

Limit block:

$$\lim_{x\to 0}$$
### Diagrams <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 39; read: 2026-09-13 15:58:05; revision: 8; modified: 2026-09-13 15:58:05; -->
MindForger supports [Mermaid](https://github.com/mermaid-js/mermaid) ([cheatsheet](https://github.com/JakeSteam/Mermaid)) to render **diagrams**.


Flowchart diagram:

``` mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

Sequence diagram - note different Mermaid diagram markup encapsulation element which has different background rendering that code block:

<div class="mermaid">
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
</div>

GANTT diagram:

``` mermaid
gantt
        dateFormat  YYYY-MM-DD
        title GANTT diagrams in MindForger
        section A section
        Completed task            :done,    des1, 2014-01-06,2014-01-08
        Active task               :active,  des2, 2014-01-09, 3d
        Future task               :         des3, after des2, 5d
        Future task2              :         des4, after des3, 5d
        section Critical tasks
        Completed task in the critical line :crit, done, 2014-01-06,24h
        Implement parser and jison          :crit, done, after des1, 2d
        Create tests for parser             :crit, active, 3d
        Future task in critical line        :crit, 5d
        Create tests for renderer           :2d
        Add to mermaid                      :1d
```

---

💡 edit this Note to see the syntax <br/>
💡 if diagram expressions are **not** rendered, then you must **enable** them using menu `Workspace/Preferences/Viewer/Diagram support`.
### Comments <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 27; read: 2024-02-16 16:17:40; revision: 1; modified: 2022-02-26 08:27:46; -->
If you want **line** or **multi-line** comment that 
is strictly for yourself (readers of the converted 
document should not be able 
to see it, even with "view source") you could (ab)use 
the link labels (for use with reference style links) 
that are available in the core Markdown specification.

**Single line comment**:

[comment]: # (This is a comment, you cannot see it)

**Multi-line comment**:

[comment]: # (This is a comment)
[comment]: # (that spans multiple lines)
[comment]: # (and you cannot see it)

Note that two conditions are **important**:

* Using `#` (and not other delimiter allowed by Markdown specification)
* An empty line before the comment. Empty line after the comment has no impact on the result.

---

If you need **inline** comment, then use HTML comments:

* There is <!-- secret --> you cannot see.

---

💡 edit this Note to see the syntax
## Drag & Drop Images and Files <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 50; read: 2024-02-16 16:17:40; revision: 3; modified: 2024-02-16 15:24:09; -->
Drag:

* **file**
    * ... for example `.pdf`, presentation or `.zip` archive
* **image**
    * ... `.png`, `.gif`, ... or any other image
* **image data**
    * ... screenshot or image selection from Gimp, Krita or any other graphics editor

... and **drop** to Note/Notebook editor.

DnD allows easy import of attachments/images to MindForger
repository - either by value (choose `Copy` in attachment/image
dialog) or by reference (path to the file on local file system
is used).


## Table of contents generator <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 61; read: 2024-02-16 16:18:00; revision: 10; modified: 2024-02-16 16:18:00; -->
[![v](https://img.youtube.com/vi/UVVF22xG4hY/0.jpg)](https://www.youtube.com/watch?v=UVVF22xG4hY)


## Link completion <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 41; read: 2024-02-16 16:18:01; revision: 5; modified: 2024-02-16 15:24:06; -->
[![v](https://img.youtube.com/vi/YCn0ZJfe4nU/0.jpg)](https://www.youtube.com/watch?v=YCn0ZJfe4nU)

While editing a Note or Notebook write prefix of
a Notebook/Note name and use <kbd>Ctrl-/</kbd> to 
get link completion. When you choose a link from completer,
Markdown link to target Notebook/Note is automatically created.


# Markdown IDE <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 30; read: 2024-02-16 16:18:02; revision: 2; modified: 2024-02-16 15:25:35; -->
MindForger is more than just Markdown editor - it is integrated development environment (**IDE**) 
for the development of Markdown document collections (repositories, documentation, books, etc.):

* **multiple** Markdown documents can be opened in order to perform search, refactoring
  and analytics
* user defined **stencils** can be used to quickly create new notebooks and notes
* notebook **structure** can be easily refactored with outliner-style operations
  defined on notes
* both notebooks and notes can be **refactored** withing or across different notebooks and notes


## Open Markdown directory <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 25; read: 2024-02-16 16:18:03; revision: 1; modified: 2022-02-26 08:27:46; -->
You can open **any** directory and MindForger will find
all Markdown files within the directory and its sub-directories
and open them for search, navigation and editing:

```
$ mindforger a-git-repository-with-interesting-content
```

For example, you can find an [interesting Git repository](#markdown-content-and-examples)
on GitHub or BitBucket, clone it to your machine and open it 
with MindForger to easily navigate it.
### Multiple documents <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 23; read: 2024-02-16 16:18:03; revision: 2; modified: 2024-02-16 15:25:53; -->
![Image](user-documentation.multiple-documents.png)

You can open **any** directory and MindForger will find
all Markdown files within that directory and all its 
sub-directories and make them available for search, navigation 
and editation:

```
$ mindforger a-github-repository-with-interesting-content
```

Where `a-github-repository-with-interesting-content` is a directory
containing Markdown documents.

---

💡 if you openeded more than one MindForger document, you can see all documents indexed by MindForger by clicking menu `View/Notebooks`
## Stencils <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 21; read: 2024-02-16 16:18:04; revision: 1; modified: 2022-02-26 08:27:46; -->
![Image](user-documentation.stencils.png)

Stencil represents a common pattern that can be used in
various situations e.g. to solve a task. It might be a how to 
(like how to change a car wheel) that **once created**, you 
may want to use **repeatedly** w/ possibility of customization.

Notebook stencil corresponds to application of 
a problem/semantic domain to another problem. 
Once you have a _modus operandi_ or you know how to 
do that, than this is the case.

You can use a stencil when creating a **new** notebook
or note - check `Stencils` drop-down in the dialog
opened using menu `Notebook/New` or `Note/New`.

[MindForger repositories](#mindforger-repository) (including 
the default one) contain stencils for both notebooks and notes:

```
<mindforger repository>/
├── ...
└── stencils
    ├── notebooks
    └── notes
```

MindForger is shipped with an initial set of stencils for meeting
notes, software analysis/design, [GROW model](https://en.wikipedia.org/wiki/GROW_model)
etc. 

You can easily **extend** outlines just by copying Markdown file
to `stencils/notes` or `stencils/notebooks` directory.
## Refactoring <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 19; read: 2024-02-16 16:18:04; revision: 1; modified: 2022-02-26 08:27:46; -->
![Image](user-documentation.note-refactoring.png)

Hierarchy of **Notes** (Markdown document sections) can be easily
changed using operations introduced by [outliners](https://en.wikipedia.org/wiki/Outliner).
**Note** can be...

* moved up
* moved down
* demoted ~ moved deeper in Notes hierarchy
* promoted ~ moved lower in depth
* ... and more

To manipulate a note, choose it in the **outline view** (tree of notes/Markdown sections 
on the left) and either use shortcuts (<kbd>ctrl+up</kbd>, <kbd>ctrl+down</kbd>, 
<kbd>ctrl+left</kbd>, <kbd>ctrl+right</kbd>) or menu `Note/Promote`, ...
### Note refactoring <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 19; read: 2024-02-16 16:18:05; revision: 1; modified: 2022-02-26 08:27:46; -->
Note (Markdown section) can be refactoring (along with its child notes)
between different Notebooks (Markdown documents):

* choose **source** note to be refactored in the outliner tree of notes
* use menu `Note/Refactor` to specify **target** notebook

Note and its child notes will be moved to the target notebook.
## Home notebook <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 19; read: 2024-02-16 16:18:05; revision: 1; modified: 2022-02-26 08:27:46; -->
You can mark any notebook as **home** and it will be opened:

* on MindForger start
* using <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>h</kbd> keyboard shortcut

Home notebook can be **set**/unset using menu `Navigator/Make Home`.
# Search <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 17; read: 2024-02-16 16:18:05; revision: 1; modified: 2022-02-26 08:27:46; -->
Ability to find a specific Notebook or Note is one of the 
most important MindForger features. Notebooks and Notes
can be found by:

* full-text search (content)
* name
* tag(s)

---

💡 see menu `Recall` for search options
## Fulltext <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 17; read: 2024-02-16 16:18:06; revision: 1; modified: 2022-02-26 08:27:46; -->
Use menu `Recall/Full-text Search` to search for **notes**
using full-text search. Result shows notes Markdown source
with **highlighted** matches.

Search **scope**:

* If you run full-text search from notebooks
  view (menu `View/Notebooks`), then **all** notebooks and their
  notes are searched.
* If you run full-text search when a notebook is opened
  (notes outline on the left, note view/editor on the right),
  then **only** notes of that particular notebook are searched.
## Name <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 17; read: 2024-02-16 16:18:06; revision: 1; modified: 2022-02-26 08:27:46; -->
Use menu `Recall/Recall Notebook by Name` / `Recall/Recall Note by Name`
to search for **notebooks** / **notes** by name. Result shows as you
write the name in the dialog.

Search **scope**:

* If you run note search **by name** from notebooks
  view (menu `View/Notebooks`), then **all** notebooks notes
  are searched.
* If you run note search **by name** when a notebook is opened
  (notes outline on the left, note view/editor on the right),
  then **only** notes of that particular notebook are searched.
## Tag <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 18; read: 2024-02-16 16:18:06; revision: 1; modified: 2022-02-26 08:27:46; -->
Use menu `Recall/Recall Notebook by Tag` / `Recall/Recall Note by Tag`
to search for **notebooks** / **notes** by tag(s). Result shows as you
add/remove tags in the dialog.

Search **scope**:

* If you run note search **by tag** from notebooks
  view (menu `View/Notebooks`), then **all** notebooks notes
  are searched.
* If you run note search **by tag** when a notebook is opened
  (notes outline on the left, note view/editor on the right),
  then **only** notes of that particular notebook are searched.
# Thinking Notebook <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 15; read: 2024-02-16 16:18:06; revision: 1; modified: 2022-02-26 08:27:46; -->
MindForger aims to mimic human mind - **learning**, **recalling**, 
**recognition**, **associations**, **forgetting** - in order to achieve 
synergy with your mind to make your searching, reading and writing more 
productive:

* **learning**: MindForger loads Markdown document(s), parses them and construct [knowledge graph](#knowledge-graph-navigator) 
* **recalling**: you can recall notebooks/notes by content, name, tags, semantic domain, ...
* **recognition**: MindForger is able to recognize people, organization, places, ... in your remarks
* **associations**: MindForger suggests relevant notes as you browse, read and edit notebooks and notes
* **forgetting**: MindForger handles the process of scoping and forgetting analogous to human mind
## Learning <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 13; read: 2024-02-16 16:18:06; revision: 1; modified: 2022-02-26 08:27:46; -->
_...learning data, relationships, similarity (granularity N and O), relevancy in time (timestamps and R/W count), ..._

MindForger can be used to learn:

* manage knowledge in a [MindForger repository](#mindforger-repository)
* edit single [Markdown file](#markdown-file)
* edit [multiple Markdown files](#markdown-directory) in given (sub)directories
### MindForger repository <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 15; read: 2024-02-16 16:18:07; revision: 1; modified: 2022-02-26 08:27:46; -->
MindForger repository is a directory with specific 
[structure](developer-documentation.md#repository-layout) 
where MindForger stores your **knowledge**. It contains Markdown 
files ([Markdown hosted DSL](developer-documentation.md#markdown-hosted-dsl)) 
allowing you to get most of MindForger capabilities.

If you run MindForger without parameters, then it opens the
default MindForger repository:

```
$ mindforger
```

If MindForger default repository doesn't exist, then it is created
on MindForger first start in:

```
~/mindforger-repository
```

Repository structure looks like this:

```
$ tree mindforger-repository/

mindforger-repository/
├── limbo
├── memory
├── mind
└── stencils
    ├── notebooks
    └── notes
```
## Metadata <!-- Metadata: type: Note; tags: todo; created: 2022-02-26 08:27:46; reads: 18; read: 2024-02-16 16:18:21; revision: 2; modified: 2024-02-16 16:18:21; -->

### Tags <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 21; read: 2024-02-16 16:18:25; revision: 1; modified: 2022-02-26 08:27:46; -->

### Read/write statistics <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 15; read: 2024-02-16 16:18:26; revision: 1; modified: 2022-02-26 08:27:46; -->

### Progress <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 15; read: 2024-02-16 16:18:26; revision: 1; modified: 2022-02-26 08:27:46; -->

### Deadlines <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 15; read: 2024-02-16 16:18:26; revision: 1; modified: 2022-02-26 08:27:46; -->

### Things and types <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 15; read: 2024-02-16 16:18:26; revision: 1; modified: 2022-02-26 08:27:46; -->

### Relationships <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 17; read: 2024-02-16 16:18:26; revision: 1; modified: 2022-02-26 08:27:46; -->

## Auto-linking <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 21; read: 2024-02-16 16:18:27; revision: 5; modified: 2024-02-16 14:02:38; -->
![Autolinking](user-documentation.autolinking.png)

Autolinking discovers relevant notes in your MindForger repository and/or Markdown document
and automatically injects links to the text. In the screenshot above all links were injected
i.e. source text (Markdown) is just plain text without links.

Autolinking helps in immediately finding remarks related to the notebooks and notes you 
are browsing.

Autolinking also saves the time - you don't have to create/change/maintain links in your
remarks.

Tips and tricks:

* If note name contains `:`, then **only** text preceding `:` is used for matching.
    * Example: if "GPS: General positioning system" is note name, then text is searched for "GPS" only
      as it brings more matcheds.
* Autolinking can be configured so that it performs **case insensitive search** for the first letters
  in note names.
    * Example: if "Stencils" is note name, then text is searched **also** for "stencils"
      as it brings more matcheds.
* Autolinking can be quickly toggled using menu.
     
## TaYR: Think as you Read <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 15; read: 2024-02-16 16:18:27; revision: 1; modified: 2022-02-26 08:27:46; -->
![TAYR](user-documentation.tayr.png)

MindForger is able to **suggest relevant notes** as you browse and
read:

* relevant notes are computed for the note being currently **selected**
* relevant notes are shown in the **lower left corner** by `Associations` table
* similarity score in the `Associations` table indicates **relative relevancy** in %


In the screenshot above you can see relevant notes (lower left corner) for the selected
note `My 3D Printer MK2S by Prusa RESEARCH`.

See also: [think vs. sleep mode](#think-vs--sleep-mode)
## TaYW: Think as you Write <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 13; read: 2024-02-16 16:18:28; revision: 1; modified: 2022-02-26 08:27:46; -->
![TAYW](user-documentation.tayw.png)

MindForger is able to **suggest relevant notes** as you write note
content in the editor:


* relevant notes are computed for the **word under the cursor**
* relevant notes are shown in the **lower left corner** by `Associations` table
* similarity score in the `Associations` table indicates **relative relevancy** in %


In the screenshot above you can see relevant notes (lower left corner) for the selected
word `graph` (notice cursor between letter `g` and `r` on the current line with light-gray background).
## TaYB: Think as you Browse <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 15; read: 2024-02-16 16:18:28; revision: 1; modified: 2022-02-26 08:27:46; -->
![Navigator](user-documentation.knowledge-graph-navigator.png)

**Knowledge graph navigator** allows you to browse notebooks, notes, tags and other resources
in **visually**.

Navigator can be either activated using toolbar or using <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>k</kbd> keyboard
shortcut. It is **scope sensitive** e.g. if you activate navigator while viewing note, then this note
becomes central node of the visualization.

Knowledge graph can be **zoomed**, **shuffled** and its edgest can be (globally) stretched/shrinked.

_... how exactly it thinks and why it's useful_
## TaYS: Think as you Search <!-- Metadata: type: Note; tags: todo; created: 2022-02-26 08:27:46; reads: 26; read: 2024-02-16 16:18:36; revision: 6; modified: 2024-02-16 16:18:36; -->
_...[semantic search - this feature is being implemented - RAG]..._


## Knowledge graph navigator <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 23; read: 2024-02-16 16:18:37; revision: 2; modified: 2024-02-16 15:27:00; -->
> _"I hear, and I forget; I see, and I remember." -- Chinese proverb_


## Scopes <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 26; read: 2024-02-16 16:18:38; revision: 2; modified: 2024-02-16 15:28:08; -->
MindForger works with two types of scopes:

* [Time Scope](#time-scope)
* [Tag Scope](#tag-scope)


### Time Scope <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 23; read: 2024-02-16 16:18:38; revision: 1; modified: 2022-02-26 08:27:46; -->
Use menu `Mind/Scope` or <kbd>Alt+m c</kbd> to configure **time** scope.

---

Consider the following situations:

* Over the years your employer company internal systems change and/or
  you work for a number of different employers. Each time there is 
  a different/better/stronger 
  Wifi authentication configuration (video conference
  setup, payslips system, etc.). Therefore in you memory (or in MindForger
  remarks) there are **multiple** how-tos, but you want to use
  only the **recent** want. At the same time you do not want to
  (explicitly) remove/purge the previous how-tos as they can be useful in different
  situations.

* You learn how to manually divide two long numbers as a child.
  Then you do **not** need this skill **for years** as you use calculator/computer.
  When you want to learn your child how to manually divide numbers,
  you have to find it (deep) in your memory.

This is where MindForger **time scope** functionality comes in - you can 
restrict the scope (notes working set) by **time**. For example:

* you work on a project and want to see only notes you modified **today**
* whenever you use MindForger you want to work with notes not older
  than **18 months**
* when reading/working with your employer internal systems how-to **notebook** you want to
  see only notes younger than **1 year**

In particular you can set **global** time scope:

* Notebooks listing: 
    * Only **noteboks** within given time scope (younger) will be shown.
* Add/forget notebook:
    * Notebooks can be added/forgotten.
* Notebook's note tree view: 
    * Only notes within given time scope will be shown.
      If note **is** within timescope and note's parent notes are **not**, then note **is**
      shown along with its parents (parents would be normally hidden). In other words, fresh note
      ensures its parents are shown.
* Add/remove note: 
    * Notes can be added/forgotten.
    * **IMPORTANT**: remember that note can be forgotten **along with its child notes** that can be
      hidden (if they didn't match time scope) i.e. you may delete notes you don't see.
* Promote/demote/up/down note:
    * Notes can be added/forgotten.
    * **IMPORTANT**: remember that these operations work on the **non-filtered* model i.e.
      you perform operation (e.g. up), nothing seems to happen, but the note was just moved above
      a hiddin note that is not in scope i.e. you refactor notes you don't see.
* Note refactoring:
    * Notes can be refactoring (to other notebook) and extracted.
    * **IMPORTANT**: remember that note can be refactored **along with its child notes** that can be
      hidden (if they didn't match time scope) i.e. you may move notes you don't see.
     
In particular you can set **note** specific time scope that overrides global time scope:

* ... behaviour is the same as above except that this setting has no effect on notebooks listing ...
### Tag Scope <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 15; read: 2024-02-16 16:18:39; revision: 1; modified: 2022-02-26 08:27:46; -->
Use menu `Mind/Scope` or <kbd>Alt+m c</kbd> to configure **tag(s)** scope.

---

Scoping using **tag(s)** allows you to limit notebook **working set** only
to notebooks having specified set of tags. It's useful when you work with
bigger MindForger repositoriers and you don't want to be distracted by
unrelated notebooks.

Scoping using tags can be combined (`AND`) with [scoping using time](#time-scope).
## Recognize what matters <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 18; read: 2024-02-16 16:18:50; revision: 2; modified: 2024-02-16 15:29:03; -->


### Named-entity recognition <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 19; read: 2024-02-16 16:18:51; revision: 1; modified: 2022-02-26 08:27:46; -->
![Image](user-documentation.ner.png)

_This feature is being implemented._
### Semantic search and domains <!-- Metadata: type: Note; tags: todo; created: 2022-02-26 08:27:46; reads: 17; read: 2024-02-16 16:18:56; revision: 4; modified: 2024-02-16 16:18:56; -->
_...[semantic search - this feature is being implemented - RAG]..._

Word embeddings based search, associations and navigation.


## Forgetting <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 17; read: 2024-02-16 16:19:03; revision: 1; modified: 2022-02-26 08:27:46; -->
> Motto: "Computers need to forget". -- [Viktor Mayer-Schönberger](http://blog.mindforger.com/2007/11/computers-need-to-forget.html)

Before I deep dive to MindForger features let me formulate
a few questions to explain the motivation behind 
forgetting/scoping related functionality:

* Do we forget or we simply don’t remember?
* When we forget?
* How and where exactly forgetting in our minds happens?
* If we remember something, can it be forgotten?
* Do we need to forget and why?

I believe that if a concept makes it to long term memory
(LTM), then it can be never forgotten. It’s in LTM and 
it always be there. The only question is how many 
association/links it has. In the worst case it may happen 
that there is no association path it it - it ends as an
island or orphan better said. If it’s not reminded or not 
used for long time, association can get weaker and weaker 
and such concepts is diving deeper and deeper to LTM. However,
it is always there. Thus it’s just about the lookup. 
According to my experience a strong emotional experience or 
return to the deeper paths of LTM (talking about your friends 
or family about your early childhood) helps to remind such
concepts and in the latter case even strongly bind them 
to upper level LTM (move them up in the memory) and 
refresh such memories so that you can remind them later 
much more easier.

If there would be no possibility of the selection of sensed
informations and all the sensing will be fixed in our 
memory, its capacity would be fully used very soon.

MindForger, as computer program, needs to forget. But
forgetting does **NOT** mean deleting of information.

MindForger maintains **all** the remarks you ever written
(see [limbo](#limbo)), but works with/shows only with 
a [scope](#time-scope) **configurable** by you.
### Limbo <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 26; read: 2024-02-16 16:19:06; revision: 5; modified: 2024-02-16 16:19:06; -->
[![v](https://img.youtube.com/vi/gtGbCdb_7c8/0.jpg)](https://www.youtube.com/watch?v=gtGbCdb_7c8)

MindForger does **not** **delete** notebooks - it moves them to a location called Limbo that
can be found in `${ACTIVE_MF_REPOSITORY}/limbo`. This is where you can delete Markdown
documents permanently.

MindForger, in its current implementation, **does** delete notes. They are not moved to a note Limbo.
If you use menu `Note/Forget`, then the note is deleted. 

Side note: I personally use CMS (Git) - I have full history of notebooks and notes. Tracking of
all notes would be useful, however HW resource consumption intensive. This is also
why I don't want to duplicate this (already sophisticated) functionality within MindForger.


# Productivity <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 21; read: 2024-02-16 16:19:06; revision: 1; modified: 2022-02-26 08:27:46; -->
MindForger aims to help you when you study, write a document/paper/article/book or
want to achieve a goal.

Therefore it enables you to...

* prioritize work on notebooks using **urgency** and **importance**
* helps you to decide what you do first and next using **Eisenhower matrix**
* track **progress** in %
* specify **deadlines** (for notes)
## Urgency and Importance <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 23; read: 2024-02-16 16:19:07; revision: 1; modified: 2022-02-26 08:27:46; -->
![Image](user-documentation.importance-urgency-edit.png)

When creating (menu `Notebook/New`) or editing **notebook** (edit mode `More...` button) you
can specify:

* **importance** property ~ how important is the notebook
* **urgency** property ~ how important is (study/challenge/...) task related to notebook (or notebook content itself)

![Image](user-documentation.importance-urgency-view.png)

These properties are in turn shown in **notebooks view** (menu `View/Notebooks`) and [Eisenhower matrix](#eisenhower-matrix).
### Eisenhower matrix <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 29; read: 2024-02-16 16:19:08; revision: 1; modified: 2022-02-26 08:27:46; -->
![Image](user-documentation.eisenhower-matrix.png)


**Wikipedia**: [Eisenhower matrix](https://en.wikipedia.org/wiki/Time_management#The_Eisenhower_Method) stems from a quote attributed to Dwight D. Eisenhower: "I have two kinds of problems, the urgent and the important. The urgent are not important, and the important are never urgent."

Using the Eisenhower Decision Principle, tasks are evaluated using the criteria [important/unimportant](#urgency-and-importance) and [urgent/not urgent](#urgency-and-importance), and then placed in according quadrants in an **Eisenhower Matrix** (also known as an "Eisenhower Box" or "Eisenhower Decision Matrix"). Tasks are then handled as follows:

Tasks in

1. **Important/Urgent quadrant** are done immediately and personally e.g. crises, deadlines, problems.
1. **Important/Not Urgent quadrant** get an end date and are done personally e.g. relationships, planning, recreation.
1. **Unimportant/Urgent quadrant** are delegated e.g. interruptions, meetings, activities.
1. **Unimportant/Not Urgent quadrant** are dropped e.g. time wasters, pleasant activities, trivia.

This method is said to have been used by U.S. President Dwight D. Eisenhower.
## Organizers: tag-based aspects <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 46; read: 2024-02-16 16:19:14; revision: 6; modified: 2024-02-16 16:19:14; -->
[![v](https://img.youtube.com/vi/Tje2mso7jNY/0.jpg)](https://www.youtube.com/watch?v=Tje2mso7jNY)


### Eisenhower matrix on tags <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 41; read: 2024-02-16 16:19:15; revision: 6; modified: 2024-02-16 15:35:56; -->
![i](user-documentation.eisenhower-matrix.png)

The **Eisenhower Matrix**, also known as the **Eisenhower Decision Matrix** or simply the **Eisenhower Box**, is a time management tool that helps prioritize tasks based on their urgency and importance. It is named after Dwight D. Eisenhower, the 34th President of the United States, who was known for his effective time management skills.

The matrix categorizes tasks into four quadrants:

1. **Urgent and Important** (Do First): These are the tasks that require immediate attention and have high priority. They should be done as soon as possible to avoid negative consequences or missed opportunities.

2. **Important**, but Not Urgent (Schedule): These tasks are important for long-term goals but do not require immediate action. They should be scheduled and given appropriate time and attention.

3. **Urgent**, but Not Important (Delegate): These tasks are time-sensitive but do not contribute significantly to your goals. They should be delegated to others if possible, to free up your time for more important tasks.

4. **Not Urgent and Not Important** (Eliminate): These tasks are low priority and do not contribute to your goals. They should be eliminated or minimized to make room for more important activities.

Using the Eisenhower Matrix helps in prioritizing tasks effectively, reducing procrastination, and ensuring that important goals are not overlooked. It encourages a focus on important tasks, enables better time allocation, and maximizes productivity.


### Kanban on Tags <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 33; read: 2024-02-16 16:19:15; revision: 8; modified: 2024-02-16 15:40:33; -->
[![v](https://img.youtube.com/vi/Tje2mso7jNY/0.jpg)](https://www.youtube.com/watch?v=Tje2mso7jNY)

**Kanban** is a project management methodology that originated from the Toyota Production System in the late 1940s. It is a visual system that helps teams track and manage their work. The word "Kanban" **translates** to "visual signal" or "card" in Japanese.

In Kanban, the work is represented as cards or sticky notes, which are placed on a board with different **columns** that represent the various **stages** of the workflow, such as **"To Do"**, **"In Progress"**, and **"Done"**. This provides a clear visual representation of the work in progress and allows team members to see what tasks are in each stage of development.

The key principles of Kanban include visualizing workflow, limiting work in progress, and focusing on continuous improvement. By visualizing the work, you can identify **bottlenecks** and areas for **improvement**.

MindForger allows you to create **Kanban boards** and organize [notes](Getting-started.md#note) to **columns** using [tags](#tags).


# Machine learning: NLP <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 21; read: 2024-02-16 16:19:16; revision: 1; modified: 2022-02-26 08:27:46; -->
> _"Artificial intelligence will overcome natural intelligence soon. However, natural stupidity can never be replaced by the artificial one." -- Jára da Cimrman_
## CSV export <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 26; read: 2024-02-16 16:19:17; revision: 13; modified: 2024-02-16 15:53:09; -->
![i](user-documentation.export-workspace-to-csv.png)

You can export [workspace](Getting-started.md#workspace) to comma separated file (CSV):

1. open menu `Workspace`
1. choose `Export` menu item
1. choose `CSV` sub-menu item
1. `Export Workspace to CSV` dialog is opened:
   - type in file name
   - choose whether you want to encode notebook [tags](#tags) using
     **one hot encoding** (OHE)
1. click <kbd>Export</kbd> to export the workspace


# Coaching <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 22; read: 2024-02-16 16:19:17; revision: 6; modified: 2024-02-16 16:00:23; -->
<!-- reuse any help / text that I have in GAE MindForger -->

(Auto) **coaching** is a self-improvement process where individuals provide themselves with guidance, support, and feedback to achieve personal or professional goals. It involves self-reflection, setting goals, creating action plans, and monitoring progress. 

Auto coaching usually incorporates various techniques like journaling, visualization, affirmations, and self-assessment tools to foster self-awareness, self-motivation, and personal growth. It is a proactive approach to personal development and can be done through books, online resources, or through the use of specific self-coaching methodologies.

MindForger can be used as an **auto coaching tool**.


## GROW model <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 23; read: 2024-02-16 16:19:18; revision: 5; modified: 2024-02-16 15:58:48; -->
![Image](screenshot.grow-model.png)

The **GROW model** is a popular (auto) **coaching** framework that is used to structure a conversation or coaching session. GROW stands for **Goal**, **Reality**, **Options**, and **Way Forward**. The model helps individuals or teams set clear goals, explore the current reality, generate options for actions, and establish a plan to move forward. It is widely used in areas such as personal development, career coaching, and leadership coaching.

Use MindForger GROW model [stencil](#stencils) to create G.R.O.W. [notebook](Getting-started.md#notebook) with **questions** allowing you to efficiently use the G.R.O.W method.


## SMARTER goals <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 20; read: 2024-02-16 16:19:18; revision: 2; modified: 2024-02-16 16:00:13; -->
SMARTER goals is a framework used to set effective and measurable **goals**. It stands for:

1. **Specific**: Goals should be clear and well-defined. Avoid vague or general statements. Specify what exactly you want to achieve.

2. **Measurable**: Goals should be quantifiable so that progress can be easily tracked. Include specific criteria or indicators to measure success.

3. **Attainable**: Goals should be realistic and within reach. Consider the resources, skills, and time available to achieve the goal.

4. **Relevant**: Goals should be aligned with your overall objectives and have significance to your life or work. Ensure they are worthwhile and meaningful.

5. **Time-bound**: Goals should have a clear deadline or timeline. Set specific dates to create a sense of urgency and to keep yourself accountable.

6. **Evaluate**: Continuously monitor and evaluate progress towards your goals. Assess whether adjustments or improvements are needed.

7. **Readjust**: Adapt or readjust your goals as necessary, based on new information or changing circumstances. Remain flexible and open to revisions.


# Tools <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 26; read: 2024-02-16 16:19:18; revision: 2; modified: 2024-02-16 16:06:06; -->
MindForger tools:

* [CLI](#cli) 


## CLI <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 29; read: 2024-02-16 16:19:18; revision: 12; modified: 2024-02-16 16:11:20; -->
In certain situations, it is faster to use commands to navigate around the MindForger UI instead of using a mouse. In these cases, you can use the **command line interface** (CLI):

* activate CLI using one of the following options:
    - <kbd>Alt-x</kbd>
    - choose `View` menu, `CLI` sub-menu
* type `?` to get help
* type `/` to find [notebooks](Getting-started.md#notebooks) and [notes](Getting-started.md#note)
* type `@` to search internet sites like arXiv or Wikipedia for knowledge
* type `>` to run a command


# Cheatsheets <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 29; read: 2024-02-16 16:19:19; revision: 1; modified: 2022-02-26 08:27:46; -->
See MindForger cheetsheet(s):

* [Keyboard Shortcuts](#keyboard-shortcuts)
## Markdown cheatsheet <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 46; read: 2024-02-16 16:19:19; revision: 5; modified: 2024-02-16 16:04:07; -->
See [Markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).


## MathJax cheatsheet <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 39; read: 2026-09-13 15:17:52; revision: 5; modified: 2024-02-16 16:04:01; -->
See [MathJax cheat sheet](#mathjax).


# Keyboard shortcuts <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 27; read: 2024-02-16 16:19:23; revision: 3; modified: 2024-02-16 15:49:48; -->
<!-- ... per-platform + explain how to navigate using ALT, suggest tooltips to determine shortcuts, list THE MOST IMPORTANT only here -->

Prefer menu based keyboard shortcuts which are self-documented e.g.

* <kbd>Alt+o n</kbd>
    * create new notebook
* <kbd>Alt+o e</kbd>
    * edit currently viewed notebook
* <kbd>Alt+n n</kbd>
    * create new note
* <kbd>Alt+n e</kbd>
    * edit currently viewed note
* ... and many others...


Editor:

* <kbd>Alt+Left</kbd>
    * ... save Note, leave editor and show rendered HTML.
* <kbd>Ctrl+g</kbd>
    * ... cancel editation and leave editor without saving

Views:

* <kbd>Ctrl+Shift+o</kbd>
    * ... recall n**o**tebook.
* <kbd>Ctrl+Shift+n</kbd> 
    * ... recall **n**ote.
## Linux keyboard shortcuts <!-- Metadata: type: Note; tags: todo; created: 2022-03-10 08:49:39; reads: 34; read: 2024-02-16 16:19:27; revision: 5; modified: 2024-02-16 16:19:27; -->
...


## macOS keyboard shortcuts <!-- Metadata: type: Note; tags: todo; created: 2022-03-10 08:50:13; reads: 36; read: 2024-02-16 16:19:31; revision: 4; modified: 2024-02-16 16:19:31; -->
...


## Windows keyboard shortcuts <!-- Metadata: type: Note; tags: todo; created: 2022-03-10 08:50:29; reads: 32; read: 2024-02-16 16:19:34; revision: 4; modified: 2024-02-16 16:19:34; -->
...


# Command line and man <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 23; read: 2024-02-16 16:19:35; revision: 1; modified: 2022-02-26 08:27:46; -->
For information on MindForger command line options read the manual page:

```shell
man mindforger
```
For command options see the help file:

```shell
$ mindforger --help

Usage: mindforger [options] [<directory>|<file>]
Thinking notebook.

Options:
  -t, --theme <theme>            Use 'dark', 'light' or other GUI <theme>.
  -c, --config-file-path <file>  Load configuration from given <file>.
  -v, --version                  Displays version information.
  -h, --help                     Displays this help.

Arguments:
  [<directory>|<file>]           MindForger repository or directory/file with
                                 Markdown file(s) to open
```
# Library <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 26; read: 2024-02-16 16:19:35; revision: 6; modified: 2024-02-16 15:52:41; -->
![i](user-documentation.library-add.png)

<!--- example content, how to open it, link it from MD sections at the beginning of doc - list it here, awesome-markdown-repositories/ update and copy paste here, link and encourage to suggest -->

Library bring ability to index external PDF files and generate Notebooks which represent them in MindForger. Synchronization and removal of the library (directory with files) is supported as well.


# Credits <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 36; read: 2024-02-16 16:19:35; revision: 11; modified: 2024-02-16 16:02:53; -->
<!-- doc 2 wiki Python script to copy latest version of CREDITS.md from mindforger repo 2 here -->
Written by [Martin Dvorak](http://me.mindforger.com).

Acknowledgements to contributors:

* Vlasta 'Šaman' Hajek / [Bonitoo.io](https://www.bonitoo.io/) (Windows port)

Big thanks to 3rd party FOSS content authors:

* John Gruber ([Markdown](https://daringfireball.net/projects/markdown/) - spec)
* Qt Company ([Qt](https://www.qt.io/) - lib and code)
* GitHub ([CMark GFM](https://github.com/github/cmark-gfm) - Markdown rendering - lib)
* Kevin Hendricks, Bjoern Jacke, Lázsló Németh ([Hunspell](https://github.com/hunspell/hunspell) - spellcheck - lib)
* Daniel Stenberg ([cURL](https://curl.se) - libcurl with GnuTLS flavor)
* Niels Lohmann ([json](https://github.com/nlohmann/json) - JSon for modern C++ library)
* NetBSD Foundation (strptime - Windows port - lib)
* Toni Ronkko (dirent - Windows port - lib)
* Microsoft (getopt - Windows port - lib)
* Jordan Russell ([jrsoftware.org](http://jrsoftware.org) - Windows installer framework)
* Graeme Gott and Wereturtle ([Ghostwriter](https://github.com/wereturle/ghostwriter) - inspiration and code)
* Christian Loose ([CuteMarkEd](https://cloose.github.io/CuteMarkEd/) - inspiration and code)
* Jean-loup Gailly, Mark Adler ([Zlib](https://sourceforge.net/projects/gnuwin32/) - library)
* David Parsons ([Discount](http://www.pell.portland.or.us/~orc/Code/discount/) - Markdown rendering - library used in the past)
* Google ([Google C++ unit testing framework](https://github.com/google/googletest))
* Knut Sveidqvist ([Mermaid.js](https://mermaidjs.github.io/) - diagrams and flowcharts rendering in HTML)
* AMS and SIAM ([MathJax.js](https://www.mathjax.org/) - math rendering in HTML)
* Ivan Sagalaev ([Highlight.js](https://highlightjs.org/) - source code syntax highlighting)
* Danny Allen (primary [icon theme](https://store.kde.org/content/show.php?content=18317) store.kde.com - icons)
* Krita (https://github.com/KDE/krita - menu icons - remixed)
* Travis CI ([travis-ci.org](https://travis-ci.org/) - continous integration tests and builds infra - Ubuntu, macOS)
* AppVeyor CI ([appveyor.com](https://www.appveyor.com/) - continous integration tests and builds infra - Windows)
* Raimund Hocke ([SikuliX](http://sikulix.com/)- GUI automation testing)
* Lewis Van Winkle ([GENANN](https://github.com/codeplea/genann) - minimal neural network - library)
* Oleander Software ([Oleander stemming library](http://www.oleandersolutions.com/stemming/stemming.html) - stemmer - library)
* Jamie McGowan ([Remarkable](https://remarkableapp.github.io/) - inspiration and code)
* Andrey Smirnov ([Aptly](https://www.aptly.info/) - Debian PPAs mgmt tool)
* Apiary ([API blueprints](https://apiary.io/) - test data)
* Mark Summerfield ([Advanced Qt Programming](http://www.qtrac.eu/aqpbook.html) book examples - code snippets)
* Andres Mejia (Aho-Corasick algorithm implementation - code snippets)
* SQLite ([main file blessing](https://github.com/sqlite/sqlite/blob/master/src/main.c) - inspiration)

See [licenses](./licenses) folder for 3rd party content licensing details.

Acknowledgements to researchers:

* Karel Moulik (long term vision and ideas, consultations)
* Tomas Sieger (MindForger applications ideas, consultations)
* Gekaremi (comprehensive AI/NLP research, ideas and suggestions)

Acknowledgements to reviewers, testers and supporters:

* Ivan Kudibal (review, adoption and project support)
* Stefan Pacinda (review, testing)
* Petr Kozelka (MacBook borrowing, consultations)
* Tomas 'Floex' Dvorak (review, testing)
* Honza Odstrcil (feedback)

Special thanks to:

* Bjarne Stroustrup (C++ - for inspiring visions and being the authority behind C++ language)
* Linus Torvalds (Linux and Git - for being inspiration and strong opinions)
* Richard Stallman (GNU and GNU GPL - for passionate software freedom activism)


