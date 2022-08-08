import socket

# Simple command that send
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(('', 9000))

sock.sendto(b'command', 0, tello_address)
sock.sendto(b'battery?', 0, tello_address)

while True:
    try:
        data, ip = sock.recvfrom(1024)
        print("{}: {}".format(ip, data.decode()))
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break