'''
Created on Jun 9, 2015

@author: mewolot
'''
file = open("FreqAnal.py",'r')
newFile = []
linenum = 1
for line in file:
    num = line.index('.') + 1 + 1
    newFile.append(line[num:])
    linenum += 1
file.close()
file = open("FreqAnal.py","w")
for line in newFile:
    file.write("%s\n" % line)
file.close()