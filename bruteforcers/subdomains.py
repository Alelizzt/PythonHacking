#!/usr/bin/python

import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except request.exceptions.ConnectionError:
        pass

target_url = raw_input("[*] Enter target URL: ")
file_name = raw_input("[*] Enter file to use: ")

file = open(file_name,"r")
for line in file:
    word = line.strip()
    full_url = word + "." + target_url
    response = request(full_url)
    if response:
        print("[+] Discovered subdomain at this link: "+ full_url)
