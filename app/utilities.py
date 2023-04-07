#!/usr/bin/env python3

# Script with GUI for exporting installed packages to list in Arch linux for Flatpack, AUR, Official and PIP (Python 3)
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

from PySide6.QtWidgets import QMessageBox
import subprocess
import tomli

class ExportClass():
    def write_to_file(commands, file):
        file_path = f"{file}.txt"
        try:
            with open(file_path, "w") as f:
                print(subprocess.run(commands, shell=True, stdout=f, text=True))
        except Exception as e:
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Critical)
            msg_error.setText(f"Error: {e}")
            msg_error.setWindowTitle("Error")
            msg_error.exec()

    def export(checked):
        if checked[0]:
            flatpak = 'flatpak list --app --columns=name --columns=application'
            ExportClass.write_to_file(flatpak, "Flatpak")
        if checked[1]:
            aur = 'pamac list --foreign'
            ExportClass.write_to_file(aur, "AUR")
        if checked[2]:
            official = 'pamac list --installed | grep -v AUR'
            ExportClass.write_to_file(official, "Official")
        if checked[3]:
            pip = 'pip3 list --format=columns'
            ExportClass.write_to_file(pip, "PIP")

class Config():
    def load_config_export_list_type():
        with open('settings.toml', 'rb') as f:
            settings_dict = tomli.load(f)
            return settings_dict["APP"]["export_list_type"]
        
    def set_config(export_list_type):
        with open('settings.toml', "w") as f:
            f.write(f"[APP]\nexport_list_type = {export_list_type}")