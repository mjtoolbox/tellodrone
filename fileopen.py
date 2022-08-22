
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


if __name__ == '__main__':
    # file_open()
    # file_open_with()
    file_read()