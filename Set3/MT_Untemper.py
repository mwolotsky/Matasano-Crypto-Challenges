'''
Created on Jun 26, 2015

@author: mewolot
'''
import RandGen as MT
import time

def unTwist(rand):
    val = rand  
    val = MT.unRShift(val, 18)
    val = MT.unLShift(val, 15, 0xefc60000)
    val = MT.unLShift(val, 7, 0x9d2c5680)
    val = MT.unRShift(val, 11)
    return val

def unTwist8(rand):
    val = rand
    val = MT.unRShift(val, 5)
    val = MT.unLShift(val, 3 , 0xef)
    val = MT.unLShift(val, 2, 0x9d)
    val = MT.unRShift(val, 4)
    return val

# 
# seed = int(time.time())
# List = MT.init(seed)
# Test = []
# for i in range(1,624):
#     val = MT.extract_numbers(List, i)[1]
#     val = unTwist(val)
#     Test.append(val)
# 
# total = len(Test)
# right = 0
# for i,j in zip(List[1:], Test):
#     if i == j:
#         right += 1
# print right / 1.0 / total

    