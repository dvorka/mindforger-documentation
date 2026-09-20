# Getting Started <!-- Metadata: type: Outline; created: 2024-02-13 08:09:03; reads: 491; read: 2024-02-16 15:43:16; revision: 485; modified: 2024-02-16 15:43:16; importance: 0/5; urgency: 0/5; -->
Getting started with **MindForger**.

Table of contents:

* [Basics](#basics)
    * [Workspace](#workspace)
    * [Notebook](#notebook)
    * [Note](#note)
* [Create Workspace](#create-workspace)
    * [Create Notebook](#create-notebook)
        * [Create Note](#create-note)
        * [Edit Note](#edit-note)
        * [Fix Grammar with Wingman](#fix-grammar-with-wingman)
* [Notes Outliner](#notes-outliner)
* [Find Note](#find-note)
* [Delete Notebook](#delete-notebook)
* [Video tutorials](#video-tutorials)
    * [🎞 MindForger: From Markdown editor to thinking notebook](#mindforger--from-markdown-editor-to-thinking-notebook)
    * [🎞 MindForger: First steps](#mindforger--first-steps)


# Basics <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 130; read: 2024-02-16 15:42:41; revision: 34; modified: 2024-02-13 18:36:21; -->
![desktop](GETTING_STARTED.basic-concepts-overview.png)

This section aims to explain basic MindForger terminology:

* [Workspace](#workspace)
* [Notebook](#document---notebook)
* [Note](#section---note)

In short:

* The MindForger [workspace](#workspace) is analogous **the desktop** of an office desk.
    * The MindForger [notebook](#notebook) analogous to **a notepad** on the desktop.
        * A MindForger [note](#note) is analogous to **a page with the note** from a **notepad**.

Let's describe basic terms in more detail.


## Workspace <!-- Metadata: type: Note; created: 2024-02-10 22:53:08; reads: 129; read: 2024-02-16 15:42:41; revision: 15; modified: 2024-02-14 22:18:51; -->
![desktop](GETTING_STARTED.basic-concepts-workspace.png)

MindForger **workspace**:

* ... contains [notebooks](#notebook)
* ... stored in a directory on the filesystem
* ... has its own configuration
* ... might be empty


## Notebook <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 145; read: 2024-02-16 15:42:42; revision: 21; modified: 2024-02-13 19:18:13; -->
![desktop](GETTING_STARTED.basic-concepts-notebook.png)

MindForger **notebook**:

* contains [notes](#note)
* organizes notes in hierarchy - [outline](USER_DOCUMENTATION.md#outliner)
* can be marked with [tags](USER_DOCUMENTATION.md#tag)
* is typically devoted to a specific topic such as a project plan, family gifts or lessons learned
## Note <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 115; read: 2024-02-16 15:42:42; revision: 11; modified: 2024-02-13 19:18:43; -->
![desktop](GETTING_STARTED.basic-concepts-overview.png)

MindForger **note**:

* contains text, images and links
* can link notebooks and notes (within the [Workspace](#workspace)) and/or files and URLs
* can be marked with [tags](USER_DOCUMENTATION.md#tag)


# Create Workspace <!-- Metadata: type: Note; created: 2024-02-13 07:57:32; reads: 120; read: 2024-02-16 15:43:16; revision: 32; modified: 2024-02-16 15:43:16; -->
[![v](https://img.youtube.com/vi/ahThnkU9d90/0.jpg)](https://www.youtube.com/watch?v=ahThnkU9d90)

Create **new** [workspace](#workspace) as follows:

1. open menu `Workspace`
1. choose `New` menu item
1. choose `Workspace` sub-menu item
1. `New Workspace` dialog is opened:
   - type in workspace name 
   - feel free to modify where to store the workspace on the filesystem
1. click <kbd>New</kbd> to create the workspace


## Create Notebook <!-- Metadata: type: Note; created: 2024-02-13 07:57:40; reads: 136; read: 2024-02-16 15:42:43; revision: 18; modified: 2024-02-14 08:15:28; -->
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


### Create Note <!-- Metadata: type: Note; created: 2024-02-13 07:57:43; reads: 148; read: 2024-02-16 15:42:45; revision: 18; modified: 2024-02-14 08:57:40; -->
Create **new** [note](#note) as follows:

1. open menu `Note`
    - 💡 if `Note` menu might is disabled, 
      then open the [notebook](#notebook) in which you want to add the note
1. choose `New` menu item
1. `New Note` dialog is opened:
   - type in note name 
   - feel free modify note creation options and tags
1. click <kbd>OK</kbd> to create the note


### Edit Note <!-- Metadata: type: Note; created: 2024-02-13 08:19:27; reads: 142; read: 2024-02-16 15:42:48; revision: 15; modified: 2024-02-14 08:12:21; -->
When you are viewing a [note](#note), you can edit it using one of the options below:

* **Double click** the mouse preview.
* Use <kbd>Ctrl-e</kbd> keyboard shortcut (Linux/Win).
* Use <kbd>Alt-n e</kbd> keyboard shortcut (Linux/Win).

Once you finish editing the [note](#note) you can save it and preview using one of the options below:

* Use <kbd>Alt-⬅</kbd> keyboard shortcut.
* Click <kbd>Save & Leave</kbd> button at the bottom of the editor.


### Fix Grammar with Wingman <!-- Metadata: type: Note; created: 2024-02-13 08:22:36; reads: 156; read: 2024-02-16 15:42:49; revision: 25; modified: 2024-02-14 08:33:34; -->
[![v](https://img.youtube.com/vi/QLX9CWzzEa8/0.jpg)](https://www.youtube.com/watch?v=QLX9CWzzEa8)

Wingman is MindForger's private AI assistant which runs a large language model on your computer - to set it up
see [LLM provider configuration](USER_DOCUMENTATION.md#llm-provider-configuration).
While you are editing a [note](#note), you can **fix grammar** of the text as follows:

1. select a text withing the note editor
1. open Wingman chat window using <kbd>Ctrl-/</kbd> (Linux/Win)
1. specify prompt:
    - custom prompt: type in `Fix grammar: #TEXT` (`#TEXT` is replaced by the text you selected in the note editor)
    - predefined prompt: choose `Fix grammar: #TEXT` from the drop down
1. click `Run`
1. check LLM model answer
1. if you are satisfied, then click `Replace` and the fixed text from the Wingman chat window
   will replace the text in the note

... Wingman can do **much more**:

* complete sentences, paragraphs or portions of the text
* reformulate / rewrite the text - formally, informally, in a slang, like a person (Kafka), etc.
* provide synonyms and antonyms
* explain 

... and much more - for more details see [Wingman](USER_DOCUMENTATION.md#wingman).


# Notes Outliner <!-- Metadata: type: Note; created: 2024-02-13 08:19:31; reads: 140; read: 2024-02-16 15:42:50; revision: 26; modified: 2024-02-16 14:03:32; -->
[![v](https://img.youtube.com/vi/LUqavHfKhnc/0.jpg)](https://www.youtube.com/watch?v=LUqavHfKhnc)

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


# Find Note <!-- Metadata: type: Note; created: 2024-02-13 08:21:00; reads: 118; read: 2024-02-16 15:42:58; revision: 12; modified: 2024-02-14 09:00:13; -->
[![v](https://img.youtube.com/vi/a-i7EU58H7Y/0.jpg)](https://www.youtube.com/watch?v=a-i7EU58H7Y)

You can **find** [notebooks](#notebook) and [notes](#note) using the following attributes:

* name
* text phrase
* tag

For instance, to find [notes](#note) by text phrase:

1. open menu `Find`
1. choose `Full-text search` menu item
1. `Search` dialog is opened:
   - type in **search phrase**
1. click <kbd>Search</kbd> to search for notes containing the phrase
1. preview and select a note to open in the search results

Similarly, for other search options.


# Delete Notebook <!-- Metadata: type: Note; created: 2024-02-13 08:20:07; reads: 89; read: 2024-02-16 15:42:56; revision: 19; modified: 2024-02-16 15:29:26; -->
[![v](https://img.youtube.com/vi/gtGbCdb_7c8/0.jpg)](https://www.youtube.com/watch?v=gtGbCdb_7c8)

[Notebook](#notebook) can be ~~deleted~~ **deprecated** as follows:

1. open the [notebook](#notebook) you want to delete (be sure that you are not editing a note)
1. open menu `Notebook`
1. choose `Deprecate` menu item
1. `Deprecate Notebook` dialog is opened
1. click <kbd>Yes</kbd> to deprecate the notebook

As you can see, [notebooks](#notebook) in MindForger are not deleted,
but **deprecated** - they are moved to a **limbo** directory. To
purge or resurrect deprecated notebook:

1. open menu `View`
1. choose `Limbo`menu item
1. use you file manager to manipulate the notebook


# Video tutorials <!-- Metadata: type: Note; created: 2024-02-13 18:29:52; reads: 45; read: 2024-02-16 14:06:27; revision: 11; modified: 2024-02-14 08:21:15; -->
MindForger **video** tutorials:

* 🎞 [playlist](https://www.youtube.com/playlist?list=PLkTlgXXVRbUDdvysdslnAt_mU15oNPWNS) on YouTube


## 🎞 MindForger: From Markdown editor to thinking notebook <!-- Metadata: type: Note; created: 2024-02-13 18:30:01; reads: 45; read: 2024-02-14 09:00:21; revision: 13; modified: 2024-02-14 08:20:35; -->
[![v](https://img.youtube.com/vi/PlW2e1X3O-I/0.jpg)](https://www.youtube.com/watch?v=PlW2e1X3O-I)


## 🎞 MindForger: First steps <!-- Metadata: type: Note; created: 2024-02-13 18:33:42; reads: 25; read: 2024-02-14 09:00:22; revision: 6; modified: 2024-02-13 18:34:27; -->
[![v](https://img.youtube.com/vi/UR49y3uNurs/0.jpg)](https://www.youtube.com/watch?v=UR49y3uNurs)


