from cryptography.fernet import Fernet
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QGroupBox,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QLabel,
    QMessageBox,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from .utils import (
    read_key,
    load_encrypted_passwords,
    save_encrypted_passwords,
    rotate_keys,
    generate_passwords,
)
from .config import PASS_FILE, SIGNUP_FILE, KEY_FILE, CSS_PATH
from .list_window import PasswordListWindow


class PasswordManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.passwords_file = PASS_FILE
        self.key_file = KEY_FILE
        self.password_list_window = None

        self.old_fernet = Fernet(read_key(self.key_file))
        self.new_passwords = {}

        self.setWindowTitle("Panel Principal - Password Manager")
        self.setFixedSize(700, 600)
        self.setObjectName("password_manager_window")

        central_widget = QWidget()
        central_widget.setObjectName("password_manager_central")
        self.setCentralWidget(central_widget)

        from PySide6.QtWidgets import QGridLayout
        layout = QGridLayout(central_widget)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        self.btn_show_pwds = QPushButton("📁 Ver contraseñas guardadas")
        self.btn_show_pwds.setObjectName("show_passwords_button")
        self.btn_show_pwds.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_save = QPushButton("💾 Guardar cambios")
        self.btn_save.setObjectName("save_button")
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_clear = QPushButton("📖 Borrar Contraseñas")
        self.btn_clear.setObjectName("clear_button")
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))

        actions_group = QGroupBox("⚙️ Acciones generales")
        actions_group.setObjectName("actions_group")
        actions_layout = QVBoxLayout()
        actions_layout.addWidget(self.btn_show_pwds)
        actions_layout.addWidget(self.btn_save)
        actions_layout.addWidget(self.btn_clear)
        actions_group.setLayout(actions_layout)

        self.input_site = QLineEdit()
        self.input_site.setPlaceholderText("Ej: github.com")
        self.input_site.setObjectName("site_input")
        
        self.input_usern = QLineEdit()
        self.input_usern.setPlaceholderText("Ej: nombre132")
        self.input_usern.setObjectName("site_input")

        self.input_pwd = QLineEdit()
        self.input_pwd.setPlaceholderText("Ej: contraseña123")
        self.input_pwd.setObjectName("password_input")

        self.btn_add_pwd = QPushButton("➕ Añadir contraseña")
        self.btn_add_pwd.setObjectName("save_password_button")
        self.btn_add_pwd.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_gen_pwds = QPushButton("🔁 Generar contraseñas")
        self.input_len = QLineEdit()
        self.input_len.setPlaceholderText("Ej: 12")
        self.input_qty = QLineEdit()
        self.input_qty.setPlaceholderText("Ej: 3")

        self.lbl_save_state = QLabel("")
        self.lbl_save_state.setAlignment(Qt.AlignCenter)
        self.lbl_save_state.setObjectName("save_state")

        form_group = QGroupBox("✍️ Añadir nueva contraseña")
        form_group.setObjectName("form_group")
        form_layout = QFormLayout()
        form_layout.addRow("🌐 Sitio:", self.input_site)
        form_layout.addRow("👤 Usuario:", self.input_usern)
        form_layout.addRow("🔑 Contraseña:", self.input_pwd)
        form_layout.addRow(self.btn_add_pwd)
        form_layout.addRow(self.lbl_save_state)
        form_group.setLayout(form_layout)

        gen_group = QGroupBox("🎲 Generador de contraseñas")
        gen_group.setObjectName("gen_group")
        gen_layout = QFormLayout()
        gen_layout.addRow("🔢 ¿Cuántas generar?", self.input_qty)
        gen_layout.addRow("📏 Longitud de cada una:", self.input_len)
        gen_layout.addRow(self.btn_gen_pwds)
        gen_group.setLayout(gen_layout)

        self.txt_gen_pwds = QTextEdit("🕒 Esperando ordenes...")
        self.txt_gen_pwds.setReadOnly(True)
        
        self.lbl_footer = QLabel("v1.0 - desarrollado por Matías")
        self.lbl_footer.setAlignment(Qt.AlignCenter)
        self.lbl_footer.setObjectName("footer_label")

        layout.addWidget(actions_group, 0, 0)
        layout.addWidget(form_group, 0, 1)
        layout.addWidget(gen_group, 1, 0)
        layout.addWidget(self.txt_gen_pwds, 1, 1)
        layout.addWidget(self.lbl_footer, 2, 0, 1, 2)

        self.btn_gen_pwds.clicked.connect(self.gen_pass)
        self.btn_clear.clicked.connect(self.clear_passwords)
        self.btn_show_pwds.clicked.connect(self.open_password_list_window)
        self.btn_save.clicked.connect(self.save_passwords)
        self.btn_add_pwd.clicked.connect(self.add_password)

        self.load_stylesheet()

    def load_stylesheet(self):
        try:
            with open(CSS_PATH, "r") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(f"No se pudo cargar el archivo CSS: {e}")

    def open_password_list_window(self):
        if self.password_list_window is None:
            self.password_list_window = PasswordListWindow(self)
        self.password_list_window.show()
        self.password_list_window.show_passwords()

    def clear_passwords(self):
        reply = QMessageBox.question(
            self,
            "Borrar",
            "¿Deseas borrar las contraseñas?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            with open(PASS_FILE, "w") as f:
                f.write("")
        elif reply == QMessageBox.No:
            pass

    def add_password(self):
        site = self.input_site.text()
        username = self.input_usern.text()
        password = self.input_pwd.text()
        if site and password and username:
            self.new_passwords[site] = [username, password]
            self.lbl_save_state.setText("✅ Contraseña añadida")
        else:
            self.lbl_save_state.setText("❌ Completa todos los campos")

        self.input_site.clear()
        self.input_pwd.clear()

    def save_passwords(self):
        passwords = load_encrypted_passwords(self.passwords_file, self.old_fernet)
        passwords.update(self.new_passwords)
        save_encrypted_passwords(passwords, self.passwords_file, self.old_fernet)
        self.new_passwords.clear()
        self.lbl_save_state.setText("✅ Cambios guardados")

    def gen_pass(self):
        q = self.input_qty.text()
        l = self.input_len.text()
        try:
            q = int(q)
            l = int(l)
            pws = generate_passwords(q, l)
            self.txt_gen_pwds.setText("\n".join(pws))
        except Exception:
            self.txt_gen_pwds.setText("❌ Asegúrate de ingresar números válidos.")

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Salir",
            "¿Deseas guardar los cambios antes de cerrar?",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
        )
        if reply == QMessageBox.Yes:
            self.save_passwords()
            passwords = load_encrypted_passwords(self.passwords_file, self.old_fernet)
            rotate_keys(self.passwords_file, self.key_file, SIGNUP_FILE, passwords)
            event.accept()
        elif reply == QMessageBox.No:
            passwords = load_encrypted_passwords(self.passwords_file, self.old_fernet)
            rotate_keys(self.passwords_file, self.key_file, SIGNUP_FILE, passwords)
            event.accept()
        else:
            event.ignore()