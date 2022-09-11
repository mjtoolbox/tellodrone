import tello3oManual
from TellooUI import TelloUI


def main():
    drone = tello3oManual.Tello('', 8889)  
    vplayer = TelloUI(drone)
    vplayer.root.mainloop() 


if __name__ == '__main__':
    main()