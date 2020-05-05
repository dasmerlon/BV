# -*- coding: utf-8 -*-

import time
import numpy as np
import skimage.io as sk

def RangeCheckWithLoops():
    img = sk.imread('mandrill.png')
    boolArray = np.full((512,512), False)
    xwidth = img.shape[0]
    ywidth = img.shape[1]
    for x in range(xwidth):
        for y in range(ywidth):
            if(200 > img[x,y] > 99):
                boolArray[x,y] = True
    #print(boolArray)     
    

def RangeCheckWithBroadcasting(): 
    img = sk.imread('mandrill.png')
    SmallerArray = np.full((512,512), 99)
    LargerArray = np.full((512,512), 200)
    
    boolArray1 = LargerArray > img
    boolArray2 = img > SmallerArray
    boolArray = boolArray1 == boolArray2
    #print(boolArray)
    
def CheckTimes():
    tic = time.time()
    for x in range(100):
        RangeCheckWithBroadcasting()
    toc = time.time()
    diff = toc-tic
    print(diff)
    
    tic = time.time()
    for x in range(100): #braucht 78 sekunden!!!
        RangeCheckWithLoops()
    toc = time.time()
    diff = toc-tic
    print(diff)
    

CheckTimes()