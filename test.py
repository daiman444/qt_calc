#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.pb = QPushButton
        self.pb_pos_x = 20
        self.pb_pos_y = 30
        self.font_result = QFont('Arial', 16, 3)
        self.font_input = QFont('Arial', 25, 1)

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        result_string = QLabel('Result')
        result_string.setFont(self.font_result)
        result_string.setStyleSheet('color: orange; background-color: rgb(64, 64, 64)')
        result_string.setAlignment(Qt.AlignRight)

        input_string = QLabel('0')
        input_string.setFont(self.font_input)
        input_string.setStyleSheet('color: rgb(153, 255, 153); background-color: rgb(64, 64, 64)')
        input_string.setAlignment(Qt.AlignRight)


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
            if name == '=':
                pb = QPushButton(name)
                grid.addWidget(pb, *position, 1, 2, )
                break
            pb = QPushButton(name)
            grid.addWidget(pb, *position)

        v_layout = QVBoxLayout()

        v_layout.addWidget(result_string)
        v_layout.addWidget(input_string)
        v_layout.addLayout(grid)

        self.setLayout(v_layout)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Calc')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

