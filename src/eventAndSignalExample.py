#!/usr/bin/env python2
# -*-coding:utf-8 -*-


'''
一个关于PYQT4的事件和信号的测试例子
'''

from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('事件监听')
        self.show()
        
    def keyPressEvent(self,e):
        print (e.key())
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
            
class EventSenderExample(QtGui.QMainWindow):
    def __init__(self):
        super(EventSenderExample, self).__init__()
        self.initUI()
        
    def initUI(self):
        btn1 = QtGui.QPushButton('按钮1', self)
        btn1.move(30, 50)
        
        btn2 = QtGui.QPushButton('按钮2', self)
        btn2.move(150, 50)
        
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(300,300,290,150)
        self.setWindowTitle('手动绑定事件监听')
        self.show()
    
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' 被按下了')


class Communicate(QtCore.QObject):
    closeApp = QtCore.pyqtSignal()
    
class SignalExample(QtGui.QMainWindow):
    def __init__(self, parent=None, flags=0):
        super(SignalExample, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        
        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Emit signal')
        self.show()
        
    def mousePressEvent(self, event):
        self.c.closeApp.emit()
        