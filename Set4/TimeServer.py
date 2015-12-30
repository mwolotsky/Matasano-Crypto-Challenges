import socket 
import WebFunctions as web
import os

host = 'localhost' 
port = 50001
backlog = 5 
size = 1024
key = os.urandom(5)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
client, address = s.accept()
while True:    
    data = client.recv(size) 
    if web.decodeURL(data, key):
        client.send("%d" % 200)
        print "Worked"
    else:
        client.send("%d" % 500)

client.close()