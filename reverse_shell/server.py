#!/usr/bin/python3

import socket
from termcolor import colored

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("10.0.2.15",54321))#Change to your IP
s.listen(5)

print(colored("[+] Listening for incoming connections", 'green'))

target, ip = s.accept()
print(colored("[+] Connection established From: %s" % str(ip), 'green'))
s.close()

