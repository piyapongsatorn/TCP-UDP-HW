#!/usr/bin/env python

import socket
import base64

TCP_IP = '127.0.0.1'
TCP_PORT = 5008
BUFSIZE = 32768 
file = "ee.jpg" 

bytes1 = open(file,'rb').read() 
bytes1 = base64.b64encode(bytes1) 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect((TCP_IP, TCP_PORT)) 
client.send(bytes1) 
print('finished sent file!!')
client.close() 
