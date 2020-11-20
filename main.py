import sys

from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Git и случайные окружности')
        self.setupUi(self)

        self.but.clicked.connect(self.run)
        self.flag = False

    def paint(self, event):
        if self.flag:
            x = randint(0, 300)
            y = randint(0, 300)
            r = randint(1, 100)

            self.qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))

            self.qp.drawEllipse(x, y, r, r)

        self.flag = False

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.paint(self.qp)
        self.qp.end()

    def run(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

