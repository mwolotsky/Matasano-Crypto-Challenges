'''
Created on Jul 7, 2015

@author: mewolot
'''
import random as rand
from hashlib import sha256

N = 37
g = 2
k = 3
I = "Email" #Email
P = "Password" #Password
sha = sha256()

S_salt = rand.randrange(0,100)
sha.update(("%d%s" % (S_salt, P)))
S_xH = sha.hexdigest()
S_x = int(S_xH,16) % 100
S_v = g ** S_x % N

a = rand.randrange(0,N-1) % 100
C_A = g ** a % N
S_A = C_A

C_salt = S_salt
b = rand.randrange(0,N-1) % 100
S_B = (k * S_v + g ** b) % N
C_B = S_B

sha  = sha256()
sha.update("%s%s" % (S_A, S_B))
uH = sha.hexdigest()
u = int(uH, 16) % 100

sha = sha256()
sha.update("%d%s" % (C_salt, P))
C_xH = sha.hexdigest()
C_x = int(C_xH, 16) % 100
C_S = (C_B - k * g ** C_x) ** (a + u * C_x) % N
sha = sha256()
sha.update("%d" % C_S)
C_K = sha.hexdigest()

S_S = (S_A * S_v ** u) ** b % N
sha = sha256()
sha.update("%d" % S_S)
S_K = sha.hexdigest()

print C_K, S_K, C_K == S_K

