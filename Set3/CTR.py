'''
Created on Jun 22, 2015

@author: mewolot
'''
import binascii
from Crypto.Cipher import AES
import Set2.Detection as s2
import Set2.Padding as p
import Set1.Operations as s1

def encryptCTR(Key, Nonce, plainText):
    cipher = AES.AESCipher(Key,AES.MODE_ECB)
    blockSize = 16
    Blocks = [plainText[i:i+blockSize] for i in range(0,len(plainText),blockSize)]
    Blocks.append(plainText[len(plainText)//blockSize * blockSize:])
    cipherText = ""
    for Block in Blocks:
#         print [ord(i) for i in Nonce]
        Xstr = cipher.encrypt(Nonce)
        for i,j in zip(Xstr, Block):
            cipherText += chr(ord(i) ^ ord(j))
        Nonce = chr(0) * 8 + chr(ord(Nonce[8]) + 1) + chr(0) * 7
    return cipherText

def controlledCTR(Key, Counter, plainText):
    cipher = AES.AESCipher(Key,AES.MODE_ECB)
    blockSize = 16
    Blocks = [plainText[i:i+blockSize] for i in range(0,len(plainText),blockSize)]
    Blocks.append(plainText[len(plainText)//blockSize * blockSize:])
    cipherText = ""
    for Block in Blocks:
#         print [ord(i) for i in Nonce]
        Xstr = cipher.encrypt(Counter)
        for i,j in zip(Xstr, Block):
            cipherText += chr(ord(i) ^ ord(j))
        Nonce = [ord(c) for c in Counter]
        for i in range(1,len(Nonce)):
            if Nonce[len(Nonce) - i] < 255:
                Nonce[len(Nonce) - i] += 1
                break
            else:
                Nonce[len(Nonce) - i] = 0
        Counter = ""
        for i in Nonce:
            Counter += chr(i)
    return cipherText


# Input = "L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=="
# cipherText = binascii.a2b_base64(Input)
# Key = "YELLOW SUBMARINE"
# Nonce = chr(0) * 16
# print encryptCTR(Key, Nonce, cipherText)

