import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.setWindowTitle('Git и жёлтые окружности')

        self.but.clicked.connect(self.run)
        self.flag = False

    def paint(self, event):
        if self.flag:
            x = random.randint(0, 450)
            y = random.randint(0, 450)
            r = random.randint(1, 50)

            self.qp.setPen(QColor(255, 255, 0))

            self.qp.drawEllipse(x, y, r, r)

        # flag = False

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

