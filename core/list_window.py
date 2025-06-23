from __future__ import annotations
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from .config import CSS_PATH, PASS_FILE
from .utils import load_encrypted_passwords


class PasswordListWindow(QWidget):
    def __init__(self, pmw_instance: 'PasswordManagerWindow'): # type: ignore
        super().__init__()
        self.setWindowTitle("Saved Passwords")
        self.setFixedSize(420, 400)
        self.setObjectName("password_list_window")
        self.pmw = pmw_instance

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(15)
        layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        title = QLabel("🔎 Saved Passwords")
        title.setObjectName("section_title")
        title.setAlignment(Qt.AlignCenter)

        self.txt_list = QTextEdit()
        self.txt_list.setReadOnly(True)
        self.txt_list.setObjectName("passwords_list")

        self.btn_reload = QPushButton("🔄 View Passwords")
        self.btn_reload.setObjectName("reload_button")
        self.btn_reload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reload.clicked.connect(self.show_passwords)

        layout.addWidget(title)
        layout.addWidget(self.txt_list)
        layout.addWidget(self.btn_reload)

        self.setLayout(layout)
        self.load_stylesheet()

    def load_stylesheet(self):
        try:
            with open(CSS_PATH, "r") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(f"Failed to load QSS file: {e}")
            
    def show_passwords(self):
        self.txt_list.clear()
        passwords = load_encrypted_passwords(PASS_FILE, self.pmw.old_fernet)
        for site, pw in passwords.items():
            self.txt_list.append(f"🌐 Site: {site}\n👤 Username: {pw[1]}\n🔑 Password: {pw[1]}\n")