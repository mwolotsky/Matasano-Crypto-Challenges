'''
Created on Jun 21, 2015

@author: mewolot
'''
from Crypto.Cipher import AES
import Detection
import binascii
import Padding

def ECB_Encrypt(Message, Key, Addition):
    plain = Addition + Message
    Blocks = Padding.pad(plain, 16)
    plainText = ""
    for Block in Blocks:
        plainText += Block
    cipher = AES.AESCipher(Key, AES.MODE_ECB)
    return cipher.encrypt(plainText)

def findByte(cipherText, knownStr, Key):
    for i in range(256):
        current = knownStr + chr(i)
        testCipher = ECB_Encrypt(current, Key, "")
        if testCipher == cipherText[0:16]:
            return chr(i)
    print "Error"
    return None

def findAll(Message, Key, blockSize):
    Chars = []
    for i in range(len(Message)):
        if i % blockSize == 0:
            newMessage = Message[i:]
        cipherText = ECB_Encrypt(newMessage, Key, "A" * ((blockSize - (i % blockSize) - 1)))
        knownStr = "A" * (blockSize - (i % blockSize) - 1)
        for j in range(i % blockSize):
            knownStr += Chars[j + (i / blockSize) * blockSize]
        print knownStr
        Chars.append(findByte(cipherText, knownStr, Key))
        print Chars
        
    return Chars
         
# Key = Detection.randKey()
# Message = ""
# file = open("ECBText","r")
# for line in file:
#     Message += line.strip("\n")
# file.close()
# Message = binascii.a2b_base64(Message)
# myString = "A"
# increment = "A"
# Last = ""
# blockSize = 0
# for i in range(32):
#     Current = ECB_Encrypt(Message, Key, myString)
#     if len(Last) > i:
#         if Current[0:i] == Last[0:i]:
#             blockSize = i
#             break  
#     Last = Current
#     myString += increment
# print blockSize
# myString = "A"
# cipherText = ECB_Encrypt(Message, Key, myString * 32)
# score = Detection.ECBScore(cipherText, blockSize)
# if score > 0:
#     print "ECB Mode"
#  
# myString = "A" * (blockSize - 1)
# cipherText = ECB_Encrypt(Message, Key, myString)
# print findByte(cipherText,myString,Key)
# print findAll(Message,Key,16)