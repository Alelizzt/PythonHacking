#!/usr/bin/python3

import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.0.2.15",54321))#Change to Server IP
sock.close()
