import socket

# Simple command that send
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(('', 8889))

sock.sendto(b'command', 0, tello_address)
sock.sendto(b'battery?', 0, tello_address)
sock.sendto(b'time?', 0, tello_address)
sock.sendto(b'speed?', 0, tello_address)
sock.sendto(b'wifi?', 0, tello_address)



while True:
    try:
        data, ip = sock.recvfrom(1024)
        print("{}: {}".format(ip, data.decode()))
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break
        exit()
    except:
        print('Unable to perform action')
