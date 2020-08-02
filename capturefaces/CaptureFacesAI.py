# -*- coding: utf-8 -*-
# @Time : 2020-08-02 11:17
# @Author : zcw
# @Site : 
# @File : CaptureFacesAI.py.py

import cv2
import os
import numpy as np
import random

current_dir = os.path.dirname(__file__)
mod_file = os.path.join(current_dir, "data/haarcascade_frontalface_alt2.xml")


class CaptureFacesAI:
    img_path = ''

    def __init__(self):
        super(CaptureFacesAI, self).__init__()
        # 采集的图像大小
        self.imgsize = 60

        # 记录采集的图像数目
        self.n = 0
        self.harr = cv2.CascadeClassifier(mod_file)

    def createdir(self, imgpath):
        if not os.path.exists(imgpath):
            os.makedirs(imgpath)

        self.img_path = imgpath
        self.n = 0

    def relight(self, imgsrc, alpha=1, bias=0):

        imgsrc = imgsrc.astype(float)
        imgsrc = imgsrc * alpha + bias

        imgsrc[imgsrc < 0] = 0
        imgsrc[imgsrc > 255] = 255
        imgsrc = imgsrc.astype(np.uint8)
        return imgsrc

    def handle_image(self, imgsrc):

        # 将当前桢图像转换成灰度图像
        gray_img = cv2.cvtColor(imgsrc, cv2.COLOR_BGR2GRAY)

        # 侦测人脸
        faces = self.harr.detectMultiScale(gray_img, 1.3, 5)

        # 循环处理人脸（缩放，灰度变化，保存）
        if len(faces) == 1:  # 如果识别出多个人脸，不处理
            for f_x, f_y, f_w, f_h in faces:
                face = imgsrc[f_y:f_y + f_h, f_x:f_x + f_w]

            face = cv2.resize(face, (self.imgsize, self.imgsize))
            face = self.relight(face, random.uniform(0.5, 1.5), random.randint(-50, 50))

            cv2.imwrite(os.path.join(self.img_path, F"{self.n: 03d}_1.jpg"), face)
            face = self.relight(face, random.uniform(0.5, 1.5), random.randint(-50, 50))

            cv2.imwrite(os.path.join(self.img_path, F"{self.n: 03d}_2.jpg"), face)
            face = self.relight(face, random.uniform(0.5, 1.5), random.randint(-50, 50))

            cv2.imwrite(os.path.join(self.img_path, F"{self.n: 03d}_3.jpg"), face)
            # 标记人脸
            imgsrc = cv2.rectangle(imgsrc, (f_x, f_y), (f_x + f_w, f_y + f_h), (255, 0, 0), 1)

            self.n += 1
        return imgsrc