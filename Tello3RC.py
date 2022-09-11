import logging
import threading
import time

import socket

# Simple command that send
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(('', 8889))


def send_fromtxt_function():
    print('Reading from txt')
    with open('commandrc.txt', 'r') as file:
        commands = file.readlines()

    try:              
        for command in commands:
            if command != '' and command != '\n':
                command = command.rstrip()
                msg = command

                # Send data
                msg = msg.encode(encoding="utf-8") 
                sent = sock.sendto(msg, tello_address)
                print("Command: ",msg)
                time.sleep(3)
        msg = input("Type 'end' to quit")
            
        if 'end' in msg:
            print ('Closing...')
            sock.close()  
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
    except:
        print('Unable to perform action')


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
    send_fromtxt_function()
    