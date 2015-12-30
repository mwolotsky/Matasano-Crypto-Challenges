'''
Created on Jun 23, 2015

@author: mewolot
'''
import CTR
from Set2.Detection import randKey
import binascii
import Set1.Single_Byte as sb
from Set1.FreqAnal import englishFreqMatchScore as score
import random


def Scoring(Str):
    maxScore = 0
    ScoreList = []
    for i in range(256):
        newStr = ""
        for j in Str:
            newStr += chr(i ^ ord(j))
        curScore = score(newStr)
        if curScore > maxScore:
            maxScore = curScore
            ScoreList = [newStr]
        elif curScore == maxScore:
            ScoreList.append(newStr)
    return ScoreList

Key = randKey()
Nonce = chr(0) * 16
Messages = []
file = open("CTRSub","r")
for line in file:
    Messages.append(binascii.a2b_base64(line))
file.close()
cipherTexts = []
for message in Messages:
    cipherTexts.append(CTR.encryptCTR(Key, Nonce, message))

newBlock = []

maxLen = 0
for text in cipherTexts:
    if len(text) > maxLen:
        maxLen = len(text)

for i in range(maxLen):
    Str = ""
    for j in range(len(cipherTexts)):
        if len(cipherTexts[j]) > 0:
            Str += cipherTexts[j][0]
            cipherTexts[j] = cipherTexts[j][1:]
    newBlock.append(Str)
    
#Each in NewBlock has been XORD with same varaible        
for str in newBlock:
    print Scoring(str)
