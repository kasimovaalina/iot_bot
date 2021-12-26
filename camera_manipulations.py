import cv2 as cv
import logging
import datetime

logging.basicConfig(format="%(asctime)s %(filename)s:%(lineno)s %(name)s::%(funcName)s: %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
LOGGER = logging.getLogger("camera_manipulation")


def make_photo():
    cam = cv.VideoCapture(0)
    
    if not cam.isOpened():
        raise IOError("Cannot open webcam!")
    while True:
        ret, frame = cam.read()

        if not ret:
            LOGGER.debug("Failed to grab frame!")
            break

        img_name = "out.png"
        cv.imwrite(img_name, frame)
        LOGGER.debug("Photo is taken!")

        break

    cam.release()
    cv.destroyAllWindows()
