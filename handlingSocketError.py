import socket
import sys
import argparse

"""
In any networking application, it is very common that one end is trying to connect, but the 
other party is not responding due to networking media failure or any other reason. The 
Python socket library has an elegant method of handing these errors via the socket.error
exceptions. In this recipe, a few examples are presented.

Let us create a few try-except code blocks and put one potential error type in each block. In 
order to get a user input, the argparse module can be used. This module is more powerful 
than simply parsing command-line arguments using sys.argv. In the try-except blocks, put 
typical socket operations, for example, create a socket object, connect to a server, send data, 
and wait for a reply.
"""


def socketError():


    # setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action="store", dest="host",
                        required=False)
    parser.add_argument('--port', action="store", dest="port",
                        type=int, required=False)
    parser.add_argument('--file', action="store", dest="file",
                        required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file
    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" % e)
        sys.exit(1)
    # Second try-except block -- connect to given host/port
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)


    # Third try-except block -- sending data
    try:
        s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
    except socket.error as e:
        print("Error sending data: %s" % e)
        sys.exit(1)
    while 1:
    # Fourth tr-except block -- waiting to receive data from remote host
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            sys.exit(1)
        if not len(buf):
            break
    # write the received data
    sys.stdout.write(buf)


if __name__ == '__main__':
    socketError()
