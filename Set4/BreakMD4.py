'''
Created on Jul 3, 2015

@author: mewolot
'''
from Set2.Detection import randKey
from MD4 import MD4 as md4
from HackMD4 import MD4 as hackedMD4
from __builtin__ import True
def encodeData(data):
    data = data.replace(";","")
    data = data.replace("=","")
    Str ="comment1=cooking%20MCs;userdata=" + data + ";comment2=%20like%20a%20pound%20of%20bacon"
    return Str
def Verify(Str, Key, hash, length):
    m = md4()
    m.update(Key + Str)
    hashed = m.digest()
    if hash == hashed:
        return True
    return False

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
    first = Binary[:len(Binary) - 8]
    last = [Binary[len(Binary) - 1], Binary[len(Binary) - 2]] + Binary[len(Binary) - 8: len(Binary) - 2]
    Binary = first + last
    glueStr = ""
    for b in Binary:
        glueStr += chr(int(b,2))
    return glueStr
Str = "foo"

encoded = encodeData(Str)
dLen = len(encoded)
Key = randKey()
m = md4()
m.update(Key + encoded)
secret =  m.digest()
print secret
Segments = [secret[i:i+8] for i in range(0,32,8)]
Hex = []
for s in Segments:
    str = ""
    for i in range(0,len(s),2):
        str = s[i] + s[i+1] + str
    dec = int(str,16)
    Hex.append(dec)
h = hackedMD4(Hex)
HackedStr = ";admin=true;"
h.update(HackedStr, (dLen + 16) * 8)

hack = h.digest()

print hack
m = md4()
m.update(Key + encoded + reversePad(dLen,16) + HackedStr)
print m.digest()

CheckStr = encoded + reversePad(dLen, 16) + HackedStr
print Verify(CheckStr, Key, hack, (dLen + 16) * 8)