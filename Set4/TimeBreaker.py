import socket 
import time
import WebFunctions as web

host = 'localhost' 
port = 50001
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port)) 

userData = "HelloWorld"
str = "\x00" * 20
CONST_TIME = 0
average = 0
for i in range(10):
    now = time.time()
    s.send(web.fakeEncode(userData, str))
    data = s.recv(size)
    after = time.time()
    average += after - now
CONST_TIME = average / 10.0
cur = -1
while True:
    now = time.time()
    s.send(web.fakeEncode(userData,str))
    data = s.recv(size)
    after = time.time()
    passed = after - now
    if int(data) == 200:
        print "Got it!"
        print str
        break
    elif int(data) != 500:
        print "ERROR!"
        break
    instance = int((passed // .05))
    if instance > len(str):
        instance = len(str) - 1
    temp = ord(str[instance])
    temp = (temp + 1) % 256
    str = str[0:instance] + chr(temp) + str[instance + 1:]
    if instance > cur:
        print [ord(i) for i in str]
        cur = instance
    
    
        
        
s.close() 
