'''
Created on Jul 7, 2015

@author: mewolot
'''
from ModMath import eea, gcd
import math

plaintext = 120

p1 = 13
q1 = 23
n1 = p1 * q1
et1 = (p1-1) * (q1-1)
e1 = 7
#GCD must be 1 to work
if gcd(e1,et1) == 1:
    print "Good e"
else:
    print "Bad e"
d1 = eea(e1,et1) % et1
pub1 = e1,n1
priv1 = d1,n1
c1 = plaintext ** e1 % n1
print c1, n1, d1


p2 = 17
q2 = 11
n2 = p2 * q2
et2 = (p2-1) * (q2-1)
e2 = 7
#GCD must be 1 to work
if gcd(e2,et2) == 1:
    print "Good e"
else:
    print "Bad e"
d2 = eea(e2,et2) % et2
pub2 = e2,n2
priv2 = d2,n2
c2 = plaintext ** e2 % n2
print c2, n2, d2

p3 = 37
q3 = 41
n3 = p3 * q3
et3 = (p3-1) * (q3-1)
e3 = 7
#GCD must be 1 to work
if gcd(e3,et3) == 1:
    print "Good e"
else:
    print "Bad e"
d3 = eea(e3,et3) % et3
pub3 = e3,n3
priv3 = d3,n3
c3 = plaintext ** e3 % n3
print c3, n3, d3

print

ms1 = n2 * n3
ms2 = n1 * n3
ms3 = n1 * n2
nF = n1 * n2 * n3

print c1, n1, ms1
if gcd(n1,ms1) == 1:
    print "Good Pair"
else:
    print "Bad Pair"
print c2, n2, ms2
if gcd(n2,ms2) == 1:
    print "Good Pair"
else:
    print "Bad Pair"
print c3, n3, ms3
if gcd(n3,ms3) == 1:
    print "Good Pair"
else:
    print "Bad Pair"


first = eea(ms1,n1) % ms1 * ms1 * c1
second = eea(ms2,n2) %ms2 * ms2 * c2 
third = eea(ms3,n3) %ms3 * ms3 * c3
print first, second, third
final =  (first + second + third)

print final 
cubed = final ** (1/3.0)
print cubed % n3
