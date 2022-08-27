# FAQs <!-- Metadata: type: Outline; created: 2022-02-26 08:27:46; reads: 41; read: 2022-08-27 07:56:04; revision: 41; modified: 2022-08-27 07:56:04; importance: 0/5; urgency: 0/5; -->
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
# How can I open notebook title section? <!-- Metadata: type: Note; tags: todo; created: 2022-02-26 08:27:46; reads: 34; read: 2022-08-27 07:56:04; revision: 3; modified: 2022-08-27 07:56:04; -->
Image: `faq.title-section-edit.png`

Simply click notebook **name** above the note tree outline.
# How can I quickly edit viewed note? <!-- Metadata: type: Note; tags: todo,macos; created: 2022-02-26 08:27:46; reads: 36; read: 2022-08-27 07:55:33; revision: 3; modified: 2022-03-10 08:21:33; -->
**Double click** HTML preview to open note editor or use <kbd>Alt+n e</kbd> (menu `Note/Edit`).
# How can I stop Note HTML preview "bouncing" while editing its text? <!-- Metadata: type: Note; created: 2022-02-26 08:29:03; reads: 34; read: 2022-08-27 07:55:33; revision: 2; modified: 2022-02-26 08:30:12; -->
This is unfortunately know issue - you can get rid of it by disabling math expressions preview:

* go to menu `File`, `Preferences`
* click `Viewer` tab
* disable (uncheck) `math support`
# How can I open Markdown file in MindForger? <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 35; read: 2022-08-27 07:55:33; revision: 1; modified: 2022-02-26 08:27:46; -->

# How can I delete tag? <!-- Metadata: type: Note; created: 2022-03-10 08:21:07; reads: 12; read: 2022-08-27 07:55:33; revision: 2; modified: 2022-03-10 08:21:09; -->

# Why is not line starting with # turned into section when editing a note? <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 21; read: 2022-08-27 07:55:32; revision: 1; modified: 2022-02-26 08:27:46; -->
TL:DR use menu `Note/New`  to create a new section - "manual" section within section is intentionally **quoted**.

MindForger uses Markdown as a format for storing data, but it aims to do more. Therefore it splits Markdown file to sections and represents each section as **Note**: 

* MindForger shows Notes **outline** - tree of Notes on the left in Notebook view
* You can manipulate with sections (up/down/promote/demote/clone/refactor/...) from menu `Note`
* It offers associated sections (Notes) to the section being read/written
* ...

See also ![explanation](user-documentation.outliner-rules.png)
# How can I change font size/color/... in HTML preview? <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 13; read: 2022-08-27 07:55:32; revision: 1; modified: 2022-02-26 08:27:46; -->
See [Custom HTML Preview CSS](user-documentation.md#custom-html-preview-css).
# How can I manually add Markdown files to MindForger repository? <!-- Metadata: type: Note; created: 2022-02-26 08:27:46; reads: 10; read: 2022-08-27 07:55:31; revision: 2; modified: 2022-02-26 08:31:20; -->

