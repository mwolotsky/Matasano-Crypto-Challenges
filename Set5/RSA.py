'''
Created on Jul 7, 2015

@author: mewolot
'''
import gensafeprime as prime
from ModMath import eea,gcd

# p = 7919 
# q = 6271
# n = p * q
# et = (p-1) * (q-1)
# e = 97
# #GCD must be 1 to work
# print gcd(e,et)
# d = eea(e,et) % et
# pub = e,n
# priv = d,n
# 
# plaintext = 1337808
# c = plaintext ** e % n
# m = c ** d % n
# print plaintext, c, plaintext == m
# print
# print c,n,d
# print c ** d % n
# print

p = 17
q = 11
n = p * q
et = (p-1) * (q-1)
e = 7
print gcd(e,et)
print eea(e,et) % et