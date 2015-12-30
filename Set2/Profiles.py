'''
Created on Jun 21, 2015

@author: mewolot
'''
import Detection
from Crypto.Cipher import AES
from Crypto.Cipher.AES import AESCipher
import Padding

def decode(Str):
    Info = Str.split("&")
    Dict = {}
    for item in Info:
        mid = item.index("=")
        key = item[0:mid]
        value = item[mid+1:]
        Dict[key] = value
    return Dict

def profile_for(Str):
    Info = Str.split("&")
    Dict = {}
    Dict["email"] = Info[0]
    Dict["uid"] = hash(Info[0])
    if len(Info) > 1:
        if "role" in Info[1]:
            mid = Info[1].index("=")
            role = Info[1][mid + 1:]
        else:
            role = "user"
    else:
        role = "user"
    Dict["role"] = role
    return encode(Dict)

def encode(Dict):
    Keys = Dict.keys()
    Str = Keys[0] + "=" + "%s" % Dict[Keys[0]]
    for i in range(1,len(Keys)):
        Str += "&"
        Str += Keys[i] + "=" + "%s" % Dict[Keys[i]]
    return Str

def encryptProfile(Str):
    Encoded = profile_for(Str)
    Blocks = Padding.pad(Encoded, 16)
    plainText = ""
    for Block in Blocks:
        plainText += Block
    Key = Detection.randKey()
    cipher = AES.AESCipher(Key,AES.MODE_ECB)
    CipherText = cipher.encrypt(plainText)
    return CipherText, Key

def decryptProfile(CipherText, Key):
    cipher = AES.AESCipher(Key, AES.MODE_ECB)
    Encoded = cipher.decrypt(CipherText)
    endMessage = Padding.unPad(Encoded, 16)
    return decode(endMessage)

CipherText, Key = encryptProfile("foo@bar.com&role=admin")
print CipherText
print decryptProfile(CipherText,Key)
    