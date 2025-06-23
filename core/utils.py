import os
import json
import random
from cryptography.fernet import Fernet

def read_key(key_file: str) -> bytes:
    if not os.path.exists(key_file):
        return create_key(key_file)
    with open(key_file, "rb") as f:
        return f.read()


def create_pass(SIGNUP_FILE: str, KEY_FILE: str, passw: str) -> None:
    if not passw:
        print("la contra esta vacia")
    fernet = Fernet(read_key(KEY_FILE))
    data = fernet.encrypt(passw.encode())
    with open(SIGNUP_FILE, "wb") as f:
        f.write(data)


def read_pass(SIGNUP_FILE, KEY_FILE):
    if not os.path.exists(SIGNUP_FILE):
        return None
    fernet = Fernet(read_key(KEY_FILE))
    try:
        with open(SIGNUP_FILE, "rb") as f:
            encrypted_data = f.read()
        decrypted = fernet.decrypt(encrypted_data).decode()
        return decrypted
    except Exception as e:
        print(f"Clave inválida o datos corruptos: no se pudo descifrar la contraseña. {e}")
        return None


def check_if_first(SIGNUP_FILE: str) -> bool:
    return not os.path.exists(SIGNUP_FILE)


def create_key(key_file: str) -> bytes:
    key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(key)
    return key


def load_encrypted_passwords(passwords_file: str, fernet: Fernet) -> dict:
    if not os.path.exists(passwords_file):
        return {}
    try:
        with open(passwords_file, "rb") as f:
            encrypted_data = f.read()
            decrypted_json = fernet.decrypt(encrypted_data).decode()
            return json.loads(decrypted_json)
    except Exception:
        return {}


def save_encrypted_passwords(passwords: dict, passwords_file: str, fernet: Fernet) -> None:
    try:
        json_data = json.dumps(passwords)
        encrypted_data = fernet.encrypt(json_data.encode())
        with open(passwords_file, "wb") as f:
            f.write(encrypted_data)
    except Exception as e:
        print(f"Error al guardar contraseñas: {e}")


def rotate_keys(passwords_file: str, key_file: str, signup_file: str, passwords: dict) -> None:
    key = Fernet.generate_key()
    new_fernet = Fernet(key)
    data = new_fernet.encrypt(json.dumps(passwords).encode())
    data2 = new_fernet.encrypt(read_pass(signup_file, key_file).encode())

    with open(passwords_file, "wb") as f:
        f.write(data)
    with open(signup_file, "wb") as f:
        f.write(data2)
    with open(key_file, "wb") as f:
        f.write(key)


def generate_passwords(quantity: int, length: int) -> list[str]:
    chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$()*+-./:<=>?@[]_")
    pws = []
    for i in range(quantity):
        pw = "".join(random.choice(chars) for _ in range(length))
        pws.append(f"[{i + 1}]  {pw}")
    return pws