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


def write_to_file(commands, file, is_bash):
    if (is_bash):
        ext = 'sh'
    else:
        ext = 'txt'
    with open(f"{file}.{ext}", "w") as f:
        subprocess.run(commands, shell=True, stdout=f, text=True)
    if (os.stat(f"{file}.{ext}").st_size == 0):
        os.remove(f"{file}.{ext}")
        print('Status: Recording error, because no text for recording was found!')
    else:
        print('Status: Export completed successfully!')


print('''Arch-EIP  Copyright (C) 2023-2024  Zalexanninev15
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.''')

# Choosing what to export
print("\nArch-EIP v1.4-dev1 (Flatpak+AUR+Official+PIP+Cargo+DNF) by Zalexanninev15\nGitHub: https://github.com/Zalexanninev15/Arch-EIP\n")

# Step 1. Choosing what to export. All or choose many
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
    print("2. AUR (Arch Linux)")
    print("3. Official (Arch Linux)")
    print("4. PIP (Python 3)")
    print("5. Cargo (Rust)")
    print("6. DNF (Fedora)")

    while True:
        choice = input("\nEnter the corresponding number (one at a time, then you need to press Enter and enter the next one) or 'q' to finish: ")
        if choice == "q":
            break
        elif choice in ["1", "2", "3", "4", "5", "6"]:
            export_choices.append(int(choice))
        else:

# Step 2. File format selection: a list (.txt) or a script for quick installation (.sh)
format_bash = input(
    "\nDo you want to generate a script for quick installation (.sh)? (y/n): ").lower() == "y"

print("")

if export_all or 1 in export_choices:
    print('- Flatpak')
    if (format_bash):
        flatpak = "echo '#!/bin/bash'\"\nflatpak install \"$(flatpak list --app --columns=application | xargs echo -n)"
    else:
        flatpak = 'flatpak list --app --columns=name --columns=application'
    write_to_file(flatpak, "Flatpak", format_bash)
    
if export_all or 2 in export_choices:
    print('- AUR (Arch Linux) [ONLY TXT]')
    aur = 'pamac list --foreign'
    write_to_file(aur, "AUR", format_bash)

if export_all or 3 in export_choices:
    print('- Official (Arch Linux) [ONLY TXT]')
    official = 'pamac list --installed | grep -v AUR'
    write_to_file(official, "Official", format_bash)

if export_all or 4 in export_choices:
    print('- Step 4. PIP (Python 3)')
    if (format_bash):
        pip3 = "echo '#!/bin/bash'\"\npip install \"$(pip list --format freeze | sed 's/==.*//' | xargs echo -n)"
    else:
        pip3 = 'pip3 list --format=columns'
    write_to_file(pip3, "PIP", format_bash)

if export_all or 5 in export_choices:
    print('- Cargo (Rust) [In developing!]')
    cargo = ''
    write_to_file(cargo, "Cargo", format_bash)

if export_all or 6 in export_choices:
    print('- DNF (Fedora)')
    if (format_bash):
        dnf = "echo '#!/bin/bash'\"\nsudo dnf install \"$(rpm --query --all --queryformat '%{NAME} ' | xargs echo -n)"
    else:
        dnf = "rpm --query --all --queryformat '%{NAME}[%{ARCH}] %{VERSION} — %{SUMMARY}\n'"
    write_to_file(dnf, "Fedora DNF", format_bash)

print('\nDone! All installed packages are written in the files!')
