'''
Created on Jul 2, 2015

@author: mewolot
'''
from EasySha import Verify
from Sha1 import sha1 as sha
from Sha1 import hackedSha
from Set2.Detection import randKey

def encodeData(data):
    data = data.replace(";","")
    data = data.replace("=","")
    Str ="comment1=cooking%20MCs;userdata=" + data + ";comment2=%20like%20a%20pound%20of%20bacon"
    return Str

def reversePad(dLen, kLen):
    bits = (dLen + kLen) * 8
    num = bits + 1
    fPad = 0
    Padding = "1"
    while num % 512 != 448:
        num += 1
        fPad += 1
    Padding += "0" * fPad
    Padding += "{0:064b}".format(bits)
    Binary = [Padding[i:i+8] for i in range(0,len(Padding),8)]
    glueStr = ""
    for b in Binary:
        glueStr += chr(int(b,2))
    return glueStr

Str = "foo"

encoded = encodeData(Str)
dLen = len(encoded)
Key = randKey()
secret = sha(Key + encoded)
Segments = [secret[i:i+8] for i in range(0,40,8)]
Hex = []
for s in Segments:
    dec = int(s,16)
    Hex.append(dec)
HackedStr = ";admin=true;password=true;"
hack = hackedSha(HackedStr, Hex, (dLen + 16) * 8)
print hack
print sha(Key + encoded + reversePad(dLen,16) + HackedStr)
CheckStr = encoded + reversePad(dLen, 16) + HackedStr
print Verify(CheckStr, Key, hack)
#print Verify(encoded, Key, secret)