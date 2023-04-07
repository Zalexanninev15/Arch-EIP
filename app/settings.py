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

from PySide6.QtWidgets import QVBoxLayout, QDialog, QRadioButton, QPushButton, QGridLayout, \
    QGroupBox, QHBoxLayout, QMessageBox
from PySide6.QtCore import Qt
from utilities import Config

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setFixedSize(340, 114)

        self.settings_button = QPushButton("Apply settings")
        self.settings_button.clicked.connect(self.btn_save_and_close)

        layout = QGridLayout(self)
        groupbox = QGroupBox("Export list type:", checkable=False)
        layout.addWidget(groupbox)
        layout.addWidget(self.settings_button)
        radiobox = QHBoxLayout()
        groupbox.setLayout(radiobox)
        self.export_as_text_list = QRadioButton("Normal")
        self.export_as_markdown_list = QRadioButton("Markdown")
        self.export_as_installation_script = QRadioButton("Installation script")
        radiobox.addWidget(self.export_as_text_list, alignment=Qt.AlignTop)
        radiobox.addWidget(self.export_as_markdown_list, alignment=Qt.AlignTop)
        radiobox.addWidget(self.export_as_installation_script, alignment=Qt.AlignTop)
        radiobox.addStretch()
        
        layout.setColumnStretch(1, 1)
        layout.setRowStretch(1, 1)
        self.setLayout(radiobox)

        list_type = Config.load_config_export_list_type()
        if (list_type == 1):
            self.export_as_text_list.setChecked(True)
        elif (list_type == 2):
            self.export_as_markdown_list.setChecked(True)
        elif (list_type == 3):
            self.export_as_installation_script.setChecked(True)
    
    def btn_save_and_close(self):
        if self.export_as_text_list.isChecked():
            Config.set_config(1)
        elif self.export_as_markdown_list.isChecked():
            Config.set_config(2)
        elif self.export_as_installation_script.isChecked():
            Config.set_config(3)
        msg_error = QMessageBox()
        msg_error.setIcon(QMessageBox.Information)
        msg_error.setText("Settings saved and applied!")
        msg_error.setWindowTitle("Information")
        msg_error.exec()
        self.accept()