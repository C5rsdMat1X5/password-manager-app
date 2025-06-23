from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from .login_window import LogInWindow
from .utils import check_if_first, create_pass, read_pass
from .config import SIGNUP_FILE, KEY_FILE, CSS_PATH
import os


class StartUp:
    def __init__(self):
        self.window = None

    def run(self, cpw):
        password = read_pass(SIGNUP_FILE, KEY_FILE)
        if password is None and os.path.exists(SIGNUP_FILE):
            os.remove(SIGNUP_FILE)

        if not check_if_first(SIGNUP_FILE) and not cpw:
            login_window = LogInWindow()
            login_window.load_passwords()
            login_window.show()
            self.window = login_window
        else:
            signup_window = self.build_signup_window()
            signup_window.show()
            self.window = signup_window

    def build_signup_window(self):
        class SignUpWindow(QWidget):
            def __init__(self):
                super().__init__()
                self.login_window = LogInWindow()
                self.setWindowTitle("Crear Contraseña - Password Manager")
                self.setFixedSize(420, 400)
                self.setObjectName("login_window")

                main_layout = QVBoxLayout(self)
                main_layout.setAlignment(Qt.AlignCenter)

                self.lbl_title = QLabel("🛡️ Crea tu Contraseña Maestra")
                self.lbl_title.setAlignment(Qt.AlignCenter)
                self.lbl_title.setObjectName("app_title")

                self.lbl_subtitle = QLabel(
                    "Tu seguridad comienza aquí. Elige una contraseña segura."
                )
                self.lbl_subtitle.setAlignment(Qt.AlignCenter)
                self.lbl_subtitle.setObjectName("app_subtitle")

                container = QWidget()
                container.setObjectName("login_container")
                container_layout = QVBoxLayout(container)
                container_layout.setSpacing(20)
                container_layout.setContentsMargins(30, 30, 30, 30)
                container_layout.setAlignment(Qt.AlignCenter)

                self.input_pwd = QLineEdit()
                self.input_pwd.setEchoMode(QLineEdit.Password)
                self.input_pwd.setPlaceholderText("Escribe una nueva contraseña segura")
                self.input_pwd.setObjectName("password_input")
                self.input_pwd.returnPressed.connect(self.on_login_clicked)

                self.btn_login = QPushButton("Guardar y continuar")
                self.btn_login.setObjectName("login_button")
                self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
                self.btn_login.clicked.connect(self.on_login_clicked)

                self.lbl_error = QLabel("")
                self.lbl_error.setAlignment(Qt.AlignCenter)
                self.lbl_error.setObjectName("error_message")

                container_layout.addWidget(self.input_pwd)
                container_layout.addWidget(self.btn_login)
                container_layout.addWidget(self.lbl_error)

                self.lbl_footer = QLabel("v1.0 - desarrollado por Matías")
                self.lbl_footer.setAlignment(Qt.AlignCenter)
                self.lbl_footer.setObjectName("footer_label")

                main_layout.addWidget(self.lbl_title)
                main_layout.addWidget(self.lbl_subtitle)
                main_layout.addSpacing(10)
                main_layout.addWidget(container)
                main_layout.addSpacing(10)
                main_layout.addWidget(self.lbl_footer)

                self.setLayout(main_layout)
                self.load_stylesheet()

            def load_stylesheet(self):
                try:
                    with open(CSS_PATH, "r") as f:
                        self.setStyleSheet(f.read())
                except Exception as e:
                    print(f"No se pudo cargar el archivo CSS: {e}")

            def on_login_clicked(self):
                pwd = self.input_pwd.text().strip()
                if not pwd:
                    self.lbl_error.setText(
                        "⚠️ Por favor, ingresa una contraseña\nantes de continuar."
                    )
                    return

                create_pass(SIGNUP_FILE, KEY_FILE, pwd)
                self.login_window.load_passwords()
                self.login_window.show()
                self.close()

        return SignUpWindow()
