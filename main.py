# -*- coding: utf-8 -*-

import os
import sys
import glob
import threading
import time

from PySide import QtCore
from PySide import QtGui
from PySide import QtUiTools

from FlowLayout import *

app = QtGui.QApplication.instance()
if app is None:
    app = QtGui.QApplication(sys.argv)

mainWindow = None


def createLabel(path):
    #t = time.time()
    label = QtGui.QLabel()
    
    imageSize = None
    ext = os.path.splitext(path)[1]
    if ext == ".gif":
        movie = QtGui.QMovie(path)
        if movie.frameCount() > 0:
            label.setMovie(movie)
            movie.start()
        else:
            label.setPixmap(movie.currentPixmap())
        imageSize = movie.currentImage().size()
    else:
        t = time.time()
        image = QtGui.QImage(path)
        imageSize = image.size()
        pixmap = QtGui.QPixmap.fromImage(image)
        label.setPixmap(pixmap)
    
    scale = 100.0 / max(imageSize.width(), imageSize.height())
    label.setFixedWidth(int(float(imageSize.width()) * scale))
    label.setFixedHeight(int(float(imageSize.height()) * scale))
    label.setScaledContents(True)

    #print time.time() - t

    return label


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        loader = QtUiTools.QUiLoader()
        self.__ui = loader.load(os.path.join(os.getcwd(), "ui", "MainDialog.ui"))
        
        self.__layout = FlowLayout()
        
        #self.load()
        
        w = QtGui.QWidget()
        w.setLayout(self.__layout)
        self.__ui.previewPanel.setWidget(w)
        
        self.setCentralWidget(self.__ui)
        
        geom = self.__ui.geometry()
        self.__width = geom.right() - geom.left()
        self.__height = geom.bottom() - geom.top()
        self.resize(self.__width, self.__height)

    def load(self):
        for path in glob.glob(os.path.join("D:", os.sep, "home", "Pictures", "ScreenShot", "*")):
            label = createLabel(path)
            self.__layout.addWidget(label)

    def showEvent(self, e):
        super(MainWindow, self).showEvent(e)
        print "shoeEvent"
    
    def paintEvent(self, e):
        super(MainWindow, self).paintEvent(e)
        print "paintEvent"


def main():
    global mainWindow
    mainWindow = MainWindow()
    mainWindow.show()
    mainWindow.repaint()
    print "repaint"
    mainWindow.load()
    print "load"


if __name__ == '__main__':
    QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForLocale())
    main()
    if not app is None:
        sys.exit(app.exec_())

