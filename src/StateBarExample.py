'''
Created on 2012/05/29

@author: hooxin
'''
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.statusBar().showMessage("Ready")
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("StateBar")
        self.show()
        
