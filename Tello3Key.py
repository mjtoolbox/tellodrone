import logging
import threading
from time import sleep
import KeyPressModule as kp
import socket

kp.init()

# Simple command that send
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(('', 8889))

def send_function():
    print('Checking Tello drone status')
    sock.sendto(b'command', 0, tello_address)
 
    while True: 
        try:
            msg = getKeyboardInput()
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_address)                    
        except KeyboardInterrupt:
            print ('\n . . .\n')
            sock.close()  
            break
        except:
            print('Unable to perform action')

def getKeyboardInput():
    val = ''
    if kp.getKey("b"):
        val = 'battery?'
    return val


def receive_function():
    while True:
        try:
            data, ip = sock.recvfrom(1518)
            print("{}: {}".format(ip, data.decode(encoding='utf-8')))
        except Exception:
            # Main thread closed the socket, so it throws an exception
            print ('\nExit...\n')
            sock.close()
            exit()


if __name__ == "__main__":
    print ('--Start with command\r\n')
    print ('--Quit with end\r\n')
    recvThread = threading.Thread(target=receive_function)
    recvThread.start()
    send_function()
    