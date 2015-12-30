'''
Created on Jun 21, 2015

@author: mewolot
'''
import Padding
from Crypto.Cipher import AES
import Detection
import binascii
import random
import os
import ECBCracker

def ECB_Encrypt(Message, Key, Addition, Rand):
    plain = Rand + Addition + Message
    Blocks = Padding.pad(plain, 16)
    plainText = ""
    for Block in Blocks:
        plainText += Block
    cipher = AES.AESCipher(Key, AES.MODE_ECB)
    return cipher.encrypt(plainText)

def BlockAndOffset(Message, Key, Rand):
    Addition = "A"
    Increment = "A"
    Last = ECB_Encrypt(Message, Key, "", Rand)
    for blockSize in range(32):
        for offset in range(blockSize):
            cipherText = ECB_Encrypt(Message, Key, Addition * offset + Addition * blockSize * 2, Rand)
            if cipherText[blockSize:blockSize * 2] == cipherText[blockSize*2:blockSize*3]:
                return blockSize, offset
    print "Error"
    return None, None

def findByte(cipherText, knownStr, Key, Rand):
    for i in range(256):
        current = knownStr + chr(i)
        testCipher = ECB_Encrypt(current, Key, "", Rand)
        if testCipher == cipherText[0:32]:
            return chr(i)
    print "Error"
    return None

def findAll(Message, Key, blockSize, Rand):
    Chars = []
    for i in range(len(Message)):
        if i % blockSize == 0:
            newMessage = Message[i:]
        cipherText = ECB_Encrypt(newMessage, Key, "A" * offset + "A" * ((blockSize - (i % blockSize) - 1)),Rand)
        knownStr = "A" * offset + "A" * (blockSize - (i % blockSize) - 1)
        for j in range(i % blockSize):
            knownStr += Chars[j + (i / blockSize) * blockSize]
        print knownStr
        Chars.append(findByte(cipherText, knownStr, Key, Rand))
        print Chars
        
    return Chars

Key = Detection.randKey()
Randnum = random.randint(5,10)
Rand = os.urandom(Randnum)
Message = ""
file = open("ECBText","r")
for line in file:
    Message += line.strip("\n")
file.close()
Message = binascii.a2b_base64(Message)

blockSize, offset = BlockAndOffset(Message, Key, Rand)
print blockSize, offset
findAll(Message, Key, blockSize, Rand)