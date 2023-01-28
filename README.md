# Arch-EIP

 [![](https://img.shields.io/badge/platforms-Arch_Linux-1793D1.svg?logo=archlinux)](https://github.com/Zalexanninev15/Arch-EIP) 
 [![](https://img.shields.io/badge/written_on-Python-3776AB.svg?logo=python)](https://github.com/Zalexanninev15/Arch-EIP) 
 [![](https://img.shields.io/badge/release-v1.1-blue.svg)](https://github.com/Zalexanninev15/Arch-EIP) 
 [![](https://img.shields.io/github/last-commit/Zalexanninev15/Arch-EIP.svg)](https://github.com/Zalexanninev15/Arch-EIP/commits/master) 
 [![](https://img.shields.io/badge/license-GPLv3-ligthgreen.svg)](LICENSE) 
 [![](https://img.shields.io/badge/donate-Buy_Me_a_Coffee-F94400.svg)](https://zalexanninev15.jimdofree.com/buy-me-a-coffee) 

## Description 

Script for exporting installed packages to list (Markdown) in Arch linux for Flatpack, AUR, Official. Example [here](https://cloud.disroot.org/s/4K63rWKJZ9YDxcP) (from [my Telegram channel PingvinusFun](https://ttttt.me/pingvinusfun) (RU), where I talk about my adventures and discoveries in OpenSource and Linux, which I became actively interested in 2023, [post with example](https://ttttt.me/pingvinusfun/34)). To get packages, I use `flatpak`, `pamac` and `grep` to exclude unnecessary strings. All tests were performed on Manjaro Linux

## Usage

Do the following in terminal or just launch with a mouse click (or how many of them you need to produce 😉)

 ```bash 
 python ./script.py
 ```
 The packages of each type of package will be written to the appropriate text file: `Flatpak.txt`, `AUR.txt`, `Official.txt`
