'''
Created on 2012/05/30

@author: hooxin
'''
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example,self).__init__()
        
        self.init_ui()
        
    def init_ui(self):
        exit_action = QtGui.QAction(QtGui.QIcon('exit.jpg'),'&Exit',self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(QtGui.qApp.quit)
        
        self.statusBar()
        
        menubar = self.menuBar()
        file_menu = menubar.addMenu('F&ile')
        file_menu.addAction(exit_action)
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('MenuBar')
        self.show()
        
class IconMenuExample(QtGui.QMainWindow):
    def __init__(self):
        super(IconMenuExample,self).__init__()
        self.init_ui()
        
    def init_ui(self):
        text_edit = QtGui.QTextEdit()
        self.setCentralWidget(text_edit)
        
        exit_action = QtGui.QAction(QtGui.QIcon('exit.jpg'),'&Exit',self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(QtGui.qApp.quit)
        
        self.statusBar()
        
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_action)
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('IconMenubar')
        self.show()
