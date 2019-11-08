#!/usr/bin/python

import socket



def shell():
    command = sock.recv(1024)
    message = "Hello world"
    sock.send(message)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.0.2.15",54321))#Change to Server IP

shell()

sock.close()
