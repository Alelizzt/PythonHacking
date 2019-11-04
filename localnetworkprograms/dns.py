#!/usr/bin/python

from scapy import *

def findDNS(p):
    if p.haslayer(DNS):
        print p[IP].src, p[DNS].summary()

sniff(prn=findDNS)
