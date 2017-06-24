import socket
"""
If you know the port number of a network service, you can find the service name using the 
getservbyport()socket class functionfrom the socket library. You can optionally give the 
protocol name when calling this function.

Let us define a find_service_name()function, where the getservbyport()socket 
class function will be called with a few ports, for example, 80, 25. We can use Python's 
for-inloop construct.

"""

def find_service():
    for protocol in ['tcp']:
        for port in [80, 25, 53]:
            print("Port: %s => Service Name: %s" % (port, socket.getservbyport(port, protocol)))
            # print("Port: %s => services name: %s " %(53, socket.getservbyport(53, 'udp')))


if __name__ == '__main__':
    find_service()
