#!/usr/bin/env python

import socket
import base64
import os

TCP_IP = '127.0.0.1'
TCP_PORT = 5008
BUFSIZE = 32768 

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((TCP_IP, TCP_PORT))
serv.listen(1)

print 'waiting client connected!!'

conn, addr = serv.accept()
print 'Connection address:', addr

if not os.path.exists("C:\Users\Fluck\Desktop\TCP 2.2"+"/image_from_client/"):
        os.makedirs("C:\Users\Fluck\Desktop\TCP 2.2"+"/image_from_client/")
with open("C:\Users\Fluck\Desktop\TCP 2.2""/image_from_client/"+'image.jpg','wb') as myfile:
    while 1:
        data = conn.recv(BUFSIZE)
        if not data: break
        data = base64.b64decode(data) 
        myfile.write(data) 
        print('writing file ....')
        myfile.close() 
        print('finished writing file')
        conn.close() 
        print('client disconnected')
        break 
conn.close()

