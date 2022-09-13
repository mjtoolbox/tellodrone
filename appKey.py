import time
import sys
import pygame
import pygame.display
import pygame.key
import pygame.locals
import pygame.font
import os
import datetime
from tello3 import Tello
import sys
from datetime import datetime
import time
import argparse


def keyControl():
    init()
    global me 
    me = Tello()
    me.takeoff()
    while True:
        try: 
            main()
            vals = getKeyboardInput()
            me.send_command('rc {0} {1} {2} {3}'.format(vals[0], vals[1], vals[2], vals[3]))
            time.sleep(0.05)
        except KeyboardInterrupt:
            print ('\n . . .\n')
            me.land()  
            break

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getKey(keyName):
    answer = False
    for event in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        answer = True
    pygame.display.update()

    return answer

def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key pressed")
    if getKey("UP"):
        print("Up key pressed")
    if getKey("DOWN"):
        print("Down key pressed")
    if getKey("b"):
        print("Get battery")

def getKeyboardInput():
    # Left/Right, Forward/Backward, Up/Down, Yaw Velocity
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if getKey("LEFT"):
        lr = -speed
    elif getKey("RIGHT"):
        lr = speed
    if getKey("UP"):
        fb = speed
    if getKey("DOWN"):
        fb = -speed
    if getKey("w"):
        ud = speed
    if getKey("s"):
        ud = -speed
    if getKey("d"):
        yv = speed
    if getKey("a"):
        yv = -speed
        
    if getKey("q"):
        me.land()
    if getKey("e"):
        me.takeoff()
    
    if getKey("l"):
        me.flip("l")

    return [lr, fb, ud, yv]

if __name__ == '__main__':
    keyControl()

