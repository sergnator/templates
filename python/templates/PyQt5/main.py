import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class Example(QApplication, QMainWindow):
    def __init__(self):
        super().__init__()

    def setup_ui(self):
        # code of ui
        self.label = QLabel("Example")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
