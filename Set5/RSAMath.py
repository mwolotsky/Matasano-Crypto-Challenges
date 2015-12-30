'''
Created on Jul 10, 2015

@author: mewolot
'''
from ModMath import eea, gcd

def rsa(m,e,n):
    return m ** e % n

def product(L):
    prod = 1
    for l in L:
        prod *= l
    return prod

def minus(N,n):
    subList = []
    for v in N:
        if v != n:
            subList.append(v)
    return subList

def crt(C, N):
    Sum = 0
    NT = product(N)
    for c,n in zip(C,N):
        Sum += (c * product(minus(N,n)) * (eea(product(minus(N,n)),n) % n))
#     for c,n in zip(C,N):
#         if Sum % n != c:
#             print "Error CRT"
#             print Sum % n, c, n
#             exit()
    return Sum % NT


P = [11, 17, 41, 53, 27, 47, 31, 37]
m = 55
N = [P[0] * P[3], P[1] * P[4], P[2] * P[5]]
pN = [(P[0] -1) * (P[3] - 1), (P[1] -1) * (P[4] - 1), (P[2] -1) * (P[5] - 1)]
E = [3, 3, 3]
for e,n in zip(E,pN):
    print gcd(e,n)
C = [(m ** e) % n for e,n in zip(E,N)]
result = crt(C,N)
print result ** (1/3.0)