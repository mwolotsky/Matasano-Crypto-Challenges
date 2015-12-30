'''
Created on Jul 1, 2015

@author: mewolot
'''
import binascii
import Set2.Detection as d
import random
import os
from Set3.CTR import controlledCTR as CTR
from Crypto.Cipher import AES


def seek(cipherText, KEY, COUNTER, offset, newPlain):
    cipherBlock = cipherText[offset * 16:offset * 16 + 16]
    newCipher = ""
    count = COUNTER
    cipher = AES.AESCipher(Key,AES.MODE_ECB)
    xor = cipher.encrypt( count)
    for i,j in zip(xor,newPlain):
        newCipher += chr(ord(i) ^ ord(j))
    return newCipher

file = open("random_access_text","r")
plainText = ""
for line in file:
    if line == "\n":
        continue
    plainText += line
file.close()

Key = d.randKey()
count = os.urandom(16)
cipherText = CTR(Key, count, plainText)
known = "Makes No Differe"
newCipher = seek(cipherText,Key,count,0,known)
print newCipher
plain = ""
for i,j in zip(cipherText, newCipher):
    plain += chr(ord(i) ^ ord(j))
print plain
orig = ""
for i,j in zip(plain, known):
    orig += chr(ord(i) ^ ord(j))
print orig
