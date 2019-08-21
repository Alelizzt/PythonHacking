#!/usr/bin/python

import socket

#Creando un socket que utiliza ipv4 y TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

#Leyendo la ip y el puerto a escanear
host = raw_input("[*] Enter the host to scan: ")
port = int(raw_input("[*] Enter the port to scan: "))

#Definiendo una funcion para ver si el puerto esta abierto o cerrado
def portscanner(port):
    if sock.connect_ex((host,port)):
        print "Port %d is closed" % (port)
    else:
        print "Port %d is open" % (port)

portscanner(port)
        
