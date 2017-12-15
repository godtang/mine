import numpy as np
import random

def GetMineCounts( row, col ,array,rows,cols):
    if("*" == array[row*16 + col]):
        return "*"
    iCount = 0
    if(row - 1 >= 0):
        if(col - 1 >= 0):
            if("*" == array[(row-1)*16 + col - 1]):
                iCount = iCount + 1
        if("*" == array[(row-1)*16 + col]):
            iCount = iCount + 1
        if(col - 1 < cols):
            if("*" == array[(row-1)*16 + col + 1]):
                iCount = iCount + 1
    if(col - 1 >= 0):
        if("*" == array[row*16 + col - 1]):
            iCount = iCount + 1
    if(col + 1 < cols):
        if("*" == array[row*16 + col + 1]):
            iCount = iCount + 1
    if(row + 1 >= 0):
        if(col - 1 >= 0):
            if("*" == array[(row+1)*16 + col - 1]):
                iCount = iCount + 1
        if("*" == array[(row+1)*16 + col]):
            iCount = iCount + 1
        if(col - 1 < cols):
            if("*" == array[(row+1)*16 + col + 1]):
                iCount = iCount + 1
    return iCount

rows = 16#int(raw_input('����������'))
cols = 40#int(raw_input('����������'))
minecount = 99#int(raw_input('�������������'))
array = []#np.array
iTemp = 0
for i in range(0, rows):
    for k in range(0, cols):
        iRand = random.randint(minecount,rows*cols)
        array.append("#")
while iTemp < minecount:
    iRand = random.randint(0,rows*cols)
    if("#" == array[iRand]):
        array[iRand] = '*'
        iTemp = iTemp + 1
for i in range(0, rows):
    strTemp = ""
    for k in range(0, cols):
        strTemp = strTemp +str( array[i*rows + k])
    print strTemp
for i in range(0, rows):
    strTemp = ""
    for k in range(0, cols):
        strTemp = strTemp +str( GetMineCounts(i,k,array,rows,cols))
    print strTemp
