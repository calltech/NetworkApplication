import socket
from binascii import hexlify

"""
Convert IP address to a different format
"""


def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.9.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpak_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print("IP address: %s => Packed: %s  => Unpacked: %s " % (ip_addr, hexlify(packed_ip_addr), unpak_ip_addr))


if __name__ == '__main__':
    convert_ip4_address()
