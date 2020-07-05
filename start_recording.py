#!/bin/python3

import cv2
from Camera import Camera

camera = Camera()

# print openCV version
print(cv2.__version__)

while(True):
    ret = camera.captureFrame()
    if ret is True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

camera.release()
