'''
Created on Jul 7, 2015

@author: mewolot
'''

import random as rand
from hashlib import sha256
import hmac
import hashlib

g = 5
n = 37
P = "Password"
Salt = ""
b = 1
u = 1

a = rand.randrange(0,n-1)
A = g ** a % n
B = g ** b % n

sha = sha256()
sha.update("%s%s" % (Salt, P))
hX = sha.hexdigest()
x = int(hX,16) % 1000000
S = B ** (a + u * x) % n
sha = sha256()
sha.update("%d" % S)
K = sha.digest()

output = hmac.new(Salt, msg=K, digestmod=hashlib.sha256).hexdigest()

#In a dictionary attack, parse through wordlist and set guess to current word until gHash == output means found password
#Remove the %1000000 for accuracy
sha = sha256()
guess = "Password"
sha.update(guess)
gX = sha.hexdigest()
x = int(gX, 16) % 1000000
gS = (A * (g ** x % n)) % n
sha = sha256()
sha.update("%d" % gS)
gK = sha.digest()
gHash = hmac.new(Salt, msg=gK, digestmod=hashlib.sha256).hexdigest()

print output, gHash, gHash == output