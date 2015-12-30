'''
Created on Jul 2, 2015

@author: mewolot
'''
from Crypto.Cipher import AES
from Set2.Detection import randKey
from Set2.ECB2CBC import EncryptCBCNoPad as CBCEncrypt
from Set2.ECB2CBC import DecryptCBCNoPad as CBCDecrypt

def strXOR(str1, str2):
    ans = ""
    for i,j in zip(str1, str2):
        ans += chr(ord(i) ^ ord(j))
    return ans

def isBadString(str):
    for c in str:
        if ord(c) > 127:
            return True
    return False

file = open("SampleText","r")
plainText = ""
for line in file:
    plainText += line
file.close()

plainText = plainText[:48]
print plainText
Key = randKey()
print Key
cipherText = CBCEncrypt(plainText, Key, Key)
C1, C2, C3 = cipherText[:16], cipherText[16:32], cipherText[32:]
print C1
print C1 + chr(0) * 16 + C1
xPlain = CBCDecrypt(C1 + chr(0) * 16 + C1, Key, Key)
print isBadString(xPlain)
Pn1, Pn2, Pn3 = xPlain[:16], xPlain[16:32], xPlain[32:]
print strXOR(Pn1, Pn3)