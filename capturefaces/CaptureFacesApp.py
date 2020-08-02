# -*- coding: utf-8 -*-
# @Time : 2020-08-02 11:17
# @Author : zcw
# @Site : 
# @File : CaptureFacesApp.py

from PyQt5.QtWidgets import QApplication, QDialog
from .CaptureFacesForm import CaptureFacesForm
import sys


# 实现Qt应用封装，启动CaptureFacesForm对话框窗体
class CaptureFacesApp(QApplication):
    def __init__(self):
        super(CaptureFacesApp, self).__init__(sys.argv)

        # 原始Dialog
        # self.dlg = QDialog()

        # 自定义Dialog
        self.dlg = CaptureFacesForm()
        self.dlg.show()
