#!/bin/python3

import cv2
from Camera import Camera, VideoFormats

frame_width = 640
frame_height = 480
framerate = 30
camera = Camera(frame_width, frame_height, framerate, VideoFormats.mjpeg)


# print openCV version
print(cv2.__version__)

while(True):
    ret = camera.captureFrame()
    if ret is True:
        # Waits for a user input to quit the application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

camera.release()
