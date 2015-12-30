'''
Created on Jun 25, 2015

@author: mewolot
'''
import time
import math

def low32(number):
    return number & 0xFFFFFFFF

def low8(number):
    return number & 0xFF

def r15(number):
    return number >> 15

def r30(number):
    return number >> 30

def init8(seed):
    index = 0
    MT = [0 for x in range(624)]
    MT[0] = seed
    for i in range(1,624):
        MT[i] = low8(0x6c078965 * (MT[i-1] ^ r15(MT[i -1])) + i)
    return MT

def init(seed):
    index = 0
    MT = [0 for x in range(624)]
    MT[0] = seed
    for i in range(1,624):
        MT[i] = low32(1812433253 * (MT[i-1] ^ r30(MT[i-1])) + i)
    return MT

def getNext8(val, index):
    next = low8(0x6c078965 * (val ^ r15(val)) + index + 1)
    return next

def extract_numbers(MT, index):
    if index == 0:
        MT = generate_numbers(MT)
    y = MT[index]
    y ^= (y >> 11)
    y ^= (y << 7) & 0x9d2c5680
    y ^= (y << 15) & 0xefc60000
    y ^= (y >> 18)
    index = (index + 1) % 624
    return MT, y, index

def getTwist(orig):
    y = orig
    y ^= (y >> 4)
    y ^= (y << 2) & 0x9d
    y ^= (y << 3) & 0xef
    y ^= (y >> 5)
    return y

def extract_numbers8(MT, index):
    if index == 0:
        MT = generate_numbers(MT)
    y = MT[index]
    y ^= (y >> 4)
    y ^= (y << 2) & 0x9d
    y ^= (y << 3) & 0xef
    y ^= (y >> 5)
    index = (index + 1) % 624
    return MT, y, index

def generate_numbers(MT):
    for i in range(624):
        y = (MT[i] & 0x80000000) + (MT[(i+1) % 624] & 0x7fffffff)
        MT[i] = MT[(i + 397) % 624] ^ (y >> 1)
        if y % 2 != 0:
            MT[i] ^= 2567483615  
    return MT
        
def getFirst(seed):
    MT = init(seed)
    return extract_numbers(MT,1)[1]

def getFirst8(seed):
    MT = init8(seed)
    return extract_numbers8(MT,1)[1]

def binXOR(bin1, bin2, shift):
    if bin1 == "0b":
        dec1 = 0
    else:
        dec1 = int(bin1,2)
    if bin2 == "0b":
        dec2 = 0
    else:
        dec2 = int(bin2,2)
    str = bin(dec1 ^ dec2)
    extra = shift - (len(str) - 2)
    return str[0:2] + extra * "0" + str[2:]

def unRightShiftXOR(val, shift):
    known = bin(val)[0:shift + 2]
    rest = "0b" + bin(val)[shift + 2:]
    last = known
    while len(rest) - 2 >= shift:
        cur = rest[0:shift + 2]
        xor = binXOR(last, cur, shift)
        known += xor[2:]
        last = xor
        rest = "0b" + rest[shift + 2:]
    if len(rest) - 2 > 0:
        last = last[0:len(rest)]
        xor = binXOR(last, rest, len(rest) - 2)
        known += xor[2:]
    return int(known,2)


def unLeftShiftXOR(val, shift, mask):
    reversed = "0b" + (bin(val)[2:])[::-1]
    known = reversed[0:shift + 2]
    rest = "0b" + reversed[shift + 2:]
    last = known
    mask = bin(mask)
    mask = mask[:len(mask)-shift]
    difference = len(rest) - len(mask)
    for i in range(difference):
        mask = "0b0" + mask[2:]
    revmask = "0b" + (mask[2:])[::-1]
    while len(rest) - 2 >= shift:
        cur = rest[0:shift + 2]
        curmask = revmask[0:shift + 2]
        xand = bin(int(last,2) & int(curmask,2))
        xor = binXOR(cur,xand,shift)
        known += xor[2:]
        last = xor
        rest = "0b" + rest[shift + 2:]
        revmask = "0b" + revmask[shift+2:]
    if len(rest) - 2 > 0 or (len(revmask) - 2 > 0 and len(rest) == 2):
        if len(rest) == 2:
            if len(rest) > len(revmask):
                ln = len(rest)
            else:
                ln = len(revmask)
        else:
            ln = len(rest)
        last = last[0:ln]
        revmask = revmask[0:ln]
        xand = bin(int(last,2) & int(revmask,2))
        xor = binXOR(rest, xand, ln - 2)
        known += xor[2:]
    back = "0b" + (known[2:])[::-1]
    return int(back,2)

def unRShift(num, shift):
    lg = int(math.log(num,2)) + 1
    val = (num >> (lg - shift)) & (2 ** shift - 1)
    rest = num & ((2 ** (lg - shift)) - 1)
    lr = lg - shift
    known = val
    while lr > 0:
        sh = lr - shift
        if sh > 0:
            ans = (val << sh) ^ rest
            val = ans >> sh
            rest = rest & (2 ** sh - 1)
        else:
            ans = (val >> sh * -1) ^ rest
            val = ans
        if sh > 0:
            known = (known << shift) ^ val  
        else:
            known = (known << (shift + sh)) ^ val 
        lr -= shift
    return known

def unLShift(num, shift, mask):
    lg = int(math.log(num,2)) + 1
    lm = int(math.log(mask,2)) + 1
    val = num & ((2 ** shift) - 1)
    rest = num >> shift
    lr = lg - shift
    lc = shift
    mask = mask >> shift
    known = val
    lm -= shift
    while lm > 0:
        nRest = rest & ((2 ** shift) - 1)
        nMask = mask & ((2 ** shift) - 1)
        val = (nMask & val) ^ nRest
        known = known ^ (val << lc)
        lc += shift
        rest = rest >> shift
        mask = mask >> shift
        lm -= shift
        lr -= shift
    return known


        