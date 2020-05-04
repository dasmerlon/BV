# -*- coding: utf-8 -*-

""""
@author: Abdulssatar Khateb, Felix Swimmer, Merle Hoffmann 
"""

import numpy as np
import matplotlib as mp
import skimage.io as sk

img = sk.imread('mandrill.png')

#mp.pyplot.imshow(img, cmap = 'gray')

imgcropped = img[325:450, 150:350] #Y then X, not the otherway around
#mp.pyplot.imshow(imgcropped, cmap = 'gray')
sk.imsave('mandrillCropped.png', imgcropped)

imgPlusOnePixel = img
imgPlusOnePixel[200,200] = 0
#mp.pyplot.imshow(imgPlusOnePixel, cmap = 'gray')

imgEyesBlack = img
imgEyesBlack[25:100, 100:400] = 0
mp.pyplot.imshow(imgEyesBlack, cmap = 'gray')