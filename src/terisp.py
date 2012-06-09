#!/usr/bin/env python2
# -*- coding:utf-8 -*-
'''
Created on 2012-6-6

@author: hooxin
'''


import sys
import random
from PyQt4 import QtCore, QtGui
from random import Random

class Tetris(QtGui.QMainWindow):
    def __init__(self):
        super(Tetris, self).__init__()
        
        self.setGeometry(300,300,180,380)
        self.setWindowTitle('Tetris')
        self.tetrisBoard = Board(self)
        
        self.setCentralWidget(self.tetrisBoard)
        
        self.statusbar = self.statusBar()
        self.connect(self.tetrisBoard, QtCore.SIGNAL('messageToStatusbar(QString)'),self.statusbar, QtCore.SLOT('showMessage(QString)'))
        self.tetrisBoard.start()
        self.center()
        
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
        
class Board(QtGui.QFrame):
    boardWidth = 10
    boardHeight=22
    speed=300
    
    def __init__(self,parent):
        super(Board, self).__init__(parent)
        
        self.timer = QtCore.QBasicTimer()
        self.isWaitingAfterLine = False
        self.curPiece = Shape()
        self.nextPiece = Shape()
        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []
        
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()
        
        self.nextPiece.setRandomShape()
        
    def shapeAt(self,x,y):
        return self.board[(y*Board.boardWidth)+x]
    
    def setShapeAt(self,x,y,shape):
        self.board[(y*Board.boardWidth)+x]  = shape
    def squareWidth(self):
        return self.contentsRect().width() / Board.boardWidth
    
    def squareHeight(self):
        return self.contentsRect().height() / Board.boardHeight
    def start(self):
        if self.isPaused:
            return
        
        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()
        
        self.emit(QtCore.SIGNAL('messageToStatubar(QString)'), str(self.numLinesRemoved))
        
        self.newPiece()
        self.timer.start(Board.speed, self)
        
    def pause(self):
        if not self.isStarted:
            return
        
        self.isPaused = not self.isPaused
        if self.isPaused:
            self.timer.stop()
            self.emit(QtCore.SIGNAL('messageToStatusbar(QString)'), 'paused')
        else:
            self.timer.start(Board.speed,self)
            self.emit(QtCore.SIGNAL('messageToStatusbar(QString)'), str(self.numLinesRemoved))
        
        self.update()
        
    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        rect = self.contentsRect()
        
        boardTop = rect.bottom() - Board.boardHeight * self.squareHeight()
        
        for i in range(Board.boardHeight):
            for j in range(Board.boardWidth):
                shape = self.shapeAt(j, Board.boardHeight - i -1)
                if shape != Tetrominoes.NoShape:
                    self.drawSquare(painter, rect.left() + j * self.squareWidth(),
                                    boardTop + i * self.squareHeight(), shape)
                    
        if self.curPiece.shape() != Tetrominoes.NoShape:
            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(), 
                                boardTop + (Board.boardHeight - y - 1 ) * self.squareHeight(),
                                self.curPiece.shape())
                
    def keyPressEvent(self, e):
        if not self.isStarted or self.curPiece.shape() == Tetrominoes.NoShape:
            QtGui.QWidget.keyPressEvent(self,e)
            return
        
        key = e.key()
        if key == QtCore.Qt.Key_P:
            self.pause()
            return
        if self.isPaused:
            return
        elif key == QtCore.Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
        elif key == QtCore.Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
        elif key == QtCore.Qt.Key_Down:
            self.tryMove(self.curPiece.rotatedRight(), self.curX, self.curY)
        elif key == QtCore.Qt.Key_Up:
            self.tryMove(self.curPiece.rotatedLeft(), self.curX, self.curY)
        elif key == QtCore.Qt.Key_Space:
            self.dropDown()
            
        elif key == QtCore.Qt.Key_D:
            self.oneLineDown()
        else:
            QtGui.QWidget.keyPressEvent(self,e)
            
    def clearBoard(self):
        for i in range(Board.boardHeight * Board.boardWidth):
            self.board.append(Tetrominoes.NoShape)
            
    def dropDown(self):
        newY = self.curY
        while newY > 0:
            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break
            newY = 1
        self.pieceDropped()
    def timerEvent(self, e):
        if e.timerId() == self.timer.timerId():
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()
        else:
            QtGui.QFrame.timerEvent(self, e)
    
    def oneLineDown(self):
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()
        
    def pieceDropped(self):
        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())
            
        self.removeFullLines()
        
        if not self.isWaitingAfterLine:
            self.newPiece()
        
    def removeFullLines(self):
        numFullLines = 0
        rowsToRomve = []
        
        for i in range(Board.boardHeight):
            n = 0
            for j in range(Board.boardWidth):
                if not self.shapeAt(j, i) == Tetrominoes.NoShape:
                    n += 1
            
            if n == 10:
                rowsToRomve.append(i)
                
        rowsToRomve.reverse()
        
        for m in rowsToRomve:
            for k in range(m, Board.boardHeight):
                for l in range(Board.boardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))
                    
        numFullLines += len(rowsToRomve)
        
        if numFullLines > 0:
            self.numLinesRemoved += numFullLines
            self.emit(QtCore.SIGNAL('messageToStatusbar(QString)'),
                      str(self.numLinesRemoved))
            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoes.NoShape)
            self.update()
            
        
    def newPiece(self):
        self.curPiece = self.nextPiece
        self.nextPiece.setRandomShape()
        self.curX = Board.boardWidth / 2 + 1
        self.curY = Board.boardHeight - 1 + self.curPiece.minY()
        
        if not self.tryMove(self.curPiece, self.curX, self.curY):
            self.curPiece.setShape(Tetrominoes.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.emit(QtCore.SIGNAL('messageToStatusbar(QString)'), 'Game Over')
            
    def tryMove(self, newPiece, newX, newY):
        for i in range(4):
            x = newX  + newPiece.x(i)
            y = newY - newPiece.y(i)
            if x < 0 or x >= Board.boardWidth or y < 0 or y>= Board.boardHeight:
                return False
            if self.shapeAt(x, y) != Tetrominoes.NoShape:
                return False
        
        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()
        return True
    
    def drawSquare(self, painter, x, y, shape):
        colorTable = [0x000000, 0xcc6666, 0x66cc66,0x6666cc,
                     0xcccc66, 0xcc66cc, 0x66cccc, 0xdaaa00]
        color = QtGui.QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, self.squareHeight() - 2, color)
        
        painter.setPen(color.light())
        painter.drawLine(x,y + self.squareHeight() - 1, x, y)
        painter.drawLine(x,y, x+ self.squareWidth() - 1, y)
        
        painter.setPen(color.dark( ))
        painter.drawLine(x+1,y+self.squareHeight() - 1, x+self.squareWidth() - 1,y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,y + self.squareHeight() - 1,
                         x + self.squareWidth() - 1,y + 1)
    
class Tetrominoes(object):
    NoShape = 0
    ZShape = 1
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredShape = 7
                
    
class Shape(object):
    coordsTable = (
        ((0,0),(0,0),(0,0),(0,0)),
        ((0,-1),(0,0),(-1,0),(-1,1)),
        ((0,-1),(0,0),(1,0),(1,1)),
        ((0,-1),(0,0),(0,1),(0,2)),
        ((-1,0),(0,0),(1,0),(0,1)),
        ((0,0),(1,0),(0,1),(1,1)),
        ((-1,-1),(0,-1),(0,0),(0,1)),
        ((1,-1),(0,-1),(0,0),(0,1))
    )
    
    def __init__(self):
        self.coords = [[0,0] for i in range(4)]
        self.pieceShape = Tetrominoes.NoShape
        
        self.setShape(Tetrominoes.NoShape)
        
    def shape(self):
        return self.pieceShape
    
    def setShape(self, shape):
        table = Shape.coordsTable[shape]
        
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]
                
        self.pieceShape = shape
        
    def setRandomShape(self):
        self.setShape(random.randint(1,7))
    def x(self,idx):
        return self.coords[idx][0]
    
    def y(self, idx):
        return self.coords[idx][1]
    
    def setX(self,idx, x):
        self.coords[idx][0] = x
        
    def setY(self,idx, y):
        self.coords[idx][1] = y

    def minX(self):
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])
            
        return m
    
    def minY(self):
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])
            
        return m
    
    def maxY(self):
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])
        return m
    
    def rotatedLeft(self):
        if self.pieceShape == Tetrominoes.SquareShape:
            return self
        
        result = Shape()
        result.pieceShape = self.pieceShape
        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))
            
        return result
    
    def rotatedRight(self):
        if self.pieceShape == Tetrominoes.SquareShape:
            return self
        
        result = Shape()
        result.pieceShape = self.pieceShape
        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))
    
        return result
    
app = QtGui.QApplication(sys.argv)
teris = Tetris()
teris.show()

sys.exit(app.exec_())
            