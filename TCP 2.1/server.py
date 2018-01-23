#!/usr/bin/env python

import socket
from math import factorial

TCP_IP = '127.0.0.1'
TCP_PORT = 5056
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    n = int(data)
    print "Received data;","Factory of data is :", factorial(n)
    conn.send(data)  # echo
conn.close()
