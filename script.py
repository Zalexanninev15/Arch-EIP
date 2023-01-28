#!/usr/bin/env python3

# Script for exporting installed packages to list (Markdown) in Arch linux for Flatpack, AUR, Official
# Copyright (C) 2023 Zalexanninev15

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import subprocess

def console(commands, file):
    subprocess.run(commands, shell=True, stdout=file, text=True)

print('''Arch-EIP  Copyright (C) 2023  Zalexanninev15
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.''')
print("\nArch-EIP v1.1.0.1 (Flatpak+AUR+Official) by Zalexanninev15")
print("GitHub: https://github.com/Zalexanninev15/Arch-EIP\n")

print("[*] Working (3 steps)...\n")

print('[!] Step 1. Flatpak')
flatpak = 'flatpak list --app --columns=name --columns=application'
with open("Flatpak.txt", "w") as f:
    console(flatpak, f)

print('[!] Step 2. AUR')
aur = 'pamac list --foreign'
with open("AUR.txt", "w") as f:
    console(aur, f)

print('[!] Step 3. Official')
official = 'pamac list --installed | grep -v AUR'
with open("Official.txt", "w") as f:
    console(official, f)
    
print('\n[+] Done! All installed packages are written in the files \"Flatpak.txt\", \"AUR.txt\", \"Official.txt\"')
