# -*- coding: utf-8 -*-
# @Time : 2020-08-02 11:18
# @Author : zcw
# @Site : 
# @File : CaptureFacesDevs.py

from font_zh.FontZH import FontZh
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from .CaptureFacesAI import CaptureFacesAI
import cv2
import os
import time


class CaptureFacesDevs(QThread):

    # 定义信号发送采集的视频图像
    # 前面三个是图像高度，宽度，深度，最后是图像数据
    sign_show = pyqtSignal(int, int, int, bytes)

    def __init__(self, dev_id):
        super(CaptureFacesDevs, self).__init__()
        self.isSave = False
        self.isOver = False
        self.ai = CaptureFacesAI()

        # 完成摄像头初始化
        self.dev = cv2.VideoCapture(dev_id)

    def run(self):
        while not self.isOver:
            # 抓取视频
            status, img = self.dev.read()

            if not status:
                self.dev.release()
                self.exit(0)

            if self.isSave:
                img = self.ai.handle_image(img)

                if self.ai.n >= 50:
                    self.isSave = False

                img = FontZh().draw_text(img, (10, 20), F"采集中: {self.ai.n: 03d}", 20, (0, 0, 255))

            else:
                img = FontZh().draw_text(img, (10, 20), F"停止采集", 20, (0, 0, 255))

            # 发送信号给窗体显示视频
            self.sign_show.emit(img.shape[0], img.shape[1], img.shape[2], img.tobytes())
            QThread.sleep(0.5)

    def close(self):
        self.isOver = True
        while self.isRunning():
            self.isOver = True
        if self.dev.isOpened():
            self.dev.release()

    def get_state(self, save_info):
        if save_info == "stop":
            self.isSave = False

        elif save_info == "continue":
            self.isSave = True

        else:
            self.isSave = True
            self.ai.createdir(os.path.join("./images", save_info))

