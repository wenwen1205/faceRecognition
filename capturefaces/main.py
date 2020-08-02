# -*- coding: utf-8 -*-
# @Time : 2020-08-02 11:18
# @Author : zcw
# @Site : 
# @File : main.py.py

from capturefaces.CaptureFacesApp import CaptureFacesApp
import sys

if __name__ == '__main__':
    app = CaptureFacesApp()
    status = app.exec()
    sys.exit(status)
