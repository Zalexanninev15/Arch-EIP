# Arch-EIP

<img src="./icon.png" width="128">

 [![](https://img.shields.io/badge/platform-Arch_Linux-1793D1.svg?logo=archlinux)](https://github.com/Zalexanninev15/Arch-EIP)
 [![](https://img.shields.io/badge/platform-Fedora-1793D1.svg?logo=fedora)](https://github.com/Zalexanninev15/Arch-EIP)
 [![](https://img.shields.io/badge/written_on-Python-%233776AB.svg?logo=python)](https://github.com/Zalexanninev15/Arch-EIP)
 [![](https://img.shields.io/badge/release-v1.4-blue.svg)](https://github.com/Zalexanninev15/Arch-EIP)
 [![](https://img.shields.io/github/last-commit/Zalexanninev15/Arch-EIP.svg)](https://github.com/Zalexanninev15/Arch-EIP/commits/main)
 [![](https://img.shields.io/github/stars/Zalexanninev15/Arch-EIP.svg)](https://github.com/Zalexanninev15/Arch-EIP/stargazers)
[![](https://img.shields.io/github/forks/Zalexanninev15/Arch-EIP.svg)](https://github.com/Zalexanninev15/Arch-EIP/network/members)
[![](https://img.shields.io/github/issues/Zalexanninev15/Arch-EIP.svg)](https://github.com/Zalexanninev15/Arch-EIP/issues?q=is%3Aopen+is%3Aissue)
[![](https://img.shields.io/github/issues-closed/Zalexanninev15/Arch-EIP.svg)](https://github.com/Zalexanninev15/Arch-EIP/issues?q=is%3Aissue+is%3Aclosed)
 [![](https://img.shields.io/badge/license-GPLv3-ligthgreen.svg)](LICENSE)
 [![](https://img.shields.io/badge/Donate-FFDD00.svg?logo=buymeacoffee&logoColor=black)](https://z15.neocities.org/donate)

## Screenshot

![image](https://github.com/Zalexanninev15/Arch-EIP/assets/51060911/87af4b48-4be3-4519-a968-eb210763014a)

## Description

Script for exporting lists of installed packages in various package managers, for quick recovery of packages in approximately similar conditions of use. The installed flatpak, pamac, and grep utilities are recommended, but you can do without them (grep is critical only for Official). The script was tested on Nobara Linux and Manjaro. I have plans to support systems based on Debian and Ubuntu.

### Description (version 1.3-dev and older)

> Script for exporting installed packages to list in Arch linux for Flatpack, AUR, Official and PIP (Python 3). Example [here](https://cloud.disroot.org/s/4K63rWKJZ9YDxcP) (from [my Telegram channel Fiery Linux](https://t.me/FieryLinux) (RU), where I talk about my adventures and discoveries in OpenSource and Linux, which I became actively interested in 2023, [post with example](https://t.me/FieryLinux/34)). To get packages, I use `flatpak`, `pamac` and `grep` to exclude unnecessary strings. All tests were performed on Manjaro Linux ([example](https://t.me/MaxLife15/825)).

## Package managers are supported

- Flatpack
- AUR (Arch Linux/Manjaro)
- Official (Arch Linux/Manjaro)
- PIP (Python 3)
- Cargo (Rust)
- DNF (Fedora/Nobara Linux)
- APT (In developing)

## Usage

```bash
python3 ./main.py
```

The files with lists of installed packages will be placed in the output directory with the `txt` or `sh` extensions (depending on your choice).
