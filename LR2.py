import sys, math
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
        dx = math.fabs(x1-x2)
        dy = math.fabs(y2-y1)
        if (dy<0):
            znaky = -1
        else:
            znaky = 1
        
        if (dx<0):
            znakx = -1
        else:
            znakx = 1
        f = 0
        x = x1
        y = y1
        qp.drawPoints(x,y)
        while(x!=x2 or y!=y2):
            if (dy<dx):
                f = f + dy*znaky
                if (f>0):
                    f=f-dx*znakx
                    y=y+znaky
                x -= znakx
                qp.drawPoints(x,y)
            else:
                f = f + dx*znakx
                if (f>0):
                    f=f-dy*znaky
                    x=x-znakx
                y += znaky
                qp.drawPoints(x,y)
                    
            
            
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())