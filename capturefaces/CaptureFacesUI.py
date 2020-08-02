# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CaptureFaces.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CaptureFaces(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(1096, 669)
        self.formFrame_2 = QtWidgets.QFrame(dialog)
        self.formFrame_2.setGeometry(QtCore.QRect(50, 40, 221, 471))
        self.formFrame_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.formFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.formFrame_2.setObjectName("formFrame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.formFrame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblhelp_title = QtWidgets.QLabel(self.formFrame_2)
        self.lblhelp_title.setObjectName("lblhelp_title")
        self.verticalLayout_3.addWidget(self.lblhelp_title)
        self.lblhelp_description = QtWidgets.QLabel(self.formFrame_2)
        self.lblhelp_description.setObjectName("lblhelp_description")
        self.verticalLayout_3.addWidget(self.lblhelp_description)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.frm_video = QtWidgets.QFrame(dialog)
        self.frm_video.setGeometry(QtCore.QRect(290, 30, 640, 480))
        self.frm_video.setFrameShape(QtWidgets.QFrame.Panel)
        self.frm_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_video.setObjectName("frm_video")
        self.formLayout = QtWidgets.QFormLayout(self.frm_video)
        self.formLayout.setObjectName("formLayout")
        self.lbl_video = QtWidgets.QLabel(self.frm_video)
        self.lbl_video.setObjectName("lbl_video")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbl_video)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.lblhelp_title.setText(_translate("dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\"><br/><br/></span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#fc0107;\">人脸图像采集说明</span><span style=\" font-size:24pt; font-weight:600; color:#0000ff;\">：</span></p></body></html>"))
        self.lblhelp_description.setText(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\"><br /></span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18pt; font-weight:600; font-style:italic; color:#fc0107;\">Ctrl + G: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PingFang SC\'; font-weight:600;\">  需要输入姓名后开始采集人脸图像，</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PingFang SC\'; font-weight:600;\">  采集数量达到</span><span style=\" font-family:\'Helvetica Neue\'; font-weight:600;\">200</span><span style=\" font-family:\'PingFang SC\'; font-weight:600;\">后自动停止采集；</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:x-large; font-weight:600; color:#0000ff;\"><br /><br /></span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18pt; font-weight:600; font-style:italic; color:#fc0107;\">Ctrl + S: </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PingFang SC\'; font-weight:600;\">  手工停止采集人脸。</span></p></body></html>"))
        self.lbl_video.setText(_translate("dialog", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:36pt;\">视频显示区</span></p></body></html>"))

