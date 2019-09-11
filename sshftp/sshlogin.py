#!/usr/bin/python

import pexpect

PROMPT = ['# ','>>> ','> ','\$ ']

def connect(user,host,password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print '[-] Error connecting'
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print '[-] Error connecting'
            return
    child.sendline(password)
    child.pexpect(PROMPT)


def main():
    host = '192.168.1.106'
    user = 'msfadmin'
    password = 'msfadmin'
    child = connect(user,host,password)
    send_command(child, 'cat /etc/shadow | grep root;ps')

main()
