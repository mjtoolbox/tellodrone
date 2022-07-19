from djitellopy import Tello
from time import sleep
import logging


me = Tello()
me.connect()
print(me.get_battery())


# Using RC Control: left_right, forward_backward, up_down, rotate
# forward

def usingCommand():
    me.takeoff()
    me.move_forward(100)
    # me.rotate_counter_clockwise(90)
    me.move_back(100)
    me.land()


def usingRCcontrol():
    me.takeoff()
    me.send_rc_control(0, 0, 0, 30)
    sleep(2)
    me.send_rc_control(0, 0, 0, 30)
    sleep(2)
    me.send_rc_control(0, 0, 0, 30)
    me.land()


if __name__ == '__main__':
    # usingRCcontrol()
    usingCommand()
