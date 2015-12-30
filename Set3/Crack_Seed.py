'''
Created on Jun 26, 2015

@author: mewolot
'''

import RandGen as MT
import time
import random

def waitRand():
    delay = random.randrange(20,60)
    time.sleep(delay)
    seed = int(time.time())
    delay = random.randrange(20,60)
    time.sleep(delay)
    return MT.getFirst(seed), seed

maxWait = 150
minWait = 20

rand, verifier = waitRand()
cur = int(time.time())

for i in range(minWait,maxWait):
    test = MT.getFirst(cur - i)
    if test == rand:
        print cur - i
        print verifier
        break
print "Done"