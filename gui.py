#!/usr/bin/env python3

# Script with GUI for exporting installed packages to list (Markdown) in Arch linux for Flatpack, AUR, Official and PIP (Python 3)
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

import os
import subprocess
from PySide6.QtWidgets import QApplication, QSizePolicy, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, \
    QDialog, QMessageBox, QProgressBar, QDialogButtonBox, QCheckBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QThread, Signal, Qt

version = "1.3-dev1"
version_console = "1.2"
checked = []

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About")
        self.setFixedSize(340, 170)

        label = QLabel(self)
        label.setTextFormat(Qt.RichText)
        label.setText("Arch-EIP GUI<br>"
                      f"<b>GUI version:</b> {version}<br>"
                      f"<b>Console version:</b> {version_console}<br>"
                      "<b>Author:</b> <a href=\"https://github.com/Zalexanninev15\">Zalexanninev15</a> <a href=\"mailto:mail@htmlacademy.ru\"><blue.shark@disroot.org></a><br>"
                      "<b>License:</b> GNU General Public License v3.0 (GPLv3)<br>"
                      "<b>GitHub:</b> <a href=\"https://github.com/Zalexanninev15/Arch-EIP\">https://github.com/Zalexanninev15/Arch-EIP</a>")
        label.setOpenExternalLinks(True)
        label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        label.setWordWrap(True)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok, self)
        button_box.accepted.connect(self.accept)

        main_layout = QVBoxLayout()
        main_layout.addWidget(label)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)

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

def export():
    if checked[0]:
        flatpak = 'flatpak list --app --columns=name --columns=application'
        write_to_file(flatpak, "Flatpak")
    if checked[1]:
        aur = 'pamac list --foreign'
        write_to_file(aur, "AUR")
    if checked[2]:
        official = 'pamac list --installed | grep -v AUR'
        write_to_file(official, "Official")
    if checked[3]:
        pip = 'pip3 list --format=columns'
        write_to_file(pip, "PIP")

class LongTermOperationThread(QThread):
    progress_updated = Signal(int)
    operation_done = Signal()
    def run(self):
        export()
        self.operation_done.emit()
        
class ExportDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("Arch-EIP GUI")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(340, 135)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.ex_label = QLabel("What needs to be exported?")
        self.ex_label.setAlignment(Qt.AlignCenter)
        self.ex_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.flatpak_checkbox = QCheckBox("Flatpak")
        self.aur_checkbox = QCheckBox("AUR")
        self.official_checkbox = QCheckBox("Official")
        self.pip_checkbox = QCheckBox("PIP")

        self.export_button = QPushButton("Export")
        self.export_button.clicked.connect(self.btn_export)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)

        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.about)

        checkboxes_layout = QHBoxLayout()
        checkboxes_layout.addWidget(self.flatpak_checkbox)
        checkboxes_layout.addWidget(self.aur_checkbox)
        checkboxes_layout.addWidget(self.official_checkbox)
        checkboxes_layout.addWidget(self.pip_checkbox)
        down_layout = QHBoxLayout()
        down_layout.addWidget(self.progress_bar)
        down_layout.addWidget(self.about_button)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.ex_label)
        main_layout.addLayout(checkboxes_layout)
        main_layout.addWidget(self.export_button)
        main_layout.addLayout(down_layout)
        self.setLayout(main_layout)

        self.operation_thread = LongTermOperationThread()
        self.operation_thread.operation_done.connect(self.operation_done, Qt.QueuedConnection)

    def about(self):
        about_dialog = AboutDialog()
        about_dialog.exec()

    def operation_done(self):
        msg_success = QMessageBox()
        msg_success.setIcon(QMessageBox.Information)
        msg_success.setText("List of installed packages exported!")
        msg_success.setWindowTitle("Export completed!")
        msg_success.exec()
        self.progress_bar.setValue(100)
        self.progress_bar.setMaximum(100)

    def btn_export(self):
        if not self.flatpak_checkbox.isChecked() and not self.aur_checkbox.isChecked() and not self.official_checkbox.isChecked() and not self.pip_checkbox.isChecked():
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Warning)
            msg_error.setText("You need to select at least one checkbox!")
            msg_error.setWindowTitle("Error")
            msg_error.exec()
            return
        else:
            checked.clear()
            checked.append(self.flatpak_checkbox.isChecked())
            checked.append(self.aur_checkbox.isChecked())
            checked.append(self.official_checkbox.isChecked())
            checked.append(self.pip_checkbox.isChecked())
            self.progress_bar.setMaximum(0)
            self.progress_bar.setValue(-1)
            self.operation_thread.start()


if __name__ == "__main__":
    app = QApplication()
    try:
        app.setStyle('Fusion')
        app.setPalette(PALETTE_DARK())
    except:
        pass
    is_plasma = 'plasma' in os.environ.get('DESKTOP_SESSION', '')
    try:
        ret = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.interface', 'color-scheme'], capture_output=True).stdout.decode('utf-8').strip().strip("'")
        if ret == 'prefer-dark':
            print("Dark theme selected")
        else:
            ret = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme'], capture_output=True).stdout.decode('utf-8').strip().strip("'").lower()
            if ret.endswith('-dark') or ret == 'HighContrastInverse':
                print("Dark theme selected")
    except:
        pass
    if not is_plasma:
        app.setStyle('Fusion')
        app.setPalette(QStyleFactory.create('fusion').standardPalette())
    app.setWindowIcon(QIcon("icon.png"))
    export_dialog = ExportDialog()
    export_dialog.setWindowTitle(f"Arch-EIP GUI")
    export_dialog.show()
    app.exec()
