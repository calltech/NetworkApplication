import socket

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Host Name is: %s", host_name)
print("Host IP is: %s", host_ip)

print("#" *80)

def get_host_name():
    reqHost = 'www.google.com'
    reqHostIP = socket.gethostbyname(reqHost)
    print("IP of google.com is: %s", reqHostIP)

if __name__  == '__main__':
    get_host_name()