import socket, threading, time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(('', 9000))

def broadcaster():
    with open('commandb.txt','r') as file:
        commands=file.readlines()

    try:        
        for command in commands:
            if command != '' and command != '\n':
                command = command.rstrip()
                message=command                
                message=message.encode(encoding='utf-8')
                sock.sendto(message,tello_address)
                print("command", message)
                time.sleep(3)
    except Exception:
        print('Exception')
        sock.close()
        exit()
    except:
        print('Unable to perform action')



# def send(message):
#     sock.sendto(command, 0, tello_address)
def reciever():
    while True:
        try:
            data, ip = sock.recvfrom(1518)
            print('{}: {}'.format(ip, data.decode(encoding='utf-8')))
        except KeyboardInterrupt:
           print('Exiting')
           sock.close()
           break
        except Exception:
            # Main thread closed the socket, so it throws an exception
            print ('\nExit...\n')
            sock.close()
            exit()


if __name__=='__main__':
    print('hello')
    receivethread=threading.Thread(target=reciever)
    # broadcaster=threading.Thread(target=broadcaster)
    receivethread.start()
    # sock.sendto(b'command', 0, tello_address)
    broadcaster()
    # send_fromtxt_function()
    # broadcaster.start()
    # sock.sendto(b”battery?', 0, tello_address)