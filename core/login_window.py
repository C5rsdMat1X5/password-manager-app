from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from .config import CSS_PATH, SIGNUP_FILE, KEY_FILE
from .manager import PasswordManagerWindow
from .utils import read_pass


class LogInWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.sign_up = ChangePassword()
        self.password = None
        self.load_passwords()

        self.setWindowTitle("Login - Password Manager")
        self.setFixedSize(420, 420)
        self.setObjectName("login_window")

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        self.lbl_title = QLabel("🔐 Password Manager Log In")
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.lbl_title.setObjectName("app_title")

        self.lbl_subtitle = QLabel("Accede de forma segura a tus contraseñas")
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
        self.input_pwd.setPlaceholderText("Ingresa tu contraseña")
        self.input_pwd.setObjectName("password_input")
        self.input_pwd.returnPressed.connect(self.login)

        self.btn_pw = QPushButton("Entrar")
        self.btn_pw.setObjectName("login_button")
        self.btn_pw.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pw.clicked.connect(self.login)

        self.btn_cpw = QPushButton("Cambiar contraseña")
        self.btn_cpw.setObjectName("login_button")
        self.btn_cpw.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cpw.clicked.connect(self.change_pw)

        self.lbl_error = QLabel("")
        self.lbl_error.setAlignment(Qt.AlignCenter)
        self.lbl_error.setObjectName("error_message")

        container_layout.addWidget(self.input_pwd)
        container_layout.addWidget(self.btn_pw)
        container_layout.addWidget(self.lbl_error)
        container_layout.addWidget(self.btn_cpw)

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

        self.mainWindow = PasswordManagerWindow()

    def load_stylesheet(self):
        try:
            with open(CSS_PATH, "r") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(f"No se pudo cargar el archivo CSS: {e}")

    def load_passwords(self):
        self.password = read_pass(SIGNUP_FILE, KEY_FILE)

    def change_pw(self):
        self.sign_up.show()
        self.close()

    def login(self):
        if self.input_pwd.text() == self.password:
            self.mainWindow.show()
            self.close()
        else:
            self.lbl_error.setText("❌ Contraseña incorrecta")


class ChangePassword(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cambiar Contraseña - Password Manager")
        self.setFixedSize(420, 400)
        self.setObjectName("login_window")

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        self.lbl_title = QLabel("🔐 Cambiar Contraseña")
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.lbl_title.setObjectName("app_title")

        self.lbl_subtitle = QLabel("Verifica tu contraseña actual para continuar")
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
        self.input_pwd.setPlaceholderText("Confirma tu contraseña actual")
        self.input_pwd.setObjectName("password_input")
        self.input_pwd.returnPressed.connect(self.login)

        self.btn_pw = QPushButton("Continuar con el cambio")
        self.btn_pw.setObjectName("login_button")
        self.btn_pw.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pw.clicked.connect(self.login)

        self.lbl_error = QLabel("")
        self.lbl_error.setAlignment(Qt.AlignCenter)
        self.lbl_error.setObjectName("error_message")

        container_layout.addWidget(self.input_pwd)
        container_layout.addWidget(self.btn_pw)
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

    def login(self):
        self.password = read_pass(SIGNUP_FILE, KEY_FILE)
        if self.input_pwd.text() == self.password:
            from .startup import StartUp
            cpw = True
            self.sign_up = StartUp()
            self.sign_up.run(cpw)
            self.close()
        else:
            self.lbl_error.setText("❌ Contraseña incorrecta. Intenta nuevamente.")