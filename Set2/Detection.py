'''
Created on Jun 19, 2015

@author: mewolot
'''
import os
import Padding
import random
from Crypto.Cipher import AES
from Set1.ECB_Checker import fullHamDist
import numpy
import ByteXOR
import Set1.Operations as op

def randKey():
    key = os.urandom(16)
    return key

def encECB(Message, Key):
    Blocks = Padding.pad(Message, 16)
    plainText = ""
    for Block in Blocks:
        plainText += Block
    cipher = AES.AESCipher(Key, AES.MODE_ECB)
    cipherText = cipher.encrypt(plainText)
    return cipherText

def encCBC(Message, Key):
    Blocks = Padding.pad(Message, 16)
    IV = os.urandom(16)
    plainText = ""
    for Block in Blocks:
        plainText += Block
    cipher = AES.AESCipher(Key, AES.MODE_CBC, IV)
    cipherText = cipher.encrypt(plainText)
    return cipherText

def randEnc(Message):
    Key = randKey()
    choice = random.randint(0,1)
    front = random.randint(5,10)
    end = random.randint(5,10)
    frontStr = os.urandom(front)
    endStr = os.urandom(end)
    Message = frontStr + Message + endStr
    if choice:
        return encECB(Message, Key), "ECB"
    else:
        return encCBC(Message, Key), "CBC"
    
def CBCHam(Message, BlockLength):
    Blocks = [Message[i:i+BlockLength] for i in range(0,len(Message),BlockLength)]
    Average = 0
    num = 0
    for i in range(1,len(Blocks)):
        Average += op.binhamdist(Blocks[i], Blocks[i-1])
        num += 1
    Average /= float(num)
    return Average

def ECBScore(CipherText, Blocksize):
    Blocks = [CipherText[i:i+Blocksize] for i in range(0,len(CipherText),Blocksize)]
    score = 0
    for Block in Blocks:
        score += (Blocks.count(Block) - 1.0) / Blocks.count(Block) / 1.0
    return score
    
# file = open("DetectionTest","r")
# List = []
# plainText = ""
# for line in file:
#     plainText += line
# file.close()
# 
# Correct = 0
# Total = 0
# for i in range(100):
#     cipherText, type = randEnc(plainText)
#     score = ECBScore(cipherText, 16)
#     print type
#     if score > 0:
#         if type == "ECB":
#             print "Guess Correct"
#             Correct += 1
#             Total += 1
#         else:
#             print "Guess Incorrect"
#     else:
#         if type == "CBC":
#             print "Guess Correct"
#         else:
#             Total += 1
#             print "Guess Incorrect"
# print Correct / Total / 1.0
#     
#     


