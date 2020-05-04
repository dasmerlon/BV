# -*- coding: utf-8 -*-

""""
@author: Abdulssatar Khateb, Felix Swimmer, Merle Hoffmann 
"""

import numpy as np
import matplotlib as mp
import skimage.io as sk

img = sk.imread('mandrill.png')

imgFlipLeft = np.fliplr(img)
imgFlipTop = np.flipud(img)
imgBothFlips = np.flipud(imgFlipLeft)

imgBig = np.resize(img, (1024,1024))
imgBig[:512,:512] = img
imgBig[:512,512:1024] = imgFlipLeft
imgBig[512:1024, :512]= imgFlipTop
imgBig[512:1024, 512:1024] = imgBothFlips

#mp.pyplot.imshow(imgBig, cmap = 'gray')

imgInvert = np.invert(img) 

#mp.pyplot.imshow(imgInvert, cmap = 'gray')

imgcropped = img[325:450, 150:350]
imgcropped[75,150] = 0 #wird nicht angezeigt

Array = np.zeros((512,512))
Array[325:450, 150:350] = 1
img = img*Array
#mp.pyplot.imshow(img, cmap = 'gray')