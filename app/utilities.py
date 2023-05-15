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
import os

class ExportClass():
    def write_to_file(commands, file):
        file_path = f"{os.path.abspath(os.path.dirname(__file__))}/output/{file}.txt"
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
        print(f"Script path: {os.path.abspath(os.path.dirname(__file__))}")
        if not os.path.exists(f"{os.path.abspath(os.path.dirname(__file__))}/output"):
            os.mkdir(f"{os.path.abspath(os.path.dirname(__file__))}/output") 
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

class ExportTypeClass():
    pass

class ConfigClass():
    def load_config_export_list_type():
        with open('settings.toml', 'rb') as f:
            settings_dict = tomli.load(f)
            return settings_dict["APP"]["export_list_type"]
        
    def load_config_qt_class():
        with open('settings.toml', 'rb') as f:
            settings_dict = tomli.load(f)
            return [settings_dict["Qt"]["auto_screen_scale_factor"], 
                    settings_dict["Qt"]["scale_factor"], 
                    settings_dict["Qt"]["enable_high_dpi"],
                    settings_dict["Qt"]["use_native_theme_on_kde"],
                    settings_dict["Qt"]["try_to_use_native_theme_on_gnome"]]
        
    def set_config(export_list_type, use_native_theme_on_kde):
        with open('settings.toml', "w") as f:
            f.write("[APP]\n"
                    f"export_list_type = {export_list_type}\n\n"
                    f"[Qt]\n"
                    f"auto_screen_scale_factor = 1\n"
                    f"scale_factor = 100\n"
                    f"enable_high_dpi = true\n"
                    f"use_native_theme_on_kde = {use_native_theme_on_kde}\n"
                    f"try_to_use_native_theme_on_gnome = true")