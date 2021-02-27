#!/usr/bin/python3

import socket

#SOCKET FUNCTION/ OBJECT
#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.1.10'
host = socket.gethostname() #get value from the host or server
#port = 444
port = 23

#Binding to socket 
#serversocket.bind((host, port)) 
#Host will be replaced/substitued with IP, if changed and not running on host
#serversocket.bind(('192.168.1.10', port))
serversocket.bind(('127.0.0.1', port))

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection
    clientsocket, address = serversocket.accept()

    print("received connection from: %s " % str(address))

    message = 'Hello! Thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()