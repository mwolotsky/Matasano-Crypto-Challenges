'''
Created on Jul 7, 2015

@author: mewolot
'''
import DiffieHellman as dh
import random as rand

p = 37
g_1 = 1
g_2 = p
g_3 = p-1

a = rand.randrange(0,p-1)
b = rand.randrange(0,p-1)

A_1 = dh.genPub(p, g_1, a)
A_2 = dh.genPub(p, g_2, a)
A_3 = dh.genPub(p, g_3, a)

B_1 = dh.genPub(p, g_1, b)
B_2 = dh.genPub(p, g_2, b)
B_3 = dh.genPub(p, g_3, b)

s1_A = dh.getShared(p, B_1, a) 
s2_A = dh.getShared(p, B_2, a)
s3_A = dh.getShared(p, B_3, a)

s1_B = dh.getShared(p, A_1, b)
s2_B = dh.getShared(p, A_2, b)
s3_B = dh.getShared(p, A_3, b)

print s1_A == s1_B == 1
print s2_A == s2_B == 0 or s2_A == s2_B == 1
print s3_A == s3_B == 1 or s3_A == s3_B  == p -1
