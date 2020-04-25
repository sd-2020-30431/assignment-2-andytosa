import socket
import select

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]
clients = {}

print(f'Listening for connections on {IP}:{PORT}')


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        
        print(message_header.decode('utf-8'))
        message_length = int(message_header.decode('utf-8'))
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        return False


while True:

    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:

            # The other returned object is ip/port set
            client_socket, client_address = server_socket.accept()

            # Add accepted socket to select.select() list
            sockets_list.append(client_socket)
            
            clients[client_socket] = client_address
            print(client_address)
            print('Accepted new connection from {}:{}'.format(*client_address))

        # Else existing socket is sending a message
        else:

            # Receive message
            message = receive_message(notified_socket)

            # If False, client disconnected, cleanup
            if message is False:
                print('Closed connection from {}'.format(clients[notified_socket]))

                # Remove from list for socket.socket()
                sockets_list.remove(notified_socket)

                # Remove from our list of users
                del clients[notified_socket]

                continue

            # Get user by notified socket, so we will know who sent the message
            user = clients[notified_socket]

            print(f'Received message from {user}: {message["data"].decode("utf-8")}')


    # It's not really necessary to have this, but will handle some socket exceptions just in case
    for notified_socket in exception_sockets:

        # Remove from list for socket.socket()
        sockets_list.remove(notified_socket)

        # Remove from our list of users
        del clients[notified_socket]
