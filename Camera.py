import cv2
from enum import IntEnum


class VideoFormats:
    mjpeg = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    #  raw = cv2.VideoWriter_fourcc('U', 'Y', 'V', 'Y')
    raw = cv2.VideoWriter_fourcc('Y', 'U', 'Y', 'V')


class VideoResolutions:
    horizontal_res = [640, 1920, 640]
    vertical_res = [480, 1080, 480]
    framerates = [60, 60, 60]
    videoFormats = [VideoFormats.mjpeg, VideoFormats.mjpeg, VideoFormats.raw]

    def __init__(self, val):
        self.value = val

    def get_horizontal_res(self):
        return self.horizontal_res[int(self.value)]

    def get_vertical_res(self):
        return self.vertical_res[int(self.value)]

    def get_framerate(self):
        return self.framerates[int(self.value)]

    def get_videoformat(self):
        return self.videoFormats[int(self.value)]


class Resolutions(IntEnum):
    MJPEG_480 = 0
    MJPEG_1080 = 1
    RAW_480_60 = 2


class Camera:
    preview = True
    record = True

    #  def __init__(self, resolution: Resolutions):


    def __init__(self, frame_width, frame_height, framerate, videocodec):
        camera_number = 4  # the location of the camera (/dev/video*)
        ret = self.attatch(camera_number)
        if not ret:
            print("Could not find camera in /dev/video%d" % camera_number)
            return
        #  frame_width = int(cv2.CAP_PROP_FRAME_WIDTH)
        #  frame_height = int(cv2.CAP_PROP_FRAME_HEIGHT)
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.framerate = framerate
        self.videocodec = videocodec

        print("Using resolution", frame_width, "x", frame_height)

        # To set the resolution
        ret1 = self.cap.set(cv2.CAP_PROP_FOURCC, videocodec)
        ret2 = self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        ret3 = self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
        ret4 = self.cap.set(cv2.CAP_PROP_FPS, framerate)
        print(ret1, ret2, ret3, ret4)

        self.out = cv2.VideoWriter('outpy.avi', videocodec, framerate, (frame_width, frame_height))

    @classmethod
    def fromEnum(cls, number):
        res = VideoResolutions(number)
        frame_width = res.get_horizontal_res()
        frame_height = res.get_vertical_res()
        framerate = res.get_framerate()
        codec = res.get_videoformat()
        print("fram height", frame_height)
        return cls(frame_width, frame_height, framerate, codec)

    def attatch(self, number):
        # Open the device at the ID 'number'
        self.cap = cv2.VideoCapture(number)
        # Check whether user selected camera is opened successfully.
        if not (self.cap.isOpened()):
            print("Could not open video device")
            return False
        return True

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

# this doesn't seem to work yet
    #  def __del__(self):
        #  self.release()

    def setPreview(self, preview: bool):
        self.preview = preview

    def setRecord(self, record: bool):
        self.record = record


