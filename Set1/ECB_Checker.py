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

def fullHamDist(List, Blocksize):
    subLists = []
    for i in range(0,len(List),Blocksize):
        subLists.append(List[i:i + Blocksize])
    Average = 0
    num = 0
    for i in range(0,len(subLists)):
        for j in range(1,len(subLists)):
            Average += op.binhamdist(subLists[i], subLists[j])
            num += 1
    Average /= float(num)
    return Average

# file = open("FIND_ECB","r")
# hexStr = ""
# BinaryList = []
# for line in file:
#     hexStr = line
#     binStr = binascii.a2b_hex(hexStr.strip("\n"))
#     BinaryList.append(binStr)
# file.close()
#  
# Distances = []
# Index = 1
# for list in BinaryList:
#     avgDist = fullHamDist(list,16)
#     Distances.append((avgDist,Index))
#     Index += 1
#  
# Minimum, Index = op.indexOfMinimum(Distances)
# print Distances[Index-1]
# print Index