import cv2


class Camera:
    preview = True
    record = True

    def __init__(self, frame_width, frame_height, framerate, videocodec):
        # Open the device at the ID 0
        self.cap = cv2.VideoCapture(0)
        # Check whether user selected camera is opened successfully.
        if not (self.cap.isOpened()):
            print("Could not open video device")
            return
        #  frame_width = int(cv2.CAP_PROP_FRAME_WIDTH)
        #  frame_height = int(cv2.CAP_PROP_FRAME_HEIGHT)
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.framerate = framerate

        print("Using resolution", frame_width, "x", frame_height)

        # To set the resolution
        # cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

        self.out = cv2.VideoWriter('outpy.avi', videocodec, framerate, (frame_width, frame_height))

    def release(self):
        # release the camera and the capture
        print("Releasing camera")
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()

    def captureFrame(self):
        ret, frame = self.cap.read()
        if ret is True:
            if self.record:
                self.out.write(frame)
            if self.preview:
                # Display the resulting frame
                cv2.imshow('preview', frame)
        return ret

    def setPreview(self, preview: bool):
        self.preview = preview

    def setRecord(self, record: bool):
        self.record = record


class VideoFormats:
    mjpeg = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    raw = cv2.VideoWriter_fourcc('U', 'Y', 'V', 'Y')
