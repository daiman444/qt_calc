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
        self.grid = QGridLayout()
        self.lbl_result = QLabel()
        self.lbl_result.setText('Result')
        self.lbl_input = QLabel()
        self.lbl_input.setText('0')
        self.input_string = ''
        self.input_list = []
        self.pb_pos_x = 20
        self.pb_pos_y = 30
        self.font_result = QFont('Arial', 16, 3)
        self.font_input = QFont('Arial', 25, 1)
        self.v_layout = QVBoxLayout()

        self.initUI()

    def initUI(self):
        self.lbl_result.setFont(self.font_result)
        self.lbl_result.setStyleSheet('color: orange')
        self.lbl_result.setAlignment(Qt.AlignRight)

        self.lbl_input.setFont(self.font_input)
        self.lbl_input.setStyleSheet('color: rgb(153, 255, 153)')
        self.lbl_input.setAlignment(Qt.AlignRight)

        names = ['C', '<<', '(', ')',
                 '7', '8', '9', '*',
                 '4', '5', '6', '/',
                 '1', '2', '3', '+',
                 '0', '.', '=', '-',
                 ]

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            #if name == '=':
            #    pb = QPushButton(name)
            #    self.grid.addWidget(pb, *position, 1, 2, )
            #    pb.clicked.connect(lambda widget, n=name: self.pb_action(widget, action=n))
            #    break
            pb = QPushButton(name)
            self.grid.addWidget(pb, *position)
            pb.clicked.connect(lambda widget, n=name: self.pb_action(widget, action=n))

        self.v_layout.addWidget(self.lbl_result)
        self.v_layout.addWidget(self.lbl_input)
        self.v_layout.addLayout(self.grid)

        self.setLayout(self.v_layout)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Calc')
        self.show()

    def pb_action(self, widget, action):
        if action == 'C':
            self.clear()
            return
        elif action == '=':
            self.result_output()
            return
        elif action == '<<':
            self.del_last_value()
            return
        elif action == '+/-':
            return
        self.input_string = ''
        self.input_list += action
        for i in self.input_list:
            self.input_string += i
        self.lbl_input.setText(self.input_string)

    def clear(self):
        self.input_string = ''
        self.input_list = []
        self.lbl_input.setText('0')
        self.lbl_result.setText('Result')

    def result_output(self):
        result = eval(self.input_string)
        self.lbl_result.setText('%s' % result)

    def del_last_value(self):
        del self.input_list[-1]
        if len(self.input_list) == 0:
            self.clear()
            return
        self.input_string = ''
        for i in self.input_list:
            self.input_string += i
        self.lbl_input.setText(self.input_string)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

