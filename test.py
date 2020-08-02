# -*- coding: utf-8 -*-
# @Time : 2020-08-02 14:10
# @Author : zcw
# @Site : 
# @File : test

import cv2

cap = cv2.VideoCapture(0)
i = 0
while (1):
    ret, frame = cap.read()
    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('/Users/step/Desktop' + str(i) + '.jpg', frame)
        i += 1
    cv2.imshow("capture", frame)
cap.release()
cv2.destroyAllWindows()
