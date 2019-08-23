#!/usr/bin/python3

import socket
from termcolor import colored

#Creando un socket que utiliza ipv4 y TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

#Leyendo la ip y el puerto a escanear
host = input("[*] Enter the host to scan: ")

#Definiendo una funcion para ver si el puerto esta abierto o cerrado
def portscanner(port):
    if sock.connect_ex((host,port)):
        print(colored("[!!] Port %d is closed" % (port), 'red'))
    else:
        print(colored("[+] Port %d is open" % (port), 'green'))

for port in range(1,100):
    portscanner(port)
        
