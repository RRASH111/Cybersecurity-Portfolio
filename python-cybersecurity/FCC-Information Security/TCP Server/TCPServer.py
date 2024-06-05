# TCP Server

import socket
#Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
#bind to the socket
serversocket.bind((host, port))
#Starting TCP Listening
serversocket.listen(3)

while True:
    #starting connection
    clientsocket, address = serversocket.accept()
    print("Got a connection from %s" % str(address))

    message = 'Thank you for connecting to the server.'+' Goodbye!' + "\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()