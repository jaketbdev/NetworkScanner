#!/usr/bin/env python
from ip_address import ip
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())

scan(ip)
