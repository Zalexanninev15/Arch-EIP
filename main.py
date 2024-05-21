#!/usr/bin/env python3

# Script for exporting installed packages to list in Arch linux for Flatpack, AUR, Official and PIP (Python 3)
# Copyright (C) 2023-2024 Zalexanninev15

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
import os
from pathlib import Path

output_dir = ''

def write_to_file(commands, file, is_bash):
    if (is_bash):
        ext = 'sh'
    else:
        ext = 'txt'
    file_path = os.path.join(output_dir, f"{file}.{ext}")
    with open(file_path, "w") as f:
        subprocess.run(commands, shell=True, stdout=f, text=True)
    if (os.stat(file_path).st_size == 0):
        os.remove(file_path)
        print('Status: Recording error, because no text for recording was found!')
    else:
        print('Status: Export completed successfully!')


print('''Arch-EIP  Copyright (C) 2023-2024  Zalexanninev15
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.''')

print("\nArch-EIP v1.4 (Flatpak+AUR+Official+PIP+Cargo+DNF) by Zalexanninev15\nGitHub: https://github.com/Zalexanninev15/Arch-EIP\n")

print("Step 1. Choose what to export:")
print("1. All")
print("2. Choose individually")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    export_all = True
else:
    export_all = False
    export_choices = []

    print("\nSelect what to export.")
    print("1. Flatpak")
    print("2. AUR (Arch Linux/Manjaro) [ONLY TEXT FILE]")
    print("3. Official (Arch Linux/Manjaro) [ONLY TEXT FILE]")
    print("4. PIP (Python 3) [ALl packages]")
    print("5. Cargo (Rust) [Tools as packages]")
    print("6. DNF (Fedora/Nobara Linux)")
    print("7. APT (Debian/Ubuntu) [In developing]")

    while True:
        choice = input("\nEnter the corresponding number (one at a time, then you need to press Enter and enter the next one) or 'q' to finish: ")
        if choice == "q":
            break
        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
            export_choices.append(int(choice))
        else:
            print("Invalid choice. Please try again.")

format_bash = input(
    "\nDo you want to generate a script for quick installation (.sh)? (y/n): ").lower() == "y"

print("")

current_dir = os.getcwd()
output_dir = os.path.join(current_dir, "output")
if not os.path.exists(output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

if export_all or 1 in export_choices:
    print('- Flatpak')
    if (format_bash):
        flatpak = "echo '#!/bin/bash'\"\nflatpak install \"$(flatpak list --app --columns=application | xargs echo -n)"
    else:
        flatpak = 'flatpak list --app --columns=name --columns=application'
    write_to_file(flatpak, "Flatpak", format_bash)
    
if export_all or 2 in export_choices:
    print('- AUR [ONLY TEXT FILE]')
    aur = 'pamac list --foreign'
    write_to_file(aur, "AUR", format_bash)

if export_all or 3 in export_choices:
    print('- Official [ONLY TEXT FILE]')
    official = 'pamac list --installed | grep -v AUR'
    write_to_file(official, "Official", format_bash)

if export_all or 4 in export_choices:
    print('- PIP [ALl packages]')
    if (format_bash):
        pip3 = "echo '#!/bin/bash'\"\npip install \"$(pip list --format freeze | sed 's/==.*//' | xargs echo -n)"
    else:
        pip3 = 'pip3 list --format=columns'
    write_to_file(pip3, "PIP", format_bash)

if export_all or 5 in export_choices:
    print('- Cargo [Tools as packages]')
    if (format_bash):
        cargo = "echo '#!/bin/bash'\"\ncargo install \"$(cat /home/$USER/.cargo/.crates2.json | jq -r '.installs | keys[] | split(\" \")[0]' | xargs echo -n)"
    else:
        cargo = "cat /home/$USER/.cargo/.crates2.json | jq -r '.installs | keys[] | split(\" \")[0]'"
    write_to_file(cargo, "Cargo", format_bash)

if export_all or 6 in export_choices:
    print('- DNF')
    if (format_bash):
        dnf = "echo '#!/bin/bash'\"\nsudo dnf install \"$(rpm --query --all --queryformat '%{NAME} ' | xargs echo -n)"
    else:
        dnf = "rpm --query --all --queryformat '%{NAME}[%{ARCH}] %{VERSION} — %{SUMMARY}\n'"
    write_to_file(dnf, "DNF", format_bash)
    
if export_all or 7 in export_choices:
    print('- APT [In developing]')
    apt = ''
    write_to_file(apt, "APT", format_bash)

print('\nDone! Lists of installed packages are written in the output folder!')
