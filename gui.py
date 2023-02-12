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

import subprocess
from PySide6.QtWidgets import QApplication, QSizePolicy, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, \
    QLineEdit, QDialog, QMessageBox, QProgressBar, QDialogButtonBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer, QThread, Signal, Slot, Qt

version = "1.2-beta 1"
version_console = "1.2"


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About")
        self.setFixedSize(340, 180)

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
    with open(f"{file}.txt", "w") as f:
        subprocess.run(commands, shell=True, stdout=f, text=True)


class LongTermOperationThread(QThread):
    progress_updated = Signal(int)
    operation_done = Signal()

    def run(self):
        flatpak = 'flatpak list --app --columns=name --columns=application'
        write_to_file(flatpak, "Flatpak")
        aur = 'pamac list --foreign'
        write_to_file(aur, "AUR")
        official = 'pamac list --installed | grep -v AUR'
        write_to_file(official, "Official")
        pip3 = 'pip3 list'
        write_to_file(pip3, "PIP")
        self.operation_done.emit()


class ExportDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"Arch-EIP GUI")
        self.setWindowIcon(QIcon("icon.png"))
        width = 335
        height = 135
        self.setFixedSize(width, height)

        self.label = QLabel("Select a folder to save the list of installed packages:")
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.folder_line_edit = QLineEdit()
        self.folder_line_edit.setReadOnly(True)

        self.select_folder_button = QPushButton("Select Folder")
        self.select_folder_button.clicked.connect(self.select_folder)

        self.export_button = QPushButton("Export")
        self.export_button.clicked.connect(self.export)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)

        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.about)

        self.folder_line_edit = QLineEdit()
        self.folder_line_edit.setReadOnly(True)

        folder_layout = QHBoxLayout()
        folder_layout.addWidget(self.folder_line_edit)
        folder_layout.addWidget(self.select_folder_button)
        down_layout = QHBoxLayout()
        down_layout.addWidget(self.progress_bar)
        down_layout.addWidget(self.about_button)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addLayout(folder_layout)
        main_layout.addWidget(self.export_button)
        main_layout.addLayout(down_layout)
        self.setLayout(main_layout)

        self.operation_thread = LongTermOperationThread()
        self.operation_thread.operation_done.connect(self.operation_done, Qt.QueuedConnection)

    def about(self):
        about_dialog = AboutDialog()
        about_dialog.exec()

    def select_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_name = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)
        if folder_name:
            self.folder_line_edit.setText(folder_name)

    def operation_done(self):
        msg_success = QMessageBox()
        msg_success.setIcon(QMessageBox.Information)
        msg_success.setText("List of installed packages\nFlatpak, Aur, Official and PIP exported!")
        msg_success.setWindowTitle("Export completed")
        msg_success.exec()
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)

    def export(self):
        folder_name = self.folder_line_edit.text()
        if not folder_name:
            msg_error = QMessageBox()
            msg_error.setIcon(QMessageBox.Warning)
            msg_error.setText("Please select a folder to save the list of installed packages!")
            msg_error.setWindowTitle("Folder is not selected")
            msg_error.exec()
            return

        self.progress_bar.setMaximum(0)
        self.progress_bar.setValue(-1)
        self.operation_thread.start()


if __name__ == "__main__":
    app = QApplication()
    app.setWindowIcon(QIcon("icon.png"))
    export_dialog = ExportDialog()
    export_dialog.setWindowTitle(f"Arch-EIP GUI")
    export_dialog.show()
    app.exec()
