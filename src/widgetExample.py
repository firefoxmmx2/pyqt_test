#!/usr/bin/env python2
# -*- Coding:utf-8 -*-


from PyQt4 import QtGui, QtCore

class CheckboxExample(QtGui.QWidget):
    '''
    
    '''
    def __init__(self):
        super(CheckboxExample, self).__init__()
        self.initUI()
    
    def initUI(self):
        cb = QtGui.QCheckBox('show tile', self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QtGui.QCheckBox')
        self.show()
        
    def changeTitle(self,state):
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('QtGui.QCheckBox')
        else:
            self.setWindowTitle('')
            
class ToggleButtonExample(QtGui.QWidget):
    def __init__(self):
        super(ToggleButtonExample, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.col = QtGui.QColor(0,0,0)
        redb = QtGui.QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10,10)
        
        redb.clicked[bool].connect(self.setColor)
        redb = QtGui.QPushButton('Green',self)
        redb.setCheckable(True)
        redb.move(10,60)
        
        redb.clicked[bool].connect(self.setColor)
        
        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet('QWidget {background-color: %s}' % self.col.name())
        
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Toggle button')
        self.show()
        
    def setColor(self,pressed):
        source = self.sender()
        
        if pressed:
            val = 500
        else: val = 0
        
        if source.text() == 'Red':
            self.col.setRed(val)
        elif source.text() == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        self.square.setStyleSheet('QFrame {background-color: %s}' % self.col.name())
        
        
class SliderExample(QtGui.QWidget):
    def __init__(self):
        super(SliderExample, self).__init__()
        self.initUI()
    def initUI(self):
        sld =QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setGeometry(30,40,100,30)
        sld.valueChanged[int].connect(self.chantValue)
        
        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('mute.png'))
        self.label.setGeometry(160, 40, 80 ,30)
        
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QtGui.QSlider')
        self.show()
        
    def chantValue(self, value):
        if value == 0:
            self.label.setPixmap(QtGui.QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QtGui.QPixmap('min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QtGui.QPixmap('med.png'))
        else:
            self.label.setPixmap(QtGui.QPixmap('max.png'))
            
    
class ProgressBarExample(QtGui.QWidget):
    def __init__(self):
        super(ProgressBarExample, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)
        
        self.btn = QtGui.QPushButton('Start',self)
        self.btn.setGeometry(40,80,50,30)
        #self.btn.move(40,80)
        self.btn.clicked.connect(self.doAction)
        
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QtGui.QProgressBar')
        self.show()
        
    def timerEvent(self,e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100,self)
            self.btn.setText('Stop')
            
class CalendarExample(QtGui.QWidget):
    def __init__(self):
        super(CalendarExample, self).__init__()
        self.initUI()
    def initUI(self):
        cal =QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20,20)
        cal.clicked[QtCore.QDate].connect(self.showDate)
        
        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130,260)
        
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Calender')
        self.show()
        
    def showDate(self, date):
        self.lbl.setText(date.toString())
        
class PixmapExample(QtGui.QWidget):
    def __init__(self):
        super(PixmapExample,self).__init__()
        self.initUI()
    def initUI(self):
        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap('redrock.png')
        
        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)
        
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(300,200)
        self.setWindowTitle('Red Rock')
        self.show()
        
class LineEditExample(QtGui.QWidget):
    def __init__(self, parent=None, flags=0):
        super(LineEditExample,self).__init__()
        self.initUI()
    def initUI(self):
        self.lbl = QtGui.QLabel(self)
        qle = QtGui.QLineEdit(self)
        
        qle.move(60,100)
        self.lbl.move(60,40)
        qle.textChanged[str].connect(self.onChanged)
        
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QtGui.QLineEdit')
        self.show()
        
    def onChanged(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        
class SplitterExample(QtGui.QWidget):
    def __init__(self):
        super(SplitterExample,self).__init__()
        self.initUI()
        
    def initUI(self):
        hbox = QtGui.QHBoxLayout(self)
        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.StyledPanel)
        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)
        
        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)
        
        splitter1=QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        
        splitter2=QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('QtGui,QSplitter')
        self.show()
        
class ComboBoxExample(QtGui.QWidget):
    def __init__(self):
        super(ComboBoxExample, self).__init__()
        self.initUI()
    def initUI(self):
        self.lbl = QtGui.QLabel('Ubuntu',self)
        combo = QtGui.QComboBox(self)
        combo.addItem('Ubuntu')
        combo.addItem('Mandriva')
        combo.addItem('Fedora')
        combo.addItem('Red Hat')
        combo.addItem('Gentoo')
        
        combo.move(50,50)
        self.lbl.move(50,150)
        
        combo.activated[str].connect(self.onActived)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('QtGui.QComboBox')
        self.show()
        
    def onActived(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()