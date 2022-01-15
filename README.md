# MindForger Documentation Repository
This **private** repository is where MindForger documentation is written. The content 
of this repository is processed as follows:

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
