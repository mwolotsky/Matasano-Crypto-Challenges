'''
Created on Jun 19, 2015

@author: mewolot
'''
import binascii

def pad(Message, BlockLength):
    Blocks = []
    while(len(Message) > BlockLength):
        Blocks.append(Message[0:BlockLength])
        Message = Message[BlockLength:]
    if len(Message) != 0:
        padding = BlockLength - len(Message)
        padding = chr(padding)
        Message = Message + (BlockLength - len(Message)) * padding
        Blocks.append(Message)
    return Blocks

def unPad(Message, BlockLength):
    Blocks = [Message[i:i+BlockLength] for i in range(0,len(Message),BlockLength)]
    lastBlock = Blocks[len(Blocks)-1]
    number = lastBlock[len(lastBlock)-1]
    pad = ord(number)
#     for i in Blocks[1]:
#         print ord(i),
#     print
    if pad == 0:
        return "ERROR"
    padded = True
    for i in range(len(lastBlock) - pad, len(lastBlock)):
        if i < len(lastBlock) and i >= 0:
            if lastBlock[i] != number:
                padded = False
        else:
            padded = False
    if (padded):

        Blocks[len(Blocks)-1] = Blocks[len(Blocks) - 1][:len(lastBlock)-pad]
        endMessage = ""
        for Block in Blocks:
            endMessage += Block
        
        return endMessage
    else:
        return "ERROR"
    
def checkPad(Message, BlockLength, desired):
    Blocks = [Message[i:i+BlockLength] for i in range(0,len(Message),BlockLength)]
    lastBlock = Blocks[len(Blocks)-1]
    number = lastBlock[len(lastBlock)-1]
    pad = ord(number)
    padded = True
    if pad == 0:
        return "ERROR"
    for i in range(len(lastBlock) - pad, len(lastBlock)):
        if i < len(lastBlock) and i >= 0:
            if lastBlock[i] != number:
                padded = False
        else:
            if pad == desired:
                print "Something is Wrong"
            padded = False
    if (padded):
        Blocks[len(Blocks)-1] = Blocks[len(Blocks) - 1][:len(lastBlock)-pad]
        endMessage = ""
        for Block in Blocks:
            endMessage += Block
        return endMessage
    else:
        return "ERROR"
# str = pad("YELLOW SUBMARINE",20)[0]
# BLOCK_SIZE = 20
# PADDIN = chr(0x4)
# str = pad("YELLOW SUBMARINE")
# print str
# print len(str)
# str1 = "ICE ICE BABY\x04\x04\x04\x04"
# str2 = "ICE ICE BABY\x05\x05\x05\x05"
# str3 = "ICE ICE BABY\x01\x02\x03\x04"
# print len(unPad(str1,16))
# print len(unPad(str2,16))
# print len(unPad(str3,16))