import socket

"""
Converting integers to and from host to 
network byte order.

Python's socket library has utilities for converting from a network byte order to host byte order 
and vice versa. You may want to become familiar with them, for example, ntohl()/htonl().
Let us define the convert_integer()function, where the ntohl()/htonl()socket class 
functions are used to convert IP address formats.

"""


def convert_int():
    data = 1234
    print(
        "Orignal: %s => Long byte Order: %s => Network Byte Order: %s" % (data, socket.ntohl(data), socket.htonl(data)))
    print(
        "Orignal: %s => Short Byte Order: %s, Network Byte Order: %s" % (data, socket.ntohs(data), socket.htons(data)))


if __name__ == '__main__':
    convert_int()
