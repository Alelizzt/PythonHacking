#!/usr/bin/python3

import crypt
from termcolor import colored

def CrackPass(cryptWord):
    salt = cryptWord[0:2]
    dictionary = open('dictionary.txt','r')
    for word in dictionary.readlines():
        word = word.strip('\n')
        cryptPass = crypt.crypt(word, salt)
        if(cryptWord == cryptPass):
            print(colored( "[+] Found password: " + word ,'green'))
            return
    



def main():
    passFile = open('passcrypt.txt','r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptWord = line.split(':')[1].strip(' ').strip('\n')
            print(colored("[*] Cracking password for: " + user,'yellow'))
            CrackPass(cryptWord)

main()
