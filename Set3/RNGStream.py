'''
Created on Jun 29, 2015

@author: mewolot
'''
import RandGen as rnd
import os
import random
import MT_Untemper as un

def encrypt(Message, seed):
    MT = rnd.init8(seed)
    cipherText = ""
    i = 1
    for c in Message:
        rand = rnd.extract_numbers8(MT, i)[1]
        cipherText += chr(rand ^ (ord(c)))
        i += 1
    return cipherText

def decrypt(cipherText, seed):
    MT = rnd.init8(seed)
    plainText = ""
    i = 1
    for c in cipherText:
        rand = rnd.extract_numbers8(MT, i)[1]
        plainText += chr(rand ^ (ord(c)))
        i += 1
    return plainText

def findAByte(byte, cipherText, loc):
    for i in range(256):
        j = len(cipherText) - loc
        for c in cipherText[len(cipherText)-loc:]:
            if chr((ord(c) ^ i)) == "A":
                return i, j 
            j += 1
            
def Trace(val, index, cipherText):
    forward = cipherText[index + 1:]
    plainText = chr(ord(cipherText[index]) ^ val)
    for c in forward:
        orig = un.unTwist8(val)
        next = rnd.getNext8(orig, index)
        val = rnd.getTwist(next)
        index += 1
        plainText += chr((ord(c) ^ val))
    back = cipherText[0:index]
    return plainText
        
    
print rnd.getFirst8(1700000)

exit()
known = "A" * 14
num = random.randrange(1,10)
unknown = os.urandom(num)
Message = unknown + known
seed = random.randrange(2 ** 16, 2**17 - 1)
cipherText = encrypt(Message, seed)

rand, index = findAByte("A", cipherText, 14)
print Trace(rand, index, cipherText)