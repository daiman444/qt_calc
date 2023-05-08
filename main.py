#!/usr/bin/env python3

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import operator
from test_app import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __int__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.show()


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName('Calc')
    window = MainWindow()
    window.show()
    app.exec_()