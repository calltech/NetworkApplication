import socket
"""
Modifying socket's send/receive buffer sizes
First, define two constants: SEND_BUF_SIZE/RECV_BUF_SIZEand then wrap a socket 
instance's call to the setsockopt()method in a function. It is also a good idea to check the 
value of the buffer size before modifying it. Note that we need to set up the send and receive 
buffer size separately.
"""
S_BUFF_SIZE = 90000  # SEND BUFFER SIZE
R_BUFF_SIZE = 90000  # RECEIVE BUFFER SIZE
def buffer_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    # Get the size of the socket's send buffer
    buffsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [Before]:%d" %buffsize)
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_SNDBUF,
    S_BUFF_SIZE)
    sock.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_RCVBUF,
    R_BUFF_SIZE)
    buffsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [After]:%d" %buffsize)
if __name__ == '__main__':
    buffer_size()
