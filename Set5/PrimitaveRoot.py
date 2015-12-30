'''
Created on Jun 8, 2015

@author: mewolot
'''

def PrimativeRoots(n):
    Set = [i for i in range(1,n)]
    Roots = []
    for i in range(1,n):
        Pos = []
        for j in range(1,n):
            Pos.append(i ** j % n)
        if sorted(Pos) == Set:
            Roots.append(i)
    return Roots
        

# print PrimativeRoots(17)