

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip install scapy


"""
[{'name': 'Bluetooth Device (Personal Area Network)',
  'win_index': '5',
  'description': 'Bluetooth Network Connection',
  'guid': '{6D052EC7-606C-402D-B103-4E93635E708D}',
  'mac': '00:50:56:E7:29:39',
  'netid': 'Bluetooth Network Connection'},
 {'name': 'Intel(R) 82574L Gigabit Network Connection',
  'win_index': '4',
  'description': 'Ethernet0',
  'guid': '{28B8F286-E5AB-473E-869E-ADE5F342366F}',
  'mac': '00:0C:29:5C:E0:6A',
  'netid': 'Ethernet0'}]
"""

from pprint import pprint
from scapy.arch.windows import get_windows_if_list
from scapy.all import *


conf.verb = 0

def parse_packet(packet):
    if packet and packet.haslayer('UDP'):
        # packet.show()
        udp = packet.getlayer('UDP')
        if udp.haslayer('Raw'):
            data = udp.getlayer('Raw').load
            print(data)    # MTU: 1500 = 28 + 1472
            # udp.show()


def udp_sniffer():
    interfaces = get_windows_if_list()
    pprint(interfaces)

    print('\n[*] start udp sniffer')
    sniff(
        filter="udp port 5612",
        iface=r'Intel(R) 82574L Gigabit Network Connection', prn=parse_packet
    )


if __name__ == '__main__':
    udp_sniffer()
    
    
