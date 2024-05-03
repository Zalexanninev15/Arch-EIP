# Arch-EIP

<img src="./assets/icon.png" width="128">

 [![](https://img.shields.io/badge/platforms-Arch_Linux-1793D1.svg?logo=archlinux)](https://github.com/Zalexanninev15/Arch-EIP) 
  [![](https://img.shields.io/badge/platforms-Fedora-1793D1.svg?logo=fedora)](https://github.com/Zalexanninev15/Arch-EIP) 
 [![](https://img.shields.io/badge/written_on-Python-3776AB.svg?logo=python)](https://github.com/Zalexanninev15/Arch-EIP) 
 [![](https://img.shields.io/badge/release-v1.4-blue.svg)](https://github.com/Zalexanninev15/Arch-EIP) 
 [![](https://img.shields.io/github/last-commit/Zalexanninev15/Arch-EIP.svg)](https://github.com/Zalexanninev15/Arch-EIP/commits/master) 
 [![](https://img.shields.io/badge/license-GPLv3-ligthgreen.svg)](LICENSE) 
[![](https://img.shields.io/badge/Donate-FFDD00.svg?logo=buymeacoffee&logoColor=black)](https://teletype.in/@zalexanninev15/donate) 

## Screenshot

![Снимок экрана от 2024-05-03 13-24-33](https://github.com/Zalexanninev15/Arch-EIP/assets/51060911/6abdc59e-f105-432c-86c4-e14f68a776f5)

## Description

Script for exporting lists of installed packages in various package managers, for quick recovery of packages in approximately similar conditions of use. The installed flatpak, pamac, and grep utilities are recommended, but you can do without them (grep is critical only for Official). The script was tested on Nobara Linux and Manjaro. I have plans to support systems based on Debian and Ubuntu.

### Description (version 1.3-dev and older) 

> Script for exporting installed packages to list in Arch linux for Flatpack, AUR, Official and PIP (Python 3). Example [here](https://cloud.disroot.org/s/4K63rWKJZ9YDxcP) (from [my Telegram channel Fiery Linux](https://ttttt.me/FieryLinux) (RU), where I talk about my adventures and discoveries in OpenSource and Linux, which I became actively interested in 2023, [post with example](https://ttttt.me/FieryLinux/34)). To get packages, I use `flatpak`, `pamac` and `grep` to exclude unnecessary strings. All tests were performed on Manjaro Linux ([example](https://ttttt.me/Zalexanninev15_News/825))

## Package managers are supported

- Flatpack
- AUR (Arch Linux/Manjaro)
- Official (Arch Linux/Manjaro)
- PIP (Python 3)
- Cargo (Rust)
- DNF (Fedora/Nobara Linux)

## Usage

 ```bash 
 python ./main.py
 ```

The data files will be located in the script directory with the `txt` or `sh` extensions (depending on your choice).
