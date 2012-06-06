#!/usr/bin/env python2
# -*- Coding:utf-8 -*-


from PyQt4 import QtGui, QtCore

class Button(QtGui.QPushButton):
    def __init__(self,title ,parent):
        super(Button, self).__init__(title,parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self,e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e):
        self.setText(e.mimeData().text())

class DragDropButtonExample(QtGui.QWidget):
    def __init__(self):
        super(DragDropButtonExample,self).__init__()

        self.initUI()
    def initUI(self):
        edit = QtGui.QLineEdit('',self)
        edit.setDragEnabled(True)
        edit.move(30,65)
        button = Button('Button', self)
        button.move(190, 65)

        self.setWindowTitle('Simple Drag & Drop')
        self.setGeometry(300, 300, 300, 150)
        self.show()
        

class Button2(QtGui.QPushButton):
    def __init__(self, title,parent):
        super(Button2, self).__init__(title, parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.RightButton:
            return

        mimeData = QtCore.QMimeData()

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos())

        dragAction = drag.start(QtCore.Qt.MoveAction)

    def mousePressEvent(self, e):
        QtGui.QPushButton.mousePressEvent(self,e)
        if e.button() == QtCore.Qt.LeftButton:
            print('press')
            
class DragDropButtonExample2(QtGui.QWidget):
    def __init__(self):
        super(DragDropButtonExample2, self).__init__()
        self.initUI()
    def initUI(self):
        self.setAcceptDrops(True)
        self.button = Button2('Button',self)
        self.button.move(100, 65)
        self.setWindowTitle('Click or Move')

        self.setGeometry(300,300, 280, 150)
        self.show()

    def dragEnterEvent(self,e ):
        e.accept()
    def dropEvent(self,e):
        position = e.pos()

        self.button.move(position)
        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()
        

        