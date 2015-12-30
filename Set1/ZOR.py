'''
Created on Jul 13, 2015

@author: mewolot
'''
from FreqAnal import englishFreqMatchScore as freq
import numpy

cipherText = ""
file = open("encrypted","r")
for line in file:
    cipherText += line.strip("\n")
print cipherText
PlainTexts = []
for i in range(256):
    current = ""
    for c in cipherText:
        p = chr(ord(c) ^ i)
        current += p
    score = freq(current)
    PlainTexts.append((current,score))

plains = numpy.sort(PlainTexts,1)
for p in plains:
    print p[1]