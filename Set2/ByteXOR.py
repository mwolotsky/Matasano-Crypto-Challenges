'''
Created on Jun 19, 2015

@author: mewolot
'''
def XOR(Str1, Str2):
    Vals1 = [x for x in Str1]
    Vals2 = [x for x in Str2]
    Vals3 = []
    for i,j in zip(Vals1, Vals2):
        Vals3.append(chr(ord(i) ^ ord(j)))
    fin = ""
    for c in Vals3:
        fin += c
    difference = len(Vals1) - len(Vals2)
    if difference > 0:
        for c in Vals1[(len(Vals1) - difference):]:
            fin += c
    elif difference < 0:
        for c in Vals2[(len(Vals2) + difference):]:
            fin += c
    return fin