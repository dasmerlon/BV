# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 3 — Farbräume umrechnen in Python

Schreibt vier Python-Funktionen, die jeweils eine der folgenden Umrechnungen 
zwischen Farbräumen für ein ganzes Bild durchführen:
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
import math


def scale(img, K):
    img_m = img - np.min(img)
    img_s = K * (img_m / np.max(img_m))
    return img_s

"""
RGB zu CMY
"""
def RGBtoCMY(imgRGB):
    imgCMY = 1 - scale(imgRGB, 1)
    return imgCMY


"""
CMY zu RGB
"""
def CMYtoRGB(imgCMY):
    imgRGB = 1 - scale(imgCMY, 1)
    return imgRGB


"""
RGB zu HSI
"""
def RGBtoHSI(imgRGB):
    imgRGB = scale(imgRGB, 1)
    imgR = imgRGB[:,:,0]
    imgG = imgRGB[:,:,1]
    imgB = imgRGB[:,:,2]
    pass


"""
HSI zu RGB
"""
def HSItoRGB(imgHSI):
    pass


"""
Überprüft die Korrektheit eurer Implementierung, indem ihr das Farbbild
mandrillFarbe.png aus dem Moodle vom RGB-Farbraum jeweils in den CMY- bzw. 
den HSI-Farbraum konvertiert und wieder zurückrechnet.
"""
plt.close('all')

mandrill = imread('./mandrillFarbe.png')
plt.imshow(mandrill)

plt.show()