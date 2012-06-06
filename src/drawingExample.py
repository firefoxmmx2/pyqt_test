#!/usr/bin/env python2
# -*- coding:utf-8 -*-


from PyQt4 import QtGui, QtCore
from Crypto.Util.number import size

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        self.text = u"\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\u0435\u0432\u0438\u0447\
        \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
        \u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430"
        self.setGeometry(300,300,280, 170)
        self.setWindowTitle('Draw Text')
        self.show()

    def paintEvent(self,event):
        qp = QtGui.QPainter()
        qp.begin()

        self.drawText(event, qp)
        qp.end
    def drawText(self, event, qp):
        qp.setPen(QtGui.QColor(168, 23, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)
        
        
class DrawingPointExample(QtGui.QWidget):
    def __init__(self):
        super(DrawingPointExample, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Point')
        self.show()
        
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()
    def drawPoints(self,qp):
        qp.setPen(QtCore.Qt.red)
        size = self.size()
        import random
        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x,y)
            
        
class DrawingColorExample(QtGui.QWidget):
    def __init__(self):
        super(DrawingColorExample, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300,300,350,100)
        self.setWindowTitle('Color')
        self.show()
        
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self, qp):
        color = QtGui.QColor(0,0,0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        
        qp.setBrush(QtGui.QColor(200,0,0))
        qp.drawRect(10,15,90,60)
        qp.setBrush(QtGui.QColor(255,80,0, 160))
        qp.drawRect(130,15,90,60)
        
        qp.setBrush(QtGui.QColor(25,0,90,200))
        qp.drawRect(250,15,90,60)
        
        
  
class PenExample(QtGui.QWidget):
    def __init__(self):
        super(PenExample, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300,300,280,270)
        self.setWindowTitle('Pen Style')
        self.show()
        
    def paintEvent(self,e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
        
    def drawLines(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black,2,QtCore.Qt.SolidLine)
        
        qp.setPen(pen)
        qp.drawLine(20,40,250,40)
        pen.setStyle(QtCore.Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20,80,250,80)
        
        pen.setStyle(QtCore.Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20,120,250,120)
        
        pen.setStyle(QtCore.Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20,200,250,200)
    
        pen.setStyle(QtCore.Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20,200,250,200)
        
        pen.setStyle(QtCore.Qt.CustomDashLine)
        pen.setDashPattern([1,4,5,4])
        qp.setPen(pen)
        qp.drawLine(20,240,250,240)