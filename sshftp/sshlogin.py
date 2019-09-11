#!/usr/bin/python

import pexpect



def main():
    host = '192.168.1.106'
    user = 'msfadmin'
    password = 'msfadmin'
    child = connect(user,host,password)
    send_command(child, 'cat /etc/shadow | grep root;ps')

main()
