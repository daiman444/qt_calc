#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.pb = QPushButton
        self.pb_pos_x = 20
        self.pb_pos_y = 30
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        #self.setLayout(grid)

        names = ['C', '+/-', '<<', '*',
                 '7', '8', '9', '/',
                 '4', '5', '6', '+',
                 '1', '2', '3', '-',
                 '0', '.', '='
                 ]

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            pb = QPushButton(name)
            grid.addWidget(pb, *position)

        v_layout = QVBoxLayout()
        v_layout.addStretch(2)
        v_layout.addLayout(grid)

        self.setLayout(v_layout)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Foo')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

