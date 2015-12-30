'''
Created on Jun 9, 2015

@author: mewolot
'''
from cmath import log
from twisted.conch.openssh_compat import primes

def bitSize(a,b):
    #Finds number of bits of largest number
    if a > b:
        sizenum = a
    else:
        sizenum = b
    size = int((log(sizenum,2)).real) + 1
    return size

#Adds a and b in finite field n
def addition(a,b,n):
    return ((a % n) + (b % n)) % n

#Subtracts b from a in finite field n
def subtraction(a,b,n):
    return addition(a,-1 * b,n)

#Multiplies a by b in finite field n
def multiplication(a,b,n):
    #Number a x 1
    round = abs(a)
    #To check least significant bit of b
    number = abs(b)
    #The total
    total = 0
    while number > 0:
        if (number & 1 == 1):
            total = addition(total,round,n)
        round = round << 1
        number = number >> 1
    if (a < 0 or b < 0) and (a >= 0 or b >=0):
        return total * -1 % n
    return total
        
def gcd(num,prime):
    #a = qn + r
    a = prime
    q = num
    #Default r
    r = a
    while r > 0:
        n = a / q
        r = a % q
        a = q
        q = r
    return a
        
def eea(num, prime):
    i,j = prime,num
    s,t,u,v = 1,0,0,1
    while j != 0:
        q,r = i // j, i % j
        un, vn = s,t 
        s = u - (q * s)
        t = v - (q * t)
        i,j = j,r
        u,v = un, vn 
    d,m,n = i,u,v
    return m

def division(a,b,n):
    newB = eea(b,n)
    return multiplication(a,newB,n)


#Proof of Addition/Subtraction
# print addition(13,57,101)
# print addition(13,9,23)
# print subtraction(13,57,101)
# print subtraction(13,9,23)
    
#Proof of Multiplication
# print multiplication(13,9,23) #Desired 16? I think the answer key I am using is wrong
# print multiplication(13,57,101)
# print multiplication(123,456,2003)    
# print division(77,13,101)
    
# print division(77,13,101)
# print division(13,77,101)
# print division(123,1234,2003)
