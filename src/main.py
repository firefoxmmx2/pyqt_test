#!/usr/bin/env python2
# -*- Coding:utf-8 -*-

'''
Created on 2012/05/29

@author: hooxin
'''

import sys
from StateBarExample import Example
from PyQt4 import QtGui
import menubarExample,layoutExample,eventAndSignalExample, \
    dialogExample,widgetExample,dragdropExample, drawingExample



def main():
    app = QtGui.QApplication(sys.argv)
#    ex = Example()
#    menubar_ex = menubarExample.Example()
    #icon_menubar_ex = menubarExample.IconMenuExample()
    #label_ex = layoutExample.Example()
    #layout_ex = layoutExample.BoxLayoutExample()
    #gridlayoutEx = layoutExample.GridLayoutExample()
    #gridlayoutEx2 = layoutExample.ReviewExample()
    #eventEx = eventAndSignalExample.Example()
    #eventEx2 = eventAndSignalExample.EventSenderExample()
    #eventEx3 = eventAndSignalExample.SignalExample(    )
    #dialogEx1 = dialogExample.Example()
    #dialogEx2 = dialogExample.ColorDialogExample()
    #dialogex3 = dialogExample.FileDialogExample()
    #widgetex1 = widgetExample.CheckboxExample()
    #widgetex2 = widgetExample.CalendarExample()
    #widgetex3 = widgetExample.ComboBoxExample()
    #widgetex4 = widgetExample.LineEditExample()
    #widgetex5 = widgetExample.PixmapExample()
    #widgetex6 = widgetExample.ProgressBarExample()
    #widgetex6 = widgetExample.SliderExample()
    #widgetex7 = widgetExample.ToggleButtonExample()
    #widgetex8 = widgetExample.SplitterExample()
    #dragdropex1 = dragdropExample.DragDropButtonExample()
    #dragdropex2 = dragdropExample.DragDropButtonExample2()
#    drawingex = drawingExample.Example()
#    drawingex2 = drawingExample.DrawingPointExample()
#    drawingex3 = drawingExample.DrawingColorExample()

    drawingex4 = drawingExample.PenExample()
    
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()