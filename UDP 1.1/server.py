import socket
from math import factorial
UDP_IP = "127.0.0.1"
UDP_PORT = 5002
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    n = int(data)
    print "Received data;","Factory of data is :", factorial(n)
