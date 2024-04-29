#!/usr/bin/env python3

<<<<<<< Updated upstream
# Script for exporting installed packages to list (Markdown) in Arch linux for Flatpack, AUR, Official and PIP (Python 3)
# Copyright (C) 2023 Zalexanninev15
=======
# Script for exporting installed packages to list in Arch linux for Flatpack, AUR, Official and PIP (Python 3)
# Copyright (C) 2023-2024 Zalexanninev15
>>>>>>> Stashed changes

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

def write_to_file(commands, file):
    with open(f"{file}.txt", "w") as f:
        subprocess.run(commands, shell=True, stdout=f, text=True)

print('''Arch-EIP  Copyright (C) 2023  Zalexanninev15
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.''')

print("\nArch-EIP v1.4 (Flatpak+AUR+Official+PIP+Cargo) by Zalexanninev15\nGitHub: https://github.com/Zalexanninev15/Arch-EIP\n")

print("[*] Working (4 steps)...\n")

print('[!] Step 1. Flatpak')
flatpak = 'flatpak list --app --columns=name --columns=application'
write_to_file(flatpak, "Flatpak")

print('[!] Step 2. AUR')
aur = 'pamac list --foreign'
write_to_file(aur, "AUR")

print('[!] Step 3. Official')
official = 'pamac list --installed | grep -v AUR'
write_to_file(official, "Official")

print('[!] Step 4. PIP (Python 3)')
pip3 = 'pip3 list'
write_to_file(pip3, "PIP")

print('\n[+] Done! All installed packages are written in the files \"Flatpak.txt\", \"AUR.txt\", \"Official.txt\" and \"PIP.txt\"')
