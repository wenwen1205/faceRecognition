# -*- coding: utf-8 -*-
# @Time : 2020-08-02 11:18
# @Author : zcw
# @Site : 
# @File : InputNameForm.py

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal, Qt
from .InputNameUI import Ui_InputName


class InputNameForm(QDialog):
    input_name = ''

    # 构造器，完成UI初始化，摄像头设备初始化等。
    def __init__(self, parent=None):

        super(InputNameForm, self).__init__(parent, Qt.FramelessWindowHint)
        self.ui = Ui_InputName()
        self.ui.setupUi(self)

        # 设置按钮为默认按钮
        self.ui.btnOK.setDefault(True)

        # 绑定关闭处理槽函数
        self.ui.btnOK.clicked.connect(self.close)

    def close(self):
        self.input_name = self.ui.edtName.text()
        self.done(0)
