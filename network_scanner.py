#!/usr/bin/env python
from ip_address import ip
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request_broadcast
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()

scan(ip)
