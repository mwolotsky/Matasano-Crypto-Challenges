'''
Created on Jul 7, 2015

@author: mewolot
'''
import DiffieHellman as dh
import random as rand
from Set4.Sha1 import sha1
from Crypto.Cipher import AES
import os
from string import join
from Set2.Padding import pad, unPad

p_A = 37
g_A = 5
a = rand.randrange(0,p_A - 1)
A = dh.genPub(p_A, g_A, a)

print "A -> B"
print "Send p, g, A"

p_B = p_A
g_B = g_A
A_B = A
b = rand.randrange(0,p_B - 1)
B = dh.genPub(p_B, g_B, b)

print "B -> A"
print "Send B"

B_A = B
s_A = dh.getShared(p_A, B_A, a)
s_B = dh.getShared(p_B, A_B, b)

hash_A = sha1("%d" % s_A)
hash_B = sha1("%d" % s_B)

key_A = "".join([chr(int(hash_A[i] + hash_A[i+1],16)) for i in range(0,len(hash_A),2)])
key_B = "".join([chr(int(hash_B[i] + hash_B[i+1],16)) for i in range(0,len(hash_B),2)])
key_A = key_A[:16]
key_B = key_B[:16]

iv_A = os.urandom(16)
iv_B = os.urandom(16)

msg_A = "Hello World"
cipher = AES.AESCipher(key_A, AES.MODE_CBC, iv_A)
send_A = cipher.encrypt("".join(pad(msg_A,16))) + iv_A

print "A -> B"
print "Send AES-CBC(SHA1(s)[0:16],iv=random(16),msg)"

received_B = send_A
iv_A_B = received_B[len(received_B) - 16:]
encrypted_A_B = received_B[:len(received_B) - 16]
cipher = AES.AESCipher(key_B, AES.MODE_CBC, iv_A_B)
msg_B = unPad(cipher.decrypt(encrypted_A_B),16)

cipher = AES.AESCipher(key_B, AES.MODE_CBC, iv_B)
send_B = cipher.encrypt("".join(pad(msg_B,16))) + iv_B

print "B -> A"
print "Send AES-CBC(SHA1(s)[0:16],iv=random(16),A's msg)"

received_A = send_B
iv_B_A = received_A[len(received_A) -16:]
encrypted_B_A = received_A[:len(received_A)-16]
cipher = AES.AESCipher(key_A, AES.MODE_CBC, iv_B_A)
msg = unPad(cipher.decrypt(encrypted_B_A),16)

print msg == msg_A == msg_B

print

#Man in the Middle Portion

p_A = 37
g_A = 5
a = rand.randrange(0,p_A - 1)
A = dh.genPub(p_A, g_A, a)

print "A -> M"
print "Send p, g, A"

p_M = p_A
g_M = g_A
A_M = A

print "M -> B"
print "Send p, g, p"

p_B = p_M
g_B = g_M
A_B = p_M
b = rand.randrange(0,p_B -1)
B = dh.genPub(p_B, g_B, b)

print "B -> M"
print "Send B"

B_M = B

print "M -> A"
print "Send p"

B_A = p_M
s_A = dh.getShared(p_A, B_A, a)
hash_A = sha1("%d" % s_A)
key_A = "".join([chr(int(hash_A[i] + hash_A[i+1],16)) for i in range(0,len(hash_A),2)])
key_A = key_A[:16]
iv_A = os.urandom(16)
msg_A = "Hello World"
cipher = AES.AESCipher(key_A, AES.MODE_CBC, iv_A)
send_A = cipher.encrypt("".join(pad(msg_A,16))) + iv_A

print "A -> M"
print "Send AES-CBC(SHA1(s)[0:16],iv=random(16),msg) + iv"

send_M = send_A

print "M -> B"
print "Relay to B"

received_B = send_M

s_B = dh.getShared(p_B, A_B, b)
hash_B = sha1("%d" % s_B)
key_B = "".join([chr(int(hash_B[i] + hash_B[i+1],16)) for i in range(0,len(hash_B),2)])
key_B = key_B[:16]
iv_B = os.urandom(16)

iv_A_B = received_B[len(received_B) - 16:]
encrypted_A_B = received_B[:len(received_B) - 16]
cipher = AES.AESCipher(key_B, AES.MODE_CBC, iv_A_B)
msg_B = unPad(cipher.decrypt(encrypted_A_B),16)
cipher = AES.AESCipher(key_B, AES.MODE_CBC, iv_B)
send_B = cipher.encrypt("".join(pad(msg_B,16))) + iv_B

print "B -> M"
print "Send AES-CBC(SHA1(s)[0:16],iv=random(16),A's msg) + iv"

received_M = send_B

print "M -> A"
print "Relay to A"

received_A = received_M
iv_B_A = received_A[len(received_A) -16:]
encrypted_B_A = received_A[:len(received_A)-16]
cipher = AES.AESCipher(key_A, AES.MODE_CBC, iv_B_A)
msg = unPad(cipher.decrypt(encrypted_B_A),16)

hash_M = sha1("0")
key_M = "".join([chr(int(hash_M[i] + hash_M[i+1],16)) for i in range(0,len(hash_M),2)])
key_M = key_M[:16]
iv_M = received_M[len(received_M)-16:]
encrypted_M = received_M[:len(received_M)-16]
cipher = AES.AESCipher(key_M, AES.MODE_CBC, iv_M)
msg_M = unPad(cipher.decrypt(encrypted_M),16)

print msg == msg_A == msg_B == msg_M