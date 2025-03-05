import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Электронный журнал посещаемости")
        self.resize(800, 600)  # Задаём примерный размер окна

        # Пока здесь нет подробной логики — только заготовка.
        # Далее мы добавим поля ввода, списки студентов, предметы и т.д.

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
