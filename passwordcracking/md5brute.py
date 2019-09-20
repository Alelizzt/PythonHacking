#!/usr/bin/python3

from termcolor import colored
import hashlib


def tryOpen(wordlist):
    global pass_file
    try:
        pass_file = open(wordlist, 'r')
    except:
        print("No such file at that path!")


pass_hash = input("[*] Enter md5 hash value: ")
wordlist = input("[*] Enter path to the password file: ")
tryOpen(wordlist)

for word in pass_file:
    print(colored("[-] Trying: " +word.strip("\n"), 'red'))
    enc_wrd = word.encode('utf-8')
    md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if md5digest == pass_hash:
        print(colored("[+] Password found: " + word, 'green'))
        exit(0)

print(colored("[!!] Password not in list","yellow"))
