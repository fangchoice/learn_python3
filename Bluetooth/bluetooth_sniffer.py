

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sudo pip install scapy
from scapy.all import *


# disable verbose mode
conf.verb = 0



def parse_packet(packet):
    """parse packet from sniffer.
    """
    if packet and packet.haslayer('UDP'):
        ip = packet['IP']
        udp = packet['UDP']

        # do something here
        data = udp[Raw].load
        print(data)


def udp_sniffer():
    """start a udp sniffer.
    """
    print("[*] sniff port 5612 ")
    # sniff(filter="udp port 5612", prn=parse_packet, iface='lo0')
    sniff(
        filter="udp port 5612",
        prn=parse_packet,
        iface=r'\Device\NPF_{F71EEA2C-0192-402B-AFBB-DD77C15A5DB2}'
    )


if __name__ == '__main__':
    udp_sniffer()

# reference
# https://github.com/secdev/scapy/
# https://stackoverflow.com/questions/462439/packet-sniffing-in-python-windows
