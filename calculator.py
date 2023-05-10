#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The calculator was developed during the study and development of
programming skills in the Python3 language using the PyQt5 library
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        # adding and initializing objects
        self.pb = QPushButton
        self.grid = QGridLayout()
        self.lbl_result = QLabel()
        self.lbl_result.setText('Result')
        self.lbl_input = QLabel()
        self.lbl_input.setText('0')
        self.input_string = ''
        self.input_list = []
        self.v_layout = QVBoxLayout()
        self.init_ui()

    def init_ui(self):
        self.lbl_result.setStyleSheet('color: orange;'
                                      'font-family: Noto Sans;'
                                      'font-size: 20pt;'
                                      'font-weight: bold;'
                                      )
        self.lbl_result.setAlignment(Qt.AlignRight)

        self.lbl_input.setStyleSheet('color: rgb(153, 255, 153);'
                                     'font-family: Noto Sans;'
                                     'font-size: 26pt;'
                                     'font-weight: bold;'
                                     )
        self.lbl_input.setAlignment(Qt.AlignRight)

        # matrix of button names
        names = ['C', '<<', '(', ')',
                 '7', '8', '9', '*',
                 '4', '5', '6', '/',
                 '1', '2', '3', '+',
                 '0', '.', '=', '-',
                 ]

        # button position mark
        # copied and pasted, but I liked the method and I left it as a keepsake
        positions = [(i, j) for i in range(5) for j in range(4)]

        # creating buttons with position and name assignment to them
        for position, name in zip(positions, names):
            pb = QPushButton(name)
            self.grid.addWidget(pb, *position)
            pb.clicked.connect(lambda widget, n=name: self.pb_action(widget, action=n))

        # collect widgets
        self.v_layout.addWidget(self.lbl_result)
        self.v_layout.addWidget(self.lbl_input)
        self.v_layout.addLayout(self.grid)
        self.setLayout(self.v_layout)

        # window settings
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Calc')
        self.show()

# TODO  add a method for output of input errors so that application does not crash on errors

    def pb_action(self, widget, action):
        """
        in this method, signals from buttons are received and actions related to
        them are performed
        :param widget: unused
        :param action: gets from creating buttons
        :return: None
        """

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
        """
        clears the 'memory of the calculator
        :return: None
        """
        self.input_string = ''
        self.input_list = []
        self.lbl_input.setText('0')
        self.lbl_result.setText('Result')

    def result_output(self):
        """
        prints the result of the calculation
        :return: None
        """
        result = eval(self.input_string)
        self.lbl_result.setText('%s' % result)

    def del_last_value(self):
        """
        removes the last displayed chapter
        :return: None
        """
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
