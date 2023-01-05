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
import markdown

def console(commands):
    return subprocess.run(commands, shell=True, capture_output=True, text=True)

print('''WebWordSearch  Copyright (C) 2023  Zalexanninev15
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.''')
print("\nArch-EIP v1.0 (flatpak+aur+official) by Zalexanninev15")
print("GitHub: https://github.com/Zalexanninev15/Arch-EIP\n")

print("[*] Working (4 steps)...\n")

print('[!] Step 1. Flatpack')
flatpak = 'flatpak list | grep -v freedesktop | grep -v KDE | grep -v GNOME | grep -v theme | column -t'
s1 = console(flatpak).stdout

print('[!] Step 2. AUR')
aur = 'pacman -Qem'
s2 = console(aur).stdout

print('[!] Step 3. Official')
official = 'comm -23 <(pacman -Qqett | sort | uniq) <(pacman -Qqg -g base-devel | sort | uniq)'
s3 = console(official).stdout

print('[!] Step 4. Write packages to file')
packages = ""
file_name = "installed_packages"
packages = f'# Flatpak:\n```{s1}```\n# AUR:\n```{s2}```\n# Official:\n```{s3}```'
with open(f"{file_name}.md", "w", encoding="utf-8") as fp:
    fp.write(packages)
    
print('\n[+] Done! All installed packages are written in the file "installed_packages.md"')
