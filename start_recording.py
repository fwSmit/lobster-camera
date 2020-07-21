#!/bin/python3

import cv2
from Camera import Camera, Resolutions

# print openCV version
print("Using openCV version ", cv2.__version__)

#  frame_width = 640
#  frame_height = 480
#  framerate = 30
#  frame_width = 1920
#  frame_height = 1080
#  framerate = 60.0
frame_width = 1280
frame_height = 720
framerate = 60.0

#  camera = Camera(frame_width, frame_height, framerate, VideoFormats.mjpeg)

camera = Camera.fromEnum(Resolutions.RAW_480_60)


while(True):
    ret = camera.captureFrame()
    if ret is True:
        # Waits for a user input to quit the application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # the camera failed to record a frame so abort
        break

camera.release()
