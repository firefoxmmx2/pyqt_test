#!/usr/bin/env python2
#coding:utf8

from PyQt4 import QtGui


class Example(QtGui.QWidget):
  def __init__(self):
    super(Example, self).__init__()
    
    self.init_ui()
  
  def init_ui(self):
    lbl1 = QtGui.QLabel('Zetcode', self)
    lbl1.move(15,10)
    
    lbl2 = QtGui.QLabel('tutorials',self)
    lbl2.move(35,40)
    
    lbl3 = QtGui.QLabel('for programmers',self)
    lbl3.move(55,70)
    
    self.setGeometry(300,300,250,150)
    self.show()

    
class BoxLayoutExample(QtGui.QWidget):
  def __init__(self):
      super(BoxLayoutExample, self).__init__()
      
      self.init_ui()
  
  def init_ui(self):
    okButton = QtGui.QPushButton("OK")
    cancelButton = QtGui.QPushButton("Cancel")
    
    hbox = QtGui.QHBoxLayout()
    hbox.addStretch(1)
    hbox.addWidget(okButton)
    hbox.addWidget(cancelButton)
    
    vbox = QtGui.QVBoxLayout()
    vbox.addStretch(1)
    vbox.addLayout(hbox)
    
    self.setLayout(vbox)
    
    self.setGeometry(300,300,300,150)
    self.setWindowTitle('Buttons')
    self.show()
    

    
class GridLayoutExample(QtGui.QWidget):
  def __init__(self, parent=None, flags=0):
    super(GridLayoutExample,self).__init__()
    self.initUI()
      
  def initUI(self):
    
    names = ['Cls', 'Bck', '', 'Close',
            '7', '8', '9', '/',
            '4', '5', '6', '*', 
            '1', '2', '3', '-',
            '0', '.', '=', '+']
    grid = QtGui.QGridLayout()
    
    j = 0
    pos = [(0, 0), (0, 1), (0, 2), (0, 3),
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2), (3, 3 ), 
            (4, 0), (4, 1), (4, 2), (4, 3)]
    
    for i in names:
      button = QtGui.QPushButton(i)
      if j == 2:
          grid.addWidget(QtGui.QLabel(''),0,2)
      else:
          grid.addWidget(button,pos[j][0],pos[j][1])
      j += 1
      
    self.setLayout(grid)
    self.move(300,150)
    self.setWindowTitle('计算机')
    self.show()
    
class ReviewExample(QtGui.QWidget):
    def __init__(self, parent=None, flags=0):
        super(ReviewExample, self).__init__()
        self.initUI()
        
    def initUI(self):
        title = QtGui.QLabel('标题')
        author = QtGui.QLabel('作者')
        review = QtGui.QLabel('内容')
        
        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1,1,1)
        
        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1,1,1)
        
        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)
        
        self.setLayout(grid)
        
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('网格布局测试2')
        self.show()
        