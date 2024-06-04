# TCP Server

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print("Got a connection from %s" % str(address))

    message = 'Thank you for connecting to the server.'+' Goodbye!' + "\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()