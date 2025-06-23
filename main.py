from PySide6.QtWidgets import QApplication
import sys, os
from core.startup import StartUp

os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"
os.environ["QT_LOGGING_RULES"] = "qt.gui.icc=false"
cpw = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    startup = StartUp()
    startup.run(cpw)
    sys.exit(app.exec()) 