from djitellopy import Tello
from time import sleep
import pygame

# This is a module and intended to run as Module
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

# me = Tello()
# me.connect()
# print(me.get_battery())




def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key pressed")
    if getKey("UP"):
        print("Up key pressed")
    if getKey("DOWN"):
        print("Down key pressed")


if __name__ == '__main__':
    init()
    while True:
        main()
