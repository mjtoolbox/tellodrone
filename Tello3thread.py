import logging
import threading
import time

import socket

# Simple command that send
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(('', 9000))

def send_function():
    # sock.sendto(b'command', 0, tello_address)
    # sock.sendto(b'battery?', 0, tello_address)
    # sock.sendto(b'time?', 0, tello_address)
    # sock.sendto(b'speed?', 0, tello_address)
    # sock.sendto(b'wifi?', 0, tello_address)
    while True: 
        try:
            msg = input("")

            if not msg:
                break  

            if 'end' in msg:
                print ('...')
                sock.close()  
                break

            # Send data
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_address)
        except KeyboardInterrupt:
            print ('\n . . .\n')
            sock.close()  
            break
        except:
            print('Unable to perform action')



def receive_function():
    while True:
        try:
            data, ip = sock.recvfrom(1518)
            print("{}: {}".format(ip, data.decode(encoding='utf-8')))
        except Exception:
            print ('\nBye...\n')
            sock.close()
            exit()


if __name__ == "__main__":
    print ('--Start with command\r\n')
    print ('--Quit with end\r\n')
    recvThread = threading.Thread(target=receive_function)
    recvThread.start()
    send_function()

    