# FAQs <!-- Metadata: type: Outline; created: 2022-02-26 08:27:46; reads: 37; read: 2022-03-10 08:21:33; revision: 37; modified: 2022-03-10 08:21:33; importance: 0/5; urgency: 0/5; -->
<!-- find all GitHub issues with "question" label (even closed) and turn them to questions in this Notebook -->

Frequently asked questions:


* [How can I quickly edit viewed note?](#how-can-i-quickly-edit-viewed-note)
* [How can I open notebook title section?](#how-can-i-open-notebook-title-section) <kbd>todo</kbd>
* [Why is not line starting with # turned into section when editing a note?](#why-is-not-line-starting-with---turned-into-section-when-editing-a-note)
* [How can I change font size/color/... in HTML preview?](#how-can-i-change-font-size-color-----in-html-preview) <kbd>todo</kbd>
* [How can I open Markdown file in MindForger?](#how-can-i-open-markdown-file-in-mindforger) <kbd>todo</kbd>
* [How can I open Markdown file in MindForger?](#how-can-i-open-markdown-file-in-mindforger) <kbd>todo</kbd>
* [How can I manually add Markdown files ot MindForger repository?](#how-can-i-manually-add-markdown-files-ot-mindforger-repository) <kbd>todo</kbd>
# How can I open notebook title section? <!-- Metadata: type: Note; tags: todo; created: 2022-02-26 08:27:46; reads: 30; read: 2022-03-10 08:21:26; revision: 2; modified: 2022-03-10 08:21:15; -->
![Image](faq.title-section-edit.png)

Simply click notebook **name** above the note tree outline.
# How can I quickly edit viewed note? <!-- Metadata: type: Note; tags: todo,macos; created: 2022-02-26 08:27:46; reads: 32; read: 2022-03-10 08:21:33; revision: 3; modified: 2022-03-10 08:21:33; -->
**Double click** HTML preview to open note editor or use <kbd>Alt+n e</kbd> (menu `Note/Edit`).
# How can I stop Note HTML preview "bouncing" while editing its text? <!-- Metadata: type: Note; created: 2022-02-26 08:29:03; reads: 30; read: 2022-03-10 08:21:24; revision: 2; modified: 2022-02-26 08:30:12; -->
This is unfortunately know issue - you can get rid of it by disabling math expressions preview:

* go to menu `File`, `Preferences`
* click `Viewer` tab
* disable (uncheck) `math support`
# How can I open Markdown file in MindForger? <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 31; read: 2022-03-10 08:21:24; revision: 1; modified: 2022-02-26 08:27:46; -->

# How can I delete tag? <!-- Metadata: type: Note; created: 2022-03-10 08:21:07; reads: 8; read: 2022-03-10 08:21:24; revision: 2; modified: 2022-03-10 08:21:09; -->

# Why is not line starting with # turned into section when editing a note? <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 17; read: 2022-03-10 08:21:24; revision: 1; modified: 2022-02-26 08:27:46; -->
TL:DR use menu `Note/New`  to create a new section - "manual" section within section is intentionally **quoted**.

MindForger uses Markdown as a format for storing data, but it aims to do more. Therefore it splits Markdown file to sections and represents each section as **Note**: 

* MindForger shows Notes **outline** - tree of Notes on the left in Notebook view
* You can manipulate with sections (up/down/promote/demote/clone/refactor/...) from menu `Note`
* It offers associated sections (Notes) to the section being read/written
* ...

See also ![explanation](user-documentation.outliner-rules.png)
# How can I change font size/color/... in HTML preview? <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 9; read: 2022-02-26 08:31:04; revision: 1; modified: 2022-02-26 08:27:46; -->
See [Custom HTML Preview CSS](user-documentation.md#custom-html-preview-css).
# How can I manually add Markdown files to MindForger repository? <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 8; read: 2022-02-26 08:31:20; revision: 2; modified: 2022-02-26 08:31:20; -->

