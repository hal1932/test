# -*- coding: utf-8 -*-

import sys
from PySide import QtCore
from PySide import QtGui

from ui_MainWindow import *
from ui_TweetItem import *

app = QtGui.QApplication.instance()
if app is None:
    app = QtGui.QApplication([])

mainWindow = None


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for i in xrange(10):
            item = Ui_TweetItem()
            item.setupUi(self)
            self.ui.items.addWidget(item)


def main():
    global mainWindow
    mainWindow = MainWindow()
    mainWindow.show()


if __name__ == '__main__':
    QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForLocale())
    main()
    if not app is None:
        sys.exit(app.exec_())

