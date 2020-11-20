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

    def paint(self):
        self.repaint()

    def paintEvent(self):
        qp = QPainter()
        qp.begin(self)

        x = random.randint(0, 450)
        y = random.randint(0, 450)
        r = random.randint(1, 50)

        qp.setBrush(QColor(255, 255, 0))

        qp.drawEllipse(x, y, r, r)
        qp.end()

    def run(self):
        self.repaint()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

