'''
Created on Jun 18, 2015

@author: mewolot
'''
import Operations as op
import base64
import binascii
import numpy
import Single_Byte as sb
from Crypto.Cipher import AES

file = open("AES_ECB_Mode","r")
base64Str = ""
for line in file:
    base64Str += line
file.close()
binData = binascii.a2b_base64(base64Str)

Key = "YELLOW SUBMARINE"
Key = bytes(Key)
cipher = AES.AESCipher(Key,AES.MODE_ECB)
print cipher.decrypt(binData)

