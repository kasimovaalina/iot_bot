import cv2 as cv
import logging
import datetime

logging.basicConfig(format="%(asctime)s %(filename)s:%(lineno)s %(name)s::%(funcName)s: %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
LOGGER = logging.getLogger("main")

if __name__ == "__main__":
    cam = cv.VideoCapture(0)

    if not cam.isOpened():
        raise IOError("Cannot open webcam")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            LOGGER.debug("Failed to grab frame")
            break

        cv.imshow("Test", frame)

        k = cv.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            LOGGER.debug("Escape hit, closing...")
            break

        elif k % 256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv.imwrite(img_name, frame)
            LOGGER.debug("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv.destroyAllWindows()