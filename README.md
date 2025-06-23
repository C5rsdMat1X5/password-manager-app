# 🔐 Password Manager App

This application is a **password manager** developed in Python, using `PySide6` for the graphical user interface and `cryptography` to securely encrypt passwords.

## 🧰 Technologies Used

- 🖼️ [PySide6](https://doc.qt.io/qtforpython/) - For the graphical interface
- 🔐 [cryptography](https://cryptography.io/en/latest/) - For secure password encryption
- 🐍 Python 3.10+

## 📦 Project Structure

```
├── assets/              # Static files (CSS)
│   └── style.css        # Stylesheet (CSS)
├── core/                # Main logic and windows
│   ├── config.py        # Global configuration
│   ├── list_window.py   # Window to list passwords
│   ├── login_window.py  # Login window
│   ├── manager.py       # Main window of the manager
│   ├── startup.py       # App initialization
│   └── utils.py         # Miscellaneous utilities
├── data/                # Encrypted database storage
├── main.py              # Main entry point
├── requirements.txt     # Project dependencies
└── README.md
```

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/C5rsdMat1X5/password-manager-app
   cd password-manager-app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   - On **Linux/macOS**:
     ```bash
     python3 main.py
     ```

   - On **Windows**:
     ```bash
     python main.py
     ```

## 📁 Data

- Passwords are stored encrypted inside the `data/` folder.
- The app requires a master password for access, which is set on the first use.

## ⚠️ Security Notes

- This project is for educational purposes only. It is not recommended to use it to manage real passwords without proper review and adaptation.
- Make sure to keep the `data/` folder secure and backed up if you decide to use it.

## 🧠 Author

Developed by Matías Henríquez.
