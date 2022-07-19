from djitellopy import Tello
from time import sleep
import logging
import cv2


me = Tello()
me.connect()
print(me.get_battery())


def capture():
    me.streamon()
    while True:
        img = me.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    capture()
