#!/usr/bin/python3

import subprocess
from termcolor import colored

def change_mac_address(interface,mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])


def main():
    interface = input("[+] Enter Interface to change MAC address on: ")
    new_mac_address = input("[*] Enter MAC address to change to: ")

    before_change = subprocess.check_output(["ifconfig",interface])
    change_mac_address(interface,new_mac_address)
    after_change = subprocess.check_output(["ifconfig",interface])

    if before_change == after_change:
        print(colored("[!!] Failed to change MAC addres to: "+ new_mac_address,'red'))
        print(colored("[+] MAC address changed to: "+ new_mac_address + " on interface " + interface, 'green'))

main()
