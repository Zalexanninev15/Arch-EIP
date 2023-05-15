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

from PySide6.QtWidgets import QLabel, QVBoxLayout, QDialog, QDialogButtonBox
from PySide6.QtCore import Qt
from main import version

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About")
        self.setFixedSize(334, 162)

        label = QLabel(self)
        label.setTextFormat(Qt.RichText)
        label.setText("Arch-EIP GUI<br>"
                      f"<b>GUI version:</b> {version}<br>"
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