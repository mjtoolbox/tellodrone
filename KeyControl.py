from djitellopy import Tello
import KeyPressModule as kp
from time import sleep


kp.init()
me = Tello()
me.connect()
print(me.get_battery())
# me.takeoff()


def keyControl():
    while True:
        vals = getKeyboardInput()
        me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
        sleep(0.05)
        # print(kp.getKey("s"))


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

    if kp.getKey("e"):
        me.takeoff()
    return [lr, fb, ud, yv]


if __name__ == '__main__':
    keyControl()
