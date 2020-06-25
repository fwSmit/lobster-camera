#!/bin/python3

import cv2
# print openCV version
print (cv2.__version__)

# Open the device at the ID 0
cap = cv2.VideoCapture(0)

#Check whether user selected camera is opened successfully.
if not (cap.isOpened()):
    print("Could not open video device")

    
#  frame_width = int(cv2.CAP_PROP_FRAME_WIDTH)
#  frame_height = int(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = 640
frame_height = 480

print (frame_width, "x", frame_height)

#To set the resolution
#  cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
#  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        out.write(frame)
        # Display the resulting frame
        cv2.imshow('preview',frame)
        # Waits for a user input to quit the application

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture

cap.release()
out.release()

cv2.destroyAllWindows()

