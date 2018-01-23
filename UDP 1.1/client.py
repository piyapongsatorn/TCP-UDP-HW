import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5002
MESSAGE = str(5)

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "Data is:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
 
