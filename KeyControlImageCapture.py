from djitellopy import Tello
import KeyPressModule as kp
import time
import cv2


kp.init()
me = Tello()
me.connect()
print(me.get_battery())
# me.takeoff()
global img


def keyControl():
    while True:
        vals = getKeyboardInput()
        me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
        img = me.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        cv2.imshow("Image", img)
        cv2.waitKey(1)


def getKeyboardInput():
    # Left/Right, Forward/Backward, Up/Down, Yaw Velocity
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    if kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    if kp.getKey("s"):
        ud = -speed

    if kp.getKey("d"):
        yv = speed
    if kp.getKey("a"):
        yv = -speed

    if kp.getKey("q"):
        me.land()
        time.sleep(3)

    if kp.getKey("e"):
        me.takeoff()

    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]


if __name__ == '__main__':
    keyControl()