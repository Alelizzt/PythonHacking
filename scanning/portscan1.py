#!/usr/bin/python

import socket

#Creando un socket que utiliza ipv4 y TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 443

#Definiendo una funcion para ver si el puerto esta abierto o cerrado
def portscanner(port):
    if sock.connect_ex((host,port)):
        print "Port %d is closed" % (port)
    else:
        print "Port %d is opened" % (port)

portscanner(port)
        
