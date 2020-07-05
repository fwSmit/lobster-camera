import cv2


class Camera:
    # Open the device at the ID 0
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        # Check whether user selected camera is opened successfully.
        if not (self.cap.isOpened()):
            print("Could not open video device")
            return
        #  frame_width = int(cv2.CAP_PROP_FRAME_WIDTH)
        #  frame_height = int(cv2.CAP_PROP_FRAME_HEIGHT)
        self.frame_width = 640
        self.frame_height = 480

        print("Using resolution", self.frame_width, "x", self.frame_height)

        # To set the resolution
        # cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

        self.out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (self.frame_width, self.frame_height))

    def release(self):
        # release the camera and the capture
        print("Releasing camera")
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()

    def captureFrame(self):
        ret, frame = self.cap.read()
        if ret is True:
            self.out.write(frame)
            # Display the resulting frame
            cv2.imshow('preview', frame)
            # Waits for a user input to quit the application
        return ret
