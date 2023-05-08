# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 259)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_eq = QtWidgets.QPushButton(self.centralwidget)
        self.pb_eq.setObjectName("pb_eq")
        self.gridLayout.addWidget(self.pb_eq, 6, 3, 1, 2)
        self.pb_n8 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_n8.setObjectName("pb_n8")
        self.gridLayout.addWidget(self.pb_n8, 3, 2, 1, 1)
        self.pb_point = QtWidgets.QPushButton(self.centralwidget)
        self.pb_point.setObjectName("pb_point")
        self.gridLayout.addWidget(self.pb_point, 6, 2, 1, 1)
        self.pb_n4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_n4.setObjectName("pb_n4")
        self.gridLayout.addWidget(self.pb_n4, 4, 1, 1, 1)
        self.pb_n6 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_n6.setObjectName("pb_n6")
        self.gridLayout.addWidget(self.pb_n6, 4, 3, 1, 1)
        self.pb_n3 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_n3.setObjectName("pb_n3")
        self.gridLayout.addWidget(self.pb_n3, 5, 3, 1, 1)
        self.pb_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pb_multiply.setObjectName("pb_multiply")
        self.gridLayout.addWidget(self.pb_multiply, 2, 4, 1, 1)
        self.pb_n9 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_n9.setObjectName("pb_n9")
        self.gridLayout.addWidget(self.pb_n9, 3, 3, 1, 1)
        self.pb_div = QtWidgets.QPushButton(self.centralwidget)
        self.pb_div.setObjectName("pb_div")
        self.gridLayout.addWidget(self.pb_div, 3, 4, 1, 1)
        self.pb_n5 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_n5.setObjectName("pb_n5")
        self.gridLayout.addWidget(self.pb_n5, 4, 2, 1, 1)
        self.pb_n1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_n1.setObjectName("pb_n1")
        self.gridLayout.addWidget(self.pb_n1, 5, 1, 1, 1)
        self.pb_bspc = QtWidgets.QPushButton(self.centralwidget)
        self.pb_bspc.setObjectName("pb_bspc")
        self.gridLayout.addWidget(self.pb_bspc, 2, 3, 1, 1)
        self.pb_n0 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_n0.setObjectName("pb_n0")
        self.gridLayout.addWidget(self.pb_n0, 6, 1, 1, 1)
        self.pb_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pb_minus.setObjectName("pb_minus")
        self.gridLayout.addWidget(self.pb_minus, 5, 4, 1, 1)
        self.pb_n7 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_n7.setObjectName("pb_n7")
        self.gridLayout.addWidget(self.pb_n7, 3, 1, 1, 1)
        self.pb_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pb_clear.setObjectName("pb_clear")
        self.gridLayout.addWidget(self.pb_clear, 2, 1, 1, 1)
        self.pb_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pb_plus.setObjectName("pb_plus")
        self.gridLayout.addWidget(self.pb_plus, 4, 4, 1, 1)
        self.pb_n2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_n2.setObjectName("pb_n2")
        self.gridLayout.addWidget(self.pb_n2, 5, 2, 1, 1)
        self.lbl_input = QtWidgets.QLabel(self.centralwidget)
        self.lbl_input.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_input.setFont(font)
        self.lbl_input.setStyleSheet("")
        self.lbl_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_input.setObjectName("lbl_input")
        self.gridLayout.addWidget(self.lbl_input, 1, 1, 1, 4)
        self.pb_sign_change = QtWidgets.QPushButton(self.centralwidget)
        self.pb_sign_change.setObjectName("pb_sign_change")
        self.gridLayout.addWidget(self.pb_sign_change, 2, 2, 1, 1)
        self.lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_result.setObjectName("lbl_result")
        self.gridLayout.addWidget(self.lbl_result, 0, 1, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.pb_eq.setText(_translate("MainWindow", "="))
        self.pb_n8.setText(_translate("MainWindow", "8"))
        self.pb_point.setText(_translate("MainWindow", "."))
        self.pb_n4.setText(_translate("MainWindow", "4"))
        self.pb_n6.setText(_translate("MainWindow", "6"))
        self.pb_n3.setText(_translate("MainWindow", "3"))
        self.pb_multiply.setText(_translate("MainWindow", "*"))
        self.pb_n9.setText(_translate("MainWindow", "9"))
        self.pb_div.setText(_translate("MainWindow", "/"))
        self.pb_n5.setText(_translate("MainWindow", "5"))
        self.pb_n1.setText(_translate("MainWindow", "1"))
        self.pb_bspc.setText(_translate("MainWindow", "Bspc"))
        self.pb_n0.setText(_translate("MainWindow", "0"))
        self.pb_minus.setText(_translate("MainWindow", "-"))
        self.pb_n7.setText(_translate("MainWindow", "7"))
        self.pb_clear.setText(_translate("MainWindow", "C"))
        self.pb_plus.setText(_translate("MainWindow", "+"))
        self.pb_n2.setText(_translate("MainWindow", "2"))
        self.lbl_input.setText(_translate("MainWindow", "123456789"))
        self.pb_sign_change.setText(_translate("MainWindow", "+/-"))
        self.lbl_result.setText(_translate("MainWindow", "Result"))
