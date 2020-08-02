# -*- coding: utf-8 -*-
# @Time : 2020-08-02 11:18
# @Author : zcw
# @Site : 
# @File : CaptureFacesForm.py

from PyQt5.QtWidgets import QDialog
from .CaptureFacesUI import Ui_CaptureFaces
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap
from .CaptureFacesDevs import CaptureFacesDevs
from .InputNameForm import InputNameForm


class CaptureFacesForm(QDialog):

    # 前面三个是图像高度，宽度，深度，最后是图像数据
    sign_captrue = pyqtSignal(str)

    def __init__(self):
        super(CaptureFacesForm, self).__init__()
        # 创建Ui_CaptureFaces对象
        self.ui = Ui_CaptureFaces()
        self.ui.setupUi(self)

        # 摄像头线程创建与开启
        # 绑定采集控制信号到采集设备线程
        self.dev = CaptureFacesDevs(0)
        self.dev.sign_show.connect(self.show_video)
        self.sign_captrue.connect(self.dev.get_state)
        self.dev.start()

    def show_video(self, h, w, d, bytes_video):
        self.img_bytes = bytes_video
        self.img_shape = (h, w, d)

        image = QImage(bytes_video, w, h, d * w, QImage.Format_RGB888)

        # 把QImage转换为QPixmap
        pixmap = QPixmap.fromImage(image)

        # QLabel只接受QPixmap类型的图像
        self.ui.lbl_video.setPixmap(pixmap)

        # 根据QLabel大小缩放图像
        self.ui.lbl_video.setScaledContents(True)

    # Ctrl + G / Ctrl + S按键处理
    def keyReleaseEvent(self, e):
        pass

    # 窗体关闭前的释放工作,条件不满足可以阻止窗体关闭
    def closeEvent(self, e):
        pass

    # 实现窗体在按下ESC键也不退出；
    def keyPressEvent(self, e):
        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_G:
            self.input = InputNameForm(self)
            self.input.ui.edtName.setFocus()
            self.input.exec()

            # 获取输入的姓名
            self.name = self.input.input_name

            # 释放窗体
            self.input.destroy()

            # 发送信号开始采集-发送字符串
            self.sign_captrue.emit(self.name)

        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_R:
            self.sign_captrue.emit("continue")

        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_P:
            self.dev.run()

        # Ctrl + S暂停采集
        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_S:
            # 发送信号给采集线程，停止保存侦测到的人脸图像
            self.sign_captrue.emit("stop")  # 发送停止的信号


    # 覆盖窗体关闭事件
    def closeEvent(self, e):
        pass

    # 覆盖按键释放事件
    def keyReleaseEvent(self, e):
        pass
