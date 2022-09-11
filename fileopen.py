from datetime import datetime
import time
import logging

def file_open():
    file = open('test.txt', 'w')
    try:
        file.write('hello world')
    finally:
        file.close()


def file_open_with():
    with open('testwith.txt', 'w') as file:
        file.write("Content written with statement")

def file_read():
    with open('command.txt', 'r') as file:
        commands = file.readlines()
        for command in commands:
            print(command)

def file_write():
    with open(f'log/{time.time()}.log', 'w') as out:
        log = ['hello','there']        
        for stat in log:
            out.write(stat)

if __name__ == '__main__':
    # file_open()
    # file_open_with()
    #file_read()
    file_write()