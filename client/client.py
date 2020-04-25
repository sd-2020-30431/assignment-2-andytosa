import socket
import select
import errno
from ServerCommand import ServerCommand

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
#client_socket.setblocking(False)


SC = ServerCommand()

while True:
    action = input('Action: ')
    sv_command = SC.getCommand(action)
    #print(sv_command)

    client_socket.send(f"{len(sv_command):<{HEADER_LENGTH}}{sv_command}".encode('utf-8'))
