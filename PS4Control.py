import pygame
# from tello3 import Tello
from djitellopy import Tello

# Speed of the drone
S = 60
# Buttons used
X = 0
O = 1
triangle = 3
square = 2
L1 = 9
R1 = 10
#L2 = 6
#R2 = 7
share_button = 8
options_button = 6 
FRONT = 11
BACK = 12
LEFT = 13
RIGHT = 14

class PS4Control(object):
    """ Maintains the Tello display and moves it through the buttonboard buttons.
    Press escape button to quit.
    The controls are:
        - Square: Takeoff
        - Triangle: Land
        - Arrow buttons: Forward, backward, left and right
        - L1 and R1: Counter clockwise and clockwise rotations
        - X and O: Up and down
        - Options: turns off drone
    """
    def __init__(self):
        pygame.init()
        
        # Init joystick
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

        # Create pygame window
        self.screen = pygame.display.set_mode((400, 400))
        # Initiate Tello
        self.tello = Tello()

        # Drone velocities
        self.for_back_velocity = 0
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.yaw_velocity = 0
        self.speed = 10

        self.send_rc_control = False
        # create update timer
        pygame.time.set_timer(pygame.USEREVENT + 1, 50)

    def run(self):        

        # if not self.tello.connect():
        #     print("Tello not connected")
        #     return

        # if not self.tello.set_speed(self.speed):
        #     print("Not set speed to lowest possible")
        #     return

        # # In case streaming is on. This happens when we quit this program without the escape button.
        # if not self.tello.streamoff():
        #     print("Could not stop video stream")
        #     return

        # if not self.tello.streamon():
        #     print("Could not start video stream")
        #     return

        should_stop = False
        while not should_stop:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT + 1:
                    self.update()
                elif event.type == pygame.QUIT:
                    should_stop = True
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == options_button:
                        should_stop = True
                    else:
                        self.buttonDown(event.button)
                elif event.type == pygame.JOYHATMOTION:
                    if event.value == (0, 0):
                        self.buttonUp(event.value)
                        #print("hello from run")
                    else:
                        self.buttonDown(event.value)
                elif event.type == pygame.JOYBUTTONUP:
                    self.buttonUp(event.button)
                # Call it always before finishing. To deallocate resources.
        self.tello.end()

    def buttonDown(self, button):
        """ Update velocities based on button pressed
        Arguments:
            button: pygame button
        """
        print("Button Down: " + str(button))

        # if button == (0, 1):  # set forward velocity
        if button == FRONT:
            print("Move forward")
            self.for_back_velocity = S
        # elif button == (0, -1):  # set backward velocity
        elif button == BACK:  # set backward velocity
            print("Move backward")
            self.for_back_velocity = -S
        # elif button == (-1, 0):  # set left velocity
        elif button == LEFT:  # set left velocity
            print("Move left")
            self.left_right_velocity = -S
        # elif button == (1, 0):  # set right velocity
        elif button == RIGHT:  # set right velocity
            print("Move right")
            self.left_right_velocity = S
        elif button == X:  # set up velocity
            self.up_down_velocity = S
        elif button == O:  # set down velocity
            self.up_down_velocity = -S
        elif button == L1:  # set yaw counter clockwise velocity
            self.yaw_velocity = -S
        elif button == R1:  # set yaw clockwise velocity
            self.yaw_velocity = S

    def buttonUp(self, button):
        """ Update velocities based on button released
        Arguments:
            button: pygame button
        """
        # if button == (0, 0):
        if button == FRONT or button == BACK or button == LEFT or button == RIGHT :
            #print("hello from buttonUp")
            self.for_back_velocity = 0
            self.left_right_velocity = 0
        elif button == X or button == O:  # set zero up/down velocity
            self.up_down_velocity = 0
        elif button == L1 or button == R1:  # set zero yaw velocity
            self.yaw_velocity = 0
        elif button == triangle:  # takeoff
            self.tello.takeoff()
            self.send_rc_control = True
        elif button == square:  # land
            self.tello.land()
            self.send_rc_control = False
        # elif button == L2:
        #     cv2.imwrite(os.path.join(os.path.abspath(photos), f"picture{imgCount}.jpg"), self.tello.get_frame_read().frame)
        #     imgCount+=1
        #     print("Photo Taken!!!")

  
    def update(self):
        """ Update routine. Send velocities to Tello."""
        if self.send_rc_control:
            # self.tello.send_command(f'rc {self.left_right_velocity} {self.for_back_velocity} {self.up_down_velocity} {self.yaw_velocity}')
            self.tello.send_rc_control(self.left_right_velocity, self.for_back_velocity, self.up_down_velocity, self.yaw_velocity)
def main():
    ps4control = PS4Control()

    # run frontend
    ps4control.run()


if __name__ == '__main__':
    main()