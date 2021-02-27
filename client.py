#!/usr/bin/python3

import socket

clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.1.10'
host = socket.gethostname()

port = 23
#port = 444

#clientsocket.connect(('192.168.1.10', port))
clientsocket.connect(('127.0.0.1', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))