# Installation <!-- Metadata: type: Outline; created: 2018-03-20 16:19:07; reads: 1577; read: 2026-09-22 18:25:56; revision: 1577; modified: 2026-09-22 18:25:56; importance: 3/5; urgency: 3/5; -->
Install:

* [macOS](#macos)
* [Windows](#windows)
* [WSL](#wsl)
* [Snap](#snap)
* [Flatpak](#flatpak)
* [Ubuntu](#ubuntu)
* [Debian](#debian)
* [Fedora](#fedora)
* [FreeBSD](#freebsd)
* [Arch Linux](#arch-linux)
* [NixOS](#nixos-)
* [openSUSE](#opensuse)

Build:

* [build on macOS](#build-on-macos)
* [build on Windows](#build-on-windows)
* [build on WSL](#build-on-wsl)
* [build on Ubuntu](#build-on-ubuntu)
* [build on Debian](#build-on-debian)
* [build on Fedora](#build-on-fedora)
* [build on Gentoo](#build-on-gentoo)
* [build on NixOS](#build-on-nixos)
* [build and run container](#build-and-run-in-container)

Configure:

* [Appearance and themes](#appearance-and-themes)
* [Custom HTML Preview CSS](#custom-html-preview-css)
* [Spell check](#spell-check)
* [Think vs. Sleep mode](#think-vs--sleep-mode)

Package for a new distribution or OS:

* [download tarball](https://github.com/dvorka/mindforger/releases)

Look up:

* [release](RELEASES.md)
* [change](RELEASES.md#changelog)
# Install a package <!-- Metadata: type: Note; created: 2018-04-24 14:32:49; reads: 89; read: 2026-09-22 18:24:03; revision: 20; modified: 2022-01-30 17:15:40; -->
Install MindForger using a package.

If your operating system or distribution is not listed below, then check [packages repository](https://pkgs.org/search/?q=mindforger]) for Linux and Unix.
## macOS <!-- Metadata: type: Note; tags: macos; created: 2018-06-12 19:47:21; reads: 104; read: 2026-09-22 18:24:03; revision: 13; modified: 2021-12-31 10:09:00; -->
Install MindForger on macOS either using `brew` or by downloading `.dmg`.

**Homebrew**

Install MindForger using [HomeBrew](https://brew.sh):

```
brew install mindforger
```

**Disk iMaGe**

Install MindForger using `.dmg`:

* [download .dmg](https://github.com/dvorka/mindforger/releases) from [GitHub releases](https://github.com/dvorka/mindforger/releases)

Install `.dmg`:

* Open/mount `.dmg`
* Drag and drop/copy `mindforger` from `.dmg` to `Applications`
* Run `MindForger`

MindForger creates copy of the documentation in your home directory (`~/mindforger-repository`) and opens it as default repository.
## Windows <!-- Metadata: type: Note; tags: windows; created: 2019-02-16 09:43:18; reads: 81; read: 2026-09-22 18:24:03; revision: 6; modified: 2020-03-08 17:03:09; -->
Install MindForger using installer.

* Download installer executable from https://github.com/dvorka/mindforger/releases (or try [nightly build](https://ci.appveyor.com/project/dvorka/mindforger/build/artifacts))
* Run installer.

## WSL <!-- Metadata: type: Note; tags: windows; created: 2018-07-11 15:40:38; reads: 107; read: 2026-09-22 18:24:04; revision: 9; modified: 2020-03-08 17:03:04; -->
Install [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) (WSL) and check that you have Ubuntu 16.04 or newer:

```
lsb_release -a
  ...
  Release:        16.04
  Codename:       xenial
```
If not, then run `sudo do-release-upgrade`.

Install and start an X server for Windows like [Xming](https://sourceforge.net/projects/xming/).

---

Install MindForger from PPA. Add [my PPA](http://www.mindforger.com/debian) to Apt, trust [GPG key](http://www.mindforger.com/gpgpubkey.txt),
install MindForger and run it:

```sh
# add PPA to trusted repositories
sudo add-apt-repository ppa:ultradvorka/productivity

# update sources
sudo apt update

# install MindForger
sudo apt install mindforger

# run MindForger
DISPLAY=:0.0 mindforger
```
## Snap <!-- Metadata: type: Note; tags: linux; created: 2026-09-20 07:47:03; reads: 12; read: 2026-09-22 18:24:04; revision: 6; modified: 2026-09-22 17:57:35; -->
[Snap](https://snapcraft.io/docs) is a self-contained package which runs on all major Linux distros. There are the following MindForger Snap distributions:

* [SnapCraft.io](https://snapcraft.io/mindforger) package which uses strict confinement.
* **Classic** confinement package downloadable from [GitHub Releases](https://github.com/dvorka/mindforger/releases) page.

Both packages require `snapd` - install it (if it is not installed already) by following
the official guide for your distribution:

* [Installing snapd](https://snapcraft.io/docs/installing-snapd)

**Downloadable `.snap` package**

The `.snap` package attached to every [GitHub release](https://github.com/dvorka/mindforger/releases)
uses **classic** confinement. Unlike the strictly confined
[SnapCraft.io](https://snapcraft.io/mindforger) package it has full access to the host,
therefore it reads and writes your Markdown files and its configuration exactly like
the `.deb` or tarball installation does. Classic confinement packages cannot be
published to the Snap Store - the downloaded `.snap` file is installed directly
(sideloaded).

**Download**

Download `mindforger_<version>_amd64.snap` from the **Assets** section of the latest:

* [GitHub release](https://github.com/dvorka/mindforger/releases)

**Install**

Install the downloaded package with the `--dangerous` (sideloaded package which is not
signed by the Snap Store) and `--classic` (classic confinement) flags:

```sh
# example: mindforger_2.3.0_amd64.snap
sudo snap install --dangerous --classic ./mindforger_2.3.0_amd64.snap
```

Check the installation:

```sh
snap list mindforger
```

**Run**

Run MindForger either from the application menu (`MindForger`) or from the command line:

```sh
mindforger
```

... or:

```sh
snap run mindforger
```

On the **first** start MindForger creates a copy of the documentation and stencils in
your home directory (`~/mindforger-repository`) and opens it as the default repository.

**Data storage**

Classic confinement stores the data in the same location as any other MindForger
installation - your notebooks are not locked inside the snap:

```
~/mindforger-repository   ... default repository with your Markdown files
~/.mindforger.md          ... configuration
```

The strictly confined [SnapCraft.io](https://snapcraft.io/mindforger) package keeps both
under `~/snap/mindforger/common/` instead.

**Upgrade**

A sideloaded snap is not refreshed automatically (`snap refresh` has no Snap Store
revision to upgrade to). Download the newer `.snap` and install it the same way - your
repository and configuration are kept:

```sh
sudo snap install --dangerous --classic ./mindforger_<version>_amd64.snap
```

**Uninstall**

```sh
sudo snap remove mindforger
```

`snap remove` deletes the snap and its `~/snap/mindforger` directory -
`~/mindforger-repository` and `~/.mindforger.md` are **not** touched.


## Flatpak <!-- Metadata: type: Note; tags: linux; created: 2026-09-22 09:00:00; reads: 4; read: 2026-09-22 18:24:25; revision: 2; modified: 2026-09-22 18:24:25; -->
[Flatpak](https://flatpak.org) is a sandboxed package which runs on all major Linux
distributions. MindForger is distributed as a single-file `.flatpak` **bundle**
downloadable from the [GitHub Releases](https://github.com/dvorka/mindforger/releases)
page (it is not a Flathub hosted application).

**Prerequisites**

Install `flatpak` (if it is not installed already):

Ubuntu/Debian:

```sh
sudo apt update
sudo apt install flatpak
```

Fedora:

```sh
sudo dnf install flatpak
```

Arch Linux:

```sh
sudo pacman -S flatpak
```

openSUSE:

```sh
sudo zypper install flatpak
```

See [Flatpak setup](https://flatpak.org/setup/) for other distributions. Log out and
log in again after the **first** installation of Flatpak so that your desktop picks up
the applications installed by it.

**Download**

Download `mindforger-<version>.flatpak` from the **Assets** section of the latest:

* [GitHub release](https://github.com/dvorka/mindforger/releases)

**Install**

Install the downloaded bundle for your user (no `root` privileges are needed):

```sh
# example: mindforger-2.4.0.flatpak
flatpak install --user ./mindforger-2.4.0.flatpak
```

The bundle is self-contained - if the `org.kde.Platform` 5.15 runtime it needs is
missing, then Flatpak offers to download it from [Flathub](https://flathub.org)
automatically, you do **not** have to configure Flathub first. Should you prefer to add
the Flathub remote yourself:

```sh
flatpak remote-add --if-not-exists --user flathub https://flathub.org/repo/flathub.flatpakrepo
```

Check the installation:

```sh
flatpak info com.mindforger.MindForger
```

**Run**

Run MindForger either from the application menu (`MindForger`) or from the command line:

```sh
flatpak run com.mindforger.MindForger
```

On the **first** start MindForger creates a copy of the documentation and stencils in
your home directory (`~/mindforger-repository`) and opens it as the default repository.

**Data storage**

The sandbox is granted access to your home directory, therefore MindForger stores the
data in the same location as any other MindForger installation - your notebooks are not
locked inside the Flatpak:

```
~/mindforger-repository   ... default repository with your Markdown files
~/.mindforger.md          ... configuration
```

Markdown repositories on external/mounted media (`/media`, `/run/media`) can be opened
as well. The sandbox is also granted network access which is used by
[Wingman](USER_DOCUMENTATION.md#wingman) LLM providers.

**Upgrade**

A bundle installed from a file has no remote to be upgraded from (`flatpak update`
refreshes the runtime only). Download the newer `.flatpak` and install it the same way -
your repository and configuration are kept:

```sh
flatpak install --user --reinstall ./mindforger-<version>.flatpak
```

**Uninstall**

```sh
flatpak uninstall --user com.mindforger.MindForger
```

`~/mindforger-repository` and `~/.mindforger.md` are **not** removed by the uninstall -
delete them manually if you want to get rid of them.


## Ubuntu <!-- Metadata: type: Note; tags: linux; created: 2018-04-23 20:47:41; reads: 133; read: 2026-09-20 07:46:57; revision: 21; modified: 2020-03-08 17:02:23; -->
Install MindForger from **PPA**.
Add [my Lauchpad hosted PPA](https://launchpad.net/~ultradvorka/+archive/ubuntu/productivity) and install MindForger:

```
# add PPA to trusted repositories
sudo add-apt-repository ppa:ultradvorka/productivity

# update sources
sudo apt update

# install MindForger
sudo apt install mindforger
```
## Debian <!-- Metadata: type: Note; tags: linux; created: 2018-04-25 17:04:57; reads: 113; read: 2024-02-19 08:07:23; revision: 42; modified: 2023-11-12 13:00:51; -->
Install MindForger on [Debian](https://www.debian.org/) either by downloading `.deb` or from **PPA**.

Download `.deb` package for your Debian version from:

* [GitHub Releases](https://github.com/dvorka/mindforger/releases) **Assets** section

To install MindForger from the **PPA** add [my PPA](http://www.mindforger.com/debian) for **your Debian release** version, trust [GPG key](http://www.mindforger.com/gpgpubkey.txt) and
install MindForger - follow the instructions described in:

* http://www.mindforger.com/debian-ppa

For example Debian **"bookworm"**:

```bash
# add PPA to APT sources:
echo "deb http://www.mindforger.com/debian-ppa/bookworm bookworm main" | sudo tee /etc/apt/sources.list.d/mindforger.list

# import PPA's GPG key
wget -qO - http://www.mindforger.com/gpgpubkey.txt | sudo apt-key add -

# update sources
sudo apt update

# install MindForger
sudo apt install mindforger
```
## Fedora <!-- Metadata: type: Note; tags: linux; created: 2018-04-25 19:50:19; reads: 133; read: 2024-02-19 08:07:29; revision: 22; modified: 2020-03-08 17:02:33; -->
Install MindForger on [Fedora](https://getfedora.org/):

* [download RPM](https://github.com/dvorka/mindforger/releases) from GitHub releases

Install RPM:

```
sudo dnf install mindforger-MAJOR.MINOR.REVISION.rpm
```

## FreeBSD <!-- Metadata: type: Note; tags: unix; created: 2022-01-05 08:10:18; reads: 31; read: 2024-02-19 08:07:34; revision: 6; modified: 2022-01-05 08:13:26; -->
Install MindForger on [FreeBSD](https://www.freshports.org/deskutils/mindforger):

```
pkg install deskutils/mindforger
pkg install mindforger
```

([port commit](https://cgit.freebsd.org/ports/commit/?id=0c3409cfc37cfce255d0578b13805bf059a3be16))
## Arch Linux <!-- Metadata: type: Note; tags: linux; created: 2018-06-12 19:47:21; reads: 97; read: 2024-02-19 08:07:36; revision: 8; modified: 2020-03-08 17:02:45; -->
Install MindForger from Arch User Repository (AUR):

* https://aur.archlinux.org/packages/mindforger/

## NixOS <!-- Metadata: type: Note; tags: linux; created: 2022-01-05 07:36:42; reads: 41; read: 2024-02-19 08:07:38; revision: 3; modified: 2022-01-05 07:38:08; -->
Install [MindForger package](https://github.com/NixOS/nixpkgs/tree/master/pkgs/applications/editors/mindforger) on [NixOS](https://nixos.org/):

```
nix-env -i mindforger
```
## openSUSE <!-- Metadata: type: Note; tags: linux; created: 2020-01-21 08:08:06; reads: 97; read: 2024-02-19 08:07:41; revision: 5; modified: 2020-03-08 17:02:38; -->
Install MindForger on [openSUSE](https://www.opensuse.org/):

```
sudo zypper in opi
opi mindforger
```


# Build from source code <!-- Metadata: type: Note; created: 2018-03-20 16:19:07; reads: 113; read: 2024-02-19 08:08:06; revision: 8; modified: 2024-02-19 08:08:06; -->
Build MindForger from the source code.


## Build on macOS <!-- Metadata: type: Note; tags: macos; created: 2018-06-04 21:07:57; reads: 181; read: 2023-11-19 17:07:14; revision: 146; modified: 2022-01-05 07:57:27; -->
Build MindForger on macOS Sierra 10.12+.

Open `Terminal` and install/update [Xcode](https://developer.apple.com/) command line tools:

```sh
xcode-select --install
```

Install/update [HomeBrew](https://brew.sh) package manager:

```sh
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew doctor
```

Install build tools and dependencies:

```sh
brew install ccache
```

Download Qt from https://www.qt.io/download and in its online installer choose:

* `Qt/Qt 5.x.x`
    * latest available `5.x.x` (`Qt 5.9.9` or any newer Qt relese)
    * you can skip components like `Android` or `iOS` 
* `Developer and Designer Tools`
    * `Qt Creator`
    * `qmake`
    * `CMake`
    * `Qt Installer Framework`

Once Qt is installed you can use `~/Qt/MaintennanceTool.app` to add/remove Qt components.

Get [source code](https://github.com/dvorka/mindforger):

```sh
git clone https://github.com/dvorka/mindforger.git
git submodule init
git submodule update
```

There are two ways how to **build** MindForger Disk iMaGe package:

1. either using **scripts** from MindForger's GitHub repository:
    * `build/macos/mindforger-build.sh` which creates MindForger executable
    * `build/macos/dmg-package-build.sh` which creates Disk iMaGe `.dmg` package on top of binary executable build made by `mindforger-build.sh`
1. or using the **steps described below**

Add dependencies to `PATH`:

* fix paths: username, Qt and its components versions might be different
* add `PATH` modifications below to your `.bash_profile` and/or `.bashrc`
  or `.zshrc` depending on your shell (configuration)
* don't forget to apply changes e.g. using `. .bashr_profile`

```sh
# clang
export PATH="/Users/username/Qt/5.x.x/clang_64/bin:${PATH}"
# cmake
export PATH="${PATH}:/Users/username/Qt/Tools/CMake/CMake.app/Contents/bin"
# installer
export PATH="${PATH}:/Users/username/Qt/Tools/QtInstallerFramework/3.2/bin"
```

Get [source code](https://github.com/dvorka/mindforger):

```sh
git clone https://github.com/dvorka/mindforger.git
git submodule init
git submodule update
```

Build **dependencies**:

```sh
# build dependency: cmark-gfm
cd mindforger/deps/cmark-gfm
mkdir build && cd build
cmake -DCMARK_TESTS=OFF -DCMARK_SHARED=OFF ..
cmake --build .
```

Compile **sources** from repository **root** directory:

```sh
qmake -r mindforger.pro
# consider adding -j parameter with the number of CPU cores to use e.g. make -j 8
make
```

Optionally **install** MindForger:

```sh
cd app && cp -rvf mindforger.app /Applications
```

Install [documentation and stencils](https://github.com/dvorka/mindforger-repository):

```sh
# clone MindForger documentation repository to home directory - location and directory name matters
cd ~
git clone https://github.com/dvorka/mindforger-repository.git
```

Run MindForger either as application or using command line:

```
/Applications/mindforger.app/contents/MacOS/mindforger
```

---

Qt Creator **development environment** setup:

* start `Qt Creator` as application
* open project `mindforger.pro`
* configure project: `clang` kit, `debug` and `release` profiles
* menu `Build/Run qmake`
* menu `Build/Build all`
* menu `Build/Run`

Build `.dmg` **distribution**:

* start **terminal** session
* change to `mindforger/build/macos`
* run `build/macos/dmg-package-build.sh`
* check `.dmg` distro created in `mindforger/app/mindforger.dmg`
## Build on Windows <!-- Metadata: type: Note; tags: windows; created: 2019-02-03 17:11:52; reads: 196; read: 2023-11-19 17:07:14; revision: 125; modified: 2022-01-03 20:55:37; -->
Build MindForger on [Microsoft Windows](https://www.microsoft.com/en-us/windows).

Install build **tools**:

* Install [Microsoft Visual Studio IDE Community](https://visualstudio.microsoft.com/downloads/) edition.
    * Choose `Desktop development with C++` in installer.
* Install [Qt and Qt Creator IDE](https://www.qt.io/download)
    * Qt version - choose **latest** `5.x.x` Qt release available (must be `Qt 5.9.5` or newer, suggested `Qt 5.12.0` or newer)
    * Choose `Qt > Qt 5.x.x > QMSVC 2017 64-bit`
    * Choose `Qt > Qt 5.x.x > Qt WebEngine`
    * Choose `Qt > Developer and Designer tools > Qt Creator`
* Install `cmake`
* Install `patch`

Get **source code** from [GitHub](https://github.com/dvorka/mindforger):

* Create directory where you want to build MindForger e.g.
  `C:\Users\USER\mindforger-build`
  
```
# create and change to build directory
C: | cd %HOMEPATH% | mkdir mindforger-build | cd mindforger-build
# clone MindForger repository
git clone https://github.com/dvorka/mindforger.git
# update repository sub-modules
cd mindforger
git submodule init
git submodule update
```

* MindForger sources can be found in 
  `C:\Users\USER\mindforger-build\mindforger`

Build **dependencies**:

* build `cmark-gfm`: 

```
cd deps\cmark-gfm
mkdir build                                                                                                                                                                                                      
cd build                                                                                                                                                                                                         
cmake -G "Visual Studio 15 2017 Win64" -DCMAKE_CONFIGURATION_TYPES=Debug;Release -DCMARK_TESTS=OFF -DCMARK_SHARED=OFF ..
cmake --build . --config Release -- /m
```

Get default MindForger repository - **documentation and examples** (will be loaded on the first start):

```
# change to home directory
C: | cd %HOMEPATH%
# clone MindForger documentation
git clone https://github.com/dvorka/mindforger-repository.git
```

**Build** MindForger in Qt Creator:

1. Start Qt Creator
2. Open MindForger project:
    * `Welcome/Open project`
    * Choose `C:\Users\USER\mindforger-build\mindforger\mindforger.pro` as project file.
3. Choose kit:
    * `Desktop Qt 5.x.x MSVC2017 64bit`
4. Set build directory:
    * Set left toolbar's `Projects/Build Settings/Build directory` to `C:\Users\USER\mindforger-build\mindforger`
5. Set build configuration:
    * Set `Projects/Build Settings/Edit build configuration` choose `Release`
6. Build:
    * Menu `Build/Build All`

**Run** MindForger from Qt Creator:

* Menu `Build\Run`

Create **installer**:

* Install [JRSoftware](http://www.jrsoftware.org) [Inno Setup 5](http://www.jrsoftware.org/download.php/is-unicode.exe)
* Prepare development environment. Change path according to your Qt installation
    * Run `%QT_HOME%\5.x.x\msvc2017_64\bin\qtenv2.bat`
* Gather dependencies
    * `cd C:\Users\USER\mindforger-build\mindforger`
    * `%QT_HOME%\5.x.x\msvc2017_64\bin\windeployqt app\release\mindforger.exe  --dir app\release\bin --no-compiler-runtime`
* Build installer - **update** path to `vcredist_x64.exe` in the command below according to your setup:
    * `cd C:\Users\USER\mindforger-build\mindforger`
    * `"C:\Program Files (x86)\Inno Setup 5\ISCC.exe" /Qp /DVcRedistPath="c:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Redist\MSVC\14.16.27012\vcredist_x64.exe" build\windows\installer\mindforger-setup.iss` 
* MindForger **installer** can be found in `app\release\installer` folder.

To create **debug** version of MindForger and executable replace `debug` with `release` in the steps above and 
use `mindforger-setup-debug.iss` installer configuration.

## Build on WSL <!-- Metadata: type: Note; tags: windows; created: 2018-07-10 10:20:59; reads: 107; read: 2023-11-19 17:07:14; revision: 16; modified: 2022-01-03 20:54:01; -->
Build MindForger on [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) (WSL).

Install build tools:

```sh
sudo apt-get install build-essential zlib1g-dev libhunspell-dev libqt5webkit5-dev qttools5-dev-tools qt5-default ccache
```

Update `gcc` and `g++` to version 5 (at least):

```sh
# adds the the test toolchain which includes gcc-5 and g++5 
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install gcc-5 g++-5
# substitute gcc-5 for gcc and g++-5 for g++ (current version)
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 60 --slave /usr/bin/g++ g++ /usr/bin/g++-5
```

Get [source code](https://github.com/dvorka/mindforger):

```sh
# clone MindForger repository
git clone https://github.com/dvorka/mindforger.git
# update repository sub-modules
cd mindforger
git submodule init
git submodule update
```

Build **dependencies**:

```sh
# build cmark-gfm
cd mindforger/deps/cmark-gfm
mkdir build && cd build
cmake -DCMARK_TESTS=OFF -DCMARK_SHARED=OFF ..
cmake --build .
```

Compile and install from Git repository root directory:

```sh
qmake -r mindforger.pro
# consider speeding up compilation by increasing the number of CPU cores to use e.g. make -j8
make
sudo make install
```

Install [documentation and stencils](https://github.com/dvorka/mindforger-repository):

```sh
# clone MindForger documentation repository to home directory (location and directory name matters)
cd ~
git clone https://github.com/dvorka/mindforger-repository.git

# verify MindForger repository installation
ls mindforger-repository
  limbo  memory  mind  stencils
```

Run MindForger and start your XServer for Windows (e.g. [Xming](https://sourceforge.net/projects/xming/))

```sh
DISPLAY=:0.0 ./mindforger
```

## Build on Ubuntu <!-- Metadata: type: Note; tags: linux; created: 2018-03-20 16:19:07; reads: 210; read: 2023-11-19 18:33:09; revision: 67; modified: 2023-11-19 18:33:09; -->
Build MindForger on Ubuntu 16.04 or later.

Install package dependencies:

```sh
sudo apt-get install build-essential zlib1g-dev libhunspell-dev libqt5webkit5-dev qttools5-dev-tools qt5-default ccache cmake
```

Get [source code](https://github.com/dvorka/mindforger):

```sh
# clone MindForger repository
git clone https://github.com/dvorka/mindforger.git
# update repository sub-modules
cd mindforger
git submodule init
git submodule update
```

Build **dependencies**:

```sh
# build cmark-gfm
cd mindforger/deps/cmark-gfm
mkdir build && cd build
cmake -DCMARK_TESTS=OFF -DCMARK_SHARED=OFF ..
cmake --build .
```

**Compile** sources and **install** MindForger from Git repository root directory:

```sh
qmake -r mindforger.pro
# consider speeding up compilation by increasing the number of CPU cores to use e.g. make -j8
make
sudo make install
```

Install [documentation and stencils](https://github.com/dvorka/mindforger-repository):

```sh
# clone MindForger documentation repository to home directory (location and directory name matters)
cd ~
git clone https://github.com/dvorka/mindforger-repository.git
```

Run MindForger:

```
./mindforger
```

See also `mindforger/build/ubuntu/build-all-clean-system.sh`
## Build on Debian <!-- Metadata: type: Note; tags: linux; created: 2018-04-25 17:18:23; reads: 136; read: 2023-11-19 17:07:14; revision: 37; modified: 2023-11-05 13:38:33; -->
Build MindForger on Debian 9 (`stretch`) or later.

Install package dependencies:

```sh
sudo apt-get install build-essential zlib1g-dev libhunspell-dev libqt5webkit5-dev qttools5-dev-tools ccache cmake debhelper
```

Get [source code](https://github.com/dvorka/mindforger):

```
# clone MindForger repository
git clone https://github.com/dvorka/mindforger.git
# update repository sub-modules
git submodule init
git submodule update
```

Build dependencies:

```sh
# build cmark-gfm
cd mindforger/deps/cmark-gfm
mkdir build
# OPTIONAL step on certain Debian vesions: cmake -S . -B ./build
cd build
cmake -DCMARK_TESTS=OFF -DCMARK_SHARED=OFF ..
cmake --build .
```

Compile and install from Git repository root directory:

```sh
qmake -r mindforger.pro
# consider speeding up compilation by increasing the number of CPU cores to use e.g. make -j8
make
sudo make install
```

Install [documentation and stencils](https://github.com/dvorka/mindforger-repository):

```
# clone MindForger documentation repository to home directory (location and directory name matters)
cd ~
git clone https://github.com/dvorka/mindforger-repository.git
```

Run MindForger:

```
./mindforger
```
## Build on Fedora <!-- Metadata: type: Note; tags: linux; created: 2018-04-26 09:04:14; reads: 133; read: 2023-11-19 17:07:14; revision: 27; modified: 2022-01-05 07:57:02; -->
Build MindForger on Fedora.

Install package dependencies:

```sh
sudo dnf install zlib-devel hunspell-devel qt-devel qt5-devel ccache
```

Get source code:

```sh
# clone MindForger repository
git clone https://github.com/dvorka/mindforger.git
# update repository sub-modules                                            
git submodule init
git submodule update
```

Build dependencies:

```sh
# build cmark-gfm
cd mindforger/deps/cmark-gfm
mkdir build && cd build
cmake -DCMARK_TESTS=OFF -DCMARK_SHARED=OFF ..
cmake --build .
```

Compile and install from Git repository root directory:

```sh
qmake-qt5 -r mindforger.pro
# consider speeding up compilation by increasing the number of CPU cores to use e.g. make -j8
make
sudo make install
```

Install [documentation and stencils](https://github.com/dvorka/mindforger-repository):

```
# clone MindForger documentation repository to home directory (location and directory name matters)
cd ~
git clone https://github.com/dvorka/mindforger-repository.git
```

Run MindForger:

```
./mindforger
```
## Build on Gentoo <!-- Metadata: type: Note; tags: linux; created: 2022-01-05 07:52:13; reads: 43; read: 2023-11-04 23:12:50; revision: 8; modified: 2022-01-05 07:56:55; -->
Build MindForger on [Gentoo](https://www.gentoo.org/):

Install package dependencies.

Get source code:

```sh
# clone MindForger repository
git clone https://github.com/dvorka/mindforger.git
# update repository sub-modules                                            
git submodule init
git submodule update
```

Build dependencies:

```sh
# build cmark-gfm
cd mindforger/deps/cmark-gfm
mkdir build && cd build
cmake -DCMARK_TESTS=OFF -DCMARK_SHARED=OFF ..
cmake --build .
```

Compile and install from Git repository root directory:

```sh
qmake CONFIG+=mfwebengine -r mindforger.pro
# consider speeding up compilation by increasing the number of CPU cores to use e.g. make -j8
make
sudo make install
```

Install [documentation and stencils](https://github.com/dvorka/mindforger-repository):

```
# clone MindForger documentation repository to home directory (location and directory name matters)
cd ~
git clone https://github.com/dvorka/mindforger-repository.git
```

Run MindForger:

```
./mindforger
```
## Build on NixOS <!-- Metadata: type: Note; tags: linux; created: 2022-01-05 07:52:45; reads: 38; read: 2023-11-04 23:12:49; revision: 8; modified: 2022-01-05 07:56:49; -->
Build MindForger on [Gentoo](https://www.gentoo.org/):

Install package [dependencies](https://github.com/NixOS/nixpkgs/blob/master/pkgs/applications/editors/mindforger/default.nix).

Get source code:

```sh
# clone MindForger repository
git clone https://github.com/dvorka/mindforger.git
# update repository sub-modules                                            
git submodule init
git submodule update
```

Build dependencies:

```sh
# build cmark-gfm
cd mindforger/deps/cmark-gfm
mkdir build && cd build
cmake -DCMARK_TESTS=OFF -DCMARK_SHARED=OFF ..
cmake --build .
```

Compile and install from Git repository root directory:

```sh
qmake CONFIG+=mfwebengine -r mindforger.pro
# consider speeding up compilation by increasing the number of CPU cores to use e.g. make -j8
make
sudo make install
```

Install [documentation and stencils](https://github.com/dvorka/mindforger-repository):

```
# clone MindForger documentation repository to home directory (location and directory name matters)
cd ~
git clone https://github.com/dvorka/mindforger-repository.git
```

Run MindForger:

```
./mindforger
```


# Docker <!-- Metadata: type: Note; created: 2018-09-23 13:45:53; reads: 46; read: 2022-02-05 16:19:25; revision: 5; modified: 2018-09-23 13:49:01; -->
Run MindForger in Docker container.
## Build and run in container <!-- Metadata: type: Note; tags: docker; created: 2018-09-23 13:46:37; reads: 103; read: 2022-08-27 08:01:49; revision: 60; modified: 2020-03-08 17:04:07; -->
Build [Docker](https://www.docker.com/) image and run MindForger in Docker container.

Build image:

```
mkdir mindforger

# download Dockerfile
curl https://raw.githubusercontent.com/dvorka/mindforger/master/build/docker/mindforger/Dockerfile > mindforger/Dockerfile

# build image
docker build -t mindforger:latest mindforger
```

Run container:

```
# allow access to X server (UNSECURE, but simple):
xhost +local:root

# run image
docker run -it --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" mindforger:latest mindforger

# determine and remember container ID
docker ps -l -q > ~/.mindforger.docker
```

Run MindForger by starting container:

```
# start (stopped) container
docker start $(cat ~/.mindforger.docker)
```

Check also https://github.com/dvorka/mindforger/tree/master/build/docker for handy scripts.

# Nightly builds <!-- Metadata: type: Note; created: 2022-01-30 17:06:58; reads: 32; read: 2024-02-19 08:06:33; revision: 4; modified: 2022-03-10 08:47:54; -->
Nightly builds:

* [macOS .dmg](https://github.com/dvorka/mindforger/actions)
* [Windows installer](https://ci.appveyor.com/project/dvorka/mindforger/build/artifacts)
* [tarball](https://github.com/dvorka/mindforger/actions/workflows/build_ubuntu.yml)
# Configure <!-- Metadata: type: Note; created: 2022-01-30 18:02:50; reads: 72; read: 2024-02-19 08:07:02; revision: 5; modified: 2024-02-19 08:07:02; -->
MindForger can be configured either from UI:

* menu `Knowledge/Preferences`

... or using configuration file (while MindForger is **NOT** running):

* `~/.mindforger.md`

Review `.mindforger.md` for configuration option details and descriptions.


## Appearance and themes <!-- Metadata: type: Note; created: 2022-02-05 16:13:27; reads: 20; read: 2024-02-19 08:06:32; revision: 3; modified: 2022-02-05 16:18:48; -->

### Custom HTML Preview CSS <!-- Metadata: type: Note; created: 2022-01-30 18:02:50; reads: 63; read: 2024-02-19 08:06:32; revision: 5; modified: 2022-02-05 16:45:21; -->
If you want to change color, font size, rendering of HTML preview, then it can
be done using **custom CSS**.

You can either use your custom CSS - there is no UI for such change:

1. make sure MindForger is not running
1. download CSS you like https://github.com/dvorka/mindforger/tree/master/app/resources/qt/css (dark or light and choose `Raw`)
2. edit downloaded CSS file and change font size, ...
3. open `$HOME/.mindforger.md` and **change** path to your CSS, e.g.

```
...
* Markdown CSS theme: /home/USERNAME/my.css
...
```

This will ensure that CSS from given path will be loaded by HTML preview since the next time MindForger is started.
## Wingman preferences <!-- Metadata: type: Note; created: 2024-02-19 08:05:31; reads: 9; read: 2024-02-19 08:06:32; revision: 3; modified: 2024-02-19 08:06:00; -->
See [LLM provider configuration](USER_DOCUMENTATION.md#llm-provider-configuration)


## Spell check preferences <!-- Metadata: type: Note; created: 2021-12-22 20:04:34; reads: 63; read: 2024-02-19 08:06:32; revision: 10; modified: 2024-02-19 08:06:21; -->
MindForger's **spell check** implementation is based on [Hunspell](https://github.com/hunspell/hunspell).
### Spell check configuration on Linux <!-- Metadata: type: Note; created: 2021-12-22 20:07:03; reads: 60; read: 2024-02-19 08:06:32; revision: 20; modified: 2022-01-14 00:01:49; -->
Install [Hunspell](https://github.com/hunspell/hunspell):

```
sudo apt install hunspell
```

Download **vocabulary** for your language from:

* https://extensions.openoffice.org/en/project/english-dictionaries-apache-openoffice

**Install** vocabulary:

* extract `.oxt` archive downloaded from the URL above to get `.dict` and `.aff` files
* determine Hunspell's vocabulary search path by running:
```
hunspell -D
```
* copy downloaded (`.dict` and `.aff`) vocabulary files to one of 
  the directories on Hunspell's search path e.g. `/usr/share/hunspell`
### Spell check configuration on Windows <!-- Metadata: type: Note; created: 2021-12-22 20:07:15; reads: 44; read: 2024-02-19 08:06:32; revision: 17; modified: 2022-01-14 00:02:12; -->
[Hunspell](https://github.com/hunspell/hunspell) is included
in MindForger executable, therefore it does not have to be installed.

Download **vocabulary** for your language from:

* https://extensions.openoffice.org/en/project/english-dictionaries-apache-openoffice

**Install** vocabulary:

* extract `.oxt` archive downloaded from the URL above to get `.dict` and `.aff` files
* copy downloaded (`.dict` and `.aff`) vocabulary files to one of 
  the directories on Hunspell's search path:
```
C:\Users\<profile>\dictionaries
C:\Users\<profile>\Local Settings\dictionaries
C:\Users\<profile>\AppData\Local\dictionaries
```
## Think vs. Sleep mode <!-- Metadata: type: Note; created: 2022-01-30 18:02:50; reads: 49; read: 2024-02-19 08:06:31; revision: 6; modified: 2022-02-05 16:42:16; -->
MindForger can be either in **thinking** or **sleeping** mode:

* **Thinking** mode can be activated by checking menu item `Knowledge/Think` and it's also
  indicated by the `Thinking` indicator in main window status bar.
    * MindForger runs background mind-related computations/tasks that can be **CPU intensive**
    * MindForger suggests relevant notes as you browse/read/write
    * MindForger named-entity recognition model is loaded and enabled
    * ...
* **Sleeping** mode can be activated by unchecking menu item `Knowledge/Think` and it's also
  indicated by the `Sleeping` indicator in main window status bar.
    * MindForger runs **no** background mind-related computations/tasks i.e. it 
      does **not** consume any extra CPU power and does **not** show any async information

Switch thinking/sleeping mode based on whether you **need** mind features for the particular
repository or not - consider performance/CPU consumption vs features trade-off.
### AA poler preferences <!-- Metadata: type: Note; tags: todo; created: 2022-02-05 16:13:37; reads: 34; read: 2024-02-19 08:06:30; revision: 6; modified: 2024-02-19 08:06:30; -->

