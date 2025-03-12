import sys
from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()  # Используем MainWindow из views/main_window.py
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
