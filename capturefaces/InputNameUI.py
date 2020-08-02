# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputName.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InputName(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(633, 442)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 120, 211, 16))
        self.label.setObjectName("label")
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setGeometry(QtCore.QRect(340, 150, 112, 32))
        self.btnOK.setObjectName("btnOK")
        self.edtName = QtWidgets.QLineEdit(Dialog)
        self.edtName.setGeometry(QtCore.QRect(170, 150, 141, 31))
        self.edtName.setObjectName("edtName")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#0000ff;\">输入需要采集人脸的人员姓名：</span></p></body></html>"))
        self.btnOK.setText(_translate("Dialog", "确认"))

