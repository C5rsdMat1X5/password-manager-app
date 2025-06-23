import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.dirname(BASE_PATH)

CSS_PATH = os.path.join(BASE_PATH, "assets/style.css")
PASS_FILE = os.path.join(BASE_PATH, "data", "pass.txt")
KEY_FILE = os.path.join(BASE_PATH, "data", "key.txt")
SIGNUP_FILE = os.path.join(BASE_PATH, "data", "signup.txt")