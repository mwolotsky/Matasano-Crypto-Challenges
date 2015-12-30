'''
Created on Jul 2, 2015

@author: mewolot
'''

from Sha1 import sha1 as sha
from Set2.Detection import randKey
import binascii

def Verify(Message, Key, hash):
    hashed = sha(Key + Message)
    if hash == hashed:
        return True
    return False

# Message = "Hello, my name is Max"
# print Message
# Key = randKey()
# hash = sha(Key + Message)
# print Verify(Message, Key, hash)
# Message = Message.replace("e", "d")
# print Message
# print Verify(Message, Key, hash)

# print sha("Password")
# binary = binascii.a2b_hex(sha("Hello World"))
# print binascii.b2a_base64(binary)