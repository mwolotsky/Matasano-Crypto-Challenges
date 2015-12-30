'''
Created on Jul 1, 2015

@author: mewolot
'''
import Set3.CTR as CTR
import Set2.Detection as d
import os

def EncryptData(UserData, Key, Counter):
    UserData = UserData.replace(";","")
    UserData = UserData.replace("=","")
    Str ="comment1=cooking%20MCs;userdata=" + UserData + ";comment2=%20like%20a%20pound%20of%20bacon"
    return CTR.controlledCTR(Key, Counter, Str)

def DecryptData(CipherText, Key, Counter):
    return CTR.controlledCTR(Key, Counter, CipherText)


EntryText = "AAAAAAAAAAAA"
Key = d.randKey()
Counter = os.urandom(16)

cText = EncryptData(EntryText,Key,Counter)
desired = ";admin=true;"
newStr = ""
for i in range(32,44):
    number = ord(cText[i]) ^ ord("A") ^ ord(desired[i - 32])
    newStr += chr(number)
newCipherText = cText[:32] + newStr + cText[44:]
    
print DecryptData(newCipherText, Key, Counter)