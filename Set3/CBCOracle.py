'''
Created on Jun 22, 2015

@author: mewolot
'''
import os
import random
from Set2.Detection import randKey
from Set2.Padding import pad
from Set2.Padding import unPad
from Set2.Padding import checkPad
from Crypto.Cipher import AES
import binascii

def RandEncrypt(Key,IV):
    chosen = random.randint(1,10)
    cline = 1
    Message = ""
    file = open("RandStuff","r")
    for line in file:
        if cline == chosen:
            Message = line
        cline += 1
    file.close()
    Binary = binascii.a2b_base64(Message)
    print Binary[16:32]
    print Message[16:32]
    Blocks = pad(Binary,16)
    ready = ""
    for Block in Blocks:
        ready += Block
    cipher = AES.AESCipher(Key, AES.MODE_CBC, IV)
    return cipher.encrypt(ready)

def isValid(CipherText, Key, IV):
    cipher = AES.AESCipher(Key, AES.MODE_CBC, IV)
    plainText = cipher.decrypt(CipherText)
    if unPad(plainText, 16) != "ERROR":
        return True
    return False

def checkValid(CipherText, Key, IV, desired):
    cipher = AES.AESCipher(Key, AES.MODE_CBC, IV)
    plainText = cipher.decrypt(CipherText)
    if checkPad(plainText, 16,desired) != "ERROR":
        return True
    return False

def decryptBlock(Unknown, Key, IV):
    blockSize = len(Unknown)
    Intermediate = []
    scrambled = os.urandom(blockSize - 1)
    extra = ""
    List = []
    Is = []
    for cur in range(1,17):
        for i in range(256):
            test = isValid(scrambled + chr(i) + extra + Unknown, Key, IV)
            if test == True:
                Intermediate.append(chr((i ^ cur)))
                List.append(i)
                Is.append(i)
                break
        val = cur ^ (cur + 1)
        List = [i ^ val for i in List]
        extra = ""
        uList = [i for i in List]
        uList.reverse()
        for item in uList:
            extra += chr(item)
        scrambled = scrambled[:len(scrambled)-1]
    fin = [chr(ord(i) ^ 17) for i in extra]
    print fin
    Is.reverse()
    print Is
    return Intermediate

Key = randKey()
IV = randKey()
cipherText = RandEncrypt(Key, IV)

PlainText = ""
unknown = cipherText[16:32]
intermediate = decryptBlock(unknown, Key, IV)
intermediate.reverse()
print intermediate
first = cipherText[:16]
first = [i for i in first]
print first
for i,j in zip(first,intermediate):
    print chr((ord(i) ^ ord(j))),
