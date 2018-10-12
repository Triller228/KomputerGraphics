import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Points')
        self.show()


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()


    def drawPoints(self, qp):
        
        qp.setPen(Qt.red)
        size = self.size()
        qp.drawPoint(300, 100)
        qp.drawPoint(301, 100)
        qp.drawPoint(302, 100)
        qp.drawPoint(303, 100)
        qp.drawPoint(304, 100)
        e = 0
        x1 = 200
        y1 = 200
        x2 = 300
        y2 = 450
        dx = x2-x1
        dy = y2-y1
        e1 = e*dx
        k = (y2-y1)/(x2-x1)
        print ("k= " , k)
        while (x1!=x2 or y1!=y2):
            x1 +=1
            e1 = e1 + dy
            if (e1 > 0.5*dx):
                y1 +=1
                qp.drawPoint(x1, y1)
                e1 -=1
            
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())