'''
Created on Jun 19, 2015

@author: mewolot
'''
import Padding
from Set1.Operations import rKeyXOR
from Crypto.Cipher import AES
from ByteXOR import XOR
import binascii

def strXOR(str1, str2):
    ans = ""
    for i,j in zip(str1, str2):
        ans += chr(ord(i) ^ ord(j))
    return ans

def EncryptCBCNoPad(plainText, Key, IV):
    cipher = AES.AESCipher(Key, AES.MODE_ECB)
    Blocks = [plainText[i:i + 16] for i in range(0,len(plainText),16)]
    cipherText = ""
    prev = IV
    for Block in Blocks:
        temp = strXOR(Block, prev)
        ciph = cipher.encrypt(temp)
        prev = ciph
        cipherText += ciph
    return cipherText

def DecryptCBCNoPad(cipherText, Key, IV):
    cipher = AES.AESCipher(Key, AES.MODE_ECB)
    Blocks = [cipherText[i:i+16] for i in range(0,len(cipherText),16)]
    plainText = ""
    prev = IV
    for Block in Blocks:
        temp = cipher.decrypt(Block)
        plainText += strXOR(prev, temp)
        prev = Block
    return plainText

def CBCEncrypt(plainText, KEY, IV):
    cipher = AES.AESCipher(KEY, AES.MODE_ECB)
    eBlocks = []
    if len(plainText) % 16 != 0:
        Blocks = Padding.pad(plainText, 16)
    else:
        Blocks = [plainText[i:i + 16] for i in range(0,len(plainText),16)]
    iBlock = Blocks[0]
    cBlock = XOR(iBlock, IV)
    eBlock = cipher.encrypt(cBlock)
    eBlocks.append(eBlock)
    for Block in Blocks[1:]:
        cBlock = rKeyXOR(Block,eBlock)
        print cBlock
        eBlock = cipher.encrypt(cBlock)
        eBlocks.append(eBlock)
    cipherText = ""
    for Block in eBlocks:
        cipherText += Block
    return cipherText
    

def CBCDecrypt(cipherText, KEY, IV):
    cipher = AES.AESCipher(KEY, AES.MODE_ECB)
    dBlocks = []
    Blocks = Padding.pad(cipherText, 16)
    iBlock = Blocks[0]
    cBlock = cipher.decrypt(iBlock)
    dBlock = XOR(cBlock, IV)
    dBlocks.append(dBlock)
    for Block in Blocks[1:]:
        cBlock = cipher.decrypt(Block)
        dBlock = XOR(cBlock, iBlock)
        iBlock = Block
        dBlocks.append(dBlock)
    plainText = ""
    for Block in dBlocks:
        plainText += Block
    return plainText




# IV = "\x00" * 16
# KEY = "YELLOW SUBMARINE"
# file = open("CBCCipherText","r")
# cipherText = ""
# for line in file:
#     cipherText += line.strip("\n")
# file.close()
# # encrypted = CBCEncrypt("Hello World",KEY,IV)
# # print encrypted
# # decrypted = CBCDecrypt(encrypted,KEY,IV)
# # print decrypted
# 
# cipherText = binascii.a2b_base64(cipherText)
# 
# decrypt = CBCDecrypt(cipherText, KEY, IV)
# print decrypt