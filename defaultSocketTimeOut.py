import socket

"""
setting and getting default socket timeout

In this code snippet, we have first created a socket object by passing the socket family and 
socket type as the first and second arguments of the socket constructor. Then, youcan 
get the socket timeout value by calling gettimeout()and alter the value by calling the 
settimeout()method. The timeout value passed to the settimeout()method can be in 
seconds (non-negative float) or None. This method is used for manipulating theblocking-socket 
operations. Setting a timeout of Nonedisables timeouts on socket operations.

"""


def time_out():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default Socket timeout: %s" % s.gettimeout())
    s.settimeout(100)

    print("Current socket timeout is: %s " % s.gettimeout())


if __name__ == '__main__':
    time_out()
