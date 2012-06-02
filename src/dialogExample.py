#!/usr/bin/env python2
# -*- Coding:utf-8 -*-

from PyQt4 import QtGui

class Example(QtGui.QWidget):
    ''''''
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QtGui.QLineEdit(self)
        self.le.move(130,22)
        
        self.setGeometry(300,300,290,150)
        self.setWindowTitle('输入框测试')
        self.show()
        
    
    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, '输入框','输入你的名字:')
        if ok :
            self.le.setText(str(text))
        
    

class ColorDialogExample(QtGui.QWidget):
    ''''''
    def __init__(self):
        super(ColorDialogExample, self).__init__()
        self.initUI()
        pass
        
    def showDialog(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet('QWidget {background-color: %s}' % col.name())
        pass
        
    def initUI(self):
        col = QtGui.QColor(0, 0, 0)

        self.btn = QtGui.QPushButton('Dialog',self)
        self.btn.move(20,20)

        self.btn.clicked.connect(self.showDialog)
        
        self.frm = QtGui.QFrame(self)
        self.frm.setStyleSheet('QWidget {background-color: %s}' % col.name())
        self.frm.setGeometry(130,22,100,100)
        
        self.setGeometry(300,300,250,180)
        self.setWindowTitle('Color dialog')
        self.show()
        pass
    pass

class FontDialogExample(QtGui.QWidget):
    def __init__(self):
        '''
        doc
        '''
        super(FontDialogExample, self).__init__()
        self.initUI()

    def initUI(self):
        
        vbox = QtGui.QVBoxLayout()
        btn = QtGui.QPushButton('对话框',self)
        btn.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        btn.move(20,20)
        btn.clicked.connect(self.showDialog)
        
        vbox.addWidget(btn)
        self.lbl = QtGui.QLabel('Knowledge only matters', self)
        self.lbl.move(130,20)
        
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)
        
        self.setGeometry(300,300,250,180)
        self.setWindowTitle('字体对话框')
        self.show()
        
    def showDialog(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

class FileDialogExample(QtGui.QMainWindow):
    def __init__(self):
        super(FileDialogExample, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        
        openFile = QtGui.QAction(QtGui.QIcon('open.png'),'Open',self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)
        
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openFile)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self,'Open file', '/home/hooxin')
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)