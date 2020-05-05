# -*- coding: utf-8 -*-

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

#mp.pyplot.imshow(imgBig, cmap = 'gray') #teilaufgabe 1

imgInvert = np.invert(img) 

#mp.pyplot.imshow(imgInvert, cmap = 'gray') #teilaufgabe 2

imgcropped = img[325:450, 150:350]
imgcropped[75,150] = 0 #wird angezeigt
mp.pyplot.imshow(img, cmap = 'gray') #teilaufgabe 3

Array = np.zeros((512,512))
Array[325:450, 150:350] = 1
img = img*Array
mp.pyplot.imshow(img, cmap = 'gray') #teilaufgabe 4