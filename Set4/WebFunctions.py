'''
Created on Jul 6, 2015

@author: mewolot
'''
from hashlib import sha1
import hmac
from string import join
import time

def mac(data, key):
    hashed = hmac.new(key, data, sha1)
    return hashed.digest()

def encodeURL(file, key):
    sig = mac(file, key)
    return "http://localhost:9000/test?file=" + file + "&signature=" + sig

def fakeEncode(file, sig):
    return "http://localhost:9000/test?file=" + file + "&signature=" + sig

def decodeURL(data, key):
    filedex = data.index("=") + 1
    endex = data.index("&")
    file = data[filedex:endex]
    data = data[endex:]
    sigdex = data.index("=") + 1
    sig = data[sigdex:]
    gensig = mac(file, key)
    if insecure_compare(sig,gensig):
        return True
    return False

def insecure_compare(sig1, sig2):
    for i,j in zip(sig1,sig2):
        if i != j:
            return False
        time.sleep(.05)
    print "Got it"
    return True