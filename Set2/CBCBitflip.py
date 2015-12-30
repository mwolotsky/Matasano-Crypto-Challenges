'''
Created on Jun 21, 2015

@author: mewolot
'''
import Detection
from Crypto.Cipher import AES
import Padding
from __builtin__ import True

def CBCEncrypt(Message, Key, IV):
    cipher = AES.AESCipher(Key,AES.MODE_CBC,IV)
    return cipher.encrypt(Message)

def CBCDecrypt(CipherText, Key, IV):
    cipher = AES.AESCipher(Key, AES.MODE_CBC, IV)
    return cipher.decrypt(CipherText)

def EncryptData(UserData, Key, IV):
    UserData = UserData.replace(";","")
    UserData = UserData.replace("=","")
    Str ="comment1=cooking%20MCs;userdata=" + UserData + ";comment2=%20like%20a%20pound%20of%20bacon"
    Blocks = Padding.pad(Str, 16)
    PlainText = ""
    for Block in Blocks:
        PlainText += Block
    return CBCEncrypt(PlainText, Key, IV)

def DecryptData(CipherText, Key, IV):
    PlainText = CBCDecrypt(CipherText, Key, IV)
    if ";admin=true;" in PlainText:
        return True
    return False

Key = Detection.randKey()
IV = Detection.randKey()
Message = "Hello World My Name is Max Check"
List = []
for byte in Message:
    List.append(ord(byte))
print List[:16], "\t", List[16:]

cipherText = CBCEncrypt(Message,Key,IV)
byteList = []
for byte in cipherText:
    byteList.append(ord(byte))
print byteList[:16], "\t", byteList[16:]

byteList[0] = byteList[0] ^ 97 ^ 5
cipherText = ""
for byte in byteList:
    cipherText += "%s" % chr(byte)
plainText = CBCDecrypt(cipherText, Key, IV)
byteList = []
for byte in plainText:
    byteList.append(ord(byte))
print byteList[:16], "\t", byteList[16:]

EntryText = "AAAAAAAAAAAA"
cText = EncryptData(EntryText,Key,IV)
desired = ";admin=true;"
newStr = ""
for i in range(16,28):
    number = ord(cText[i]) ^ ord("A") ^ ord(desired[i - 16])
    newStr += chr(number)
newCipherText = cText[:16] + newStr + cText[28:]
    
print DecryptData(newCipherText, Key, IV)