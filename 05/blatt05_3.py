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
    
    imgHSI = imgRGB
    
    for x in range(imgRGB.shape[0]):  # Schleife über die Zeilen
        for y in range(imgRGB.shape[1]):
            
            TopEquation = 1/2 * ((imgR[x,y]-imgG[x,y]) + (imgR[x,y] - imgB[x,y]))
            BottomEquation = ((imgR[x,y] - imgG[x,y]) ** 2 + ((imgR[x,y] - imgB[x,y]) * (imgG[x,y] - imgB[x,y]))) ** (1/2)
            
            theta = math.acos(TopEquation/BottomEquation)
            
            if(imgB[x,y] <= imgG[x,y]):
                H = theta / 360 #normieren von 0 bis 1!
            else:
                H = (360 - theta) / 360
            
            S = 1 - (3 * min(imgR[x,y],imgG[x,y],imgB[x,y]/(imgR[x,y] + imgG[x,y] + imgB[x,y])))
            I = (1/3) * (imgR[x,y] + imgB[x,y] + imgG[x,y])
            
            imgHSI[x,y,0] = H
            imgHSI[x,y,1] = S
            imgHSI[x,y,2] = I
    return imgHSI


"""
HSI zu RGB
"""
def HSItoRGB(imgHSI):
    
    imgHSI = scale(imgHSI, 1)
    
    imgH = imgHSI[:,:,0]
    imgS = imgHSI[:,:,1]
    imgI = imgHSI[:,:,2]
    
    imgRGB = imgHSI
    
    for x in range(imgHSI.shape[0]):
        for y in range(imgHSI.shape[1]):
            if(imgH[x,y]>= 0 and imgH[x,y]<(1/3)):
                B = imgI[x,y] * (1-imgS[x,y])
                R = imgI[x,y] * (1 + ((imgS[x,y] * math.cos(imgH[x,y]))/(math.cos(60-(imgH[x,y] * 360))))) #H zwischen 0 und 1 muss zu grad werden
                G = (3 * imgI[x,y]) - (R + B)
                
                imgRGB[x,y,0] = R
                imgRGB[x,y,1] = G
                imgRGB[x,y,2] = B
                
            elif(imgH[x,y]>= (1/3) and imgH[x,y]<(2/3)):
                R = imgI[x,y] * (1-imgS[x,y])
                G = imgI[x,y] * (1 + ((imgS[x,y] * math.cos(imgH[x,y]))/(math.cos(60-(imgH[x,y] * 360)))))
                B = (3 * imgI[x,y]) - (R + G)
                
                imgRGB[x,y,0] = R
                imgRGB[x,y,1] = G
                imgRGB[x,y,2] = B
            else:
                G = imgI[x,y] * (1-imgS[x,y])
                B = imgI[x,y] * (1 + ((imgS[x,y] * math.cos(imgH[x,y]))/(math.cos(60-(imgH[x,y] * 360)))))
                R = (3 * imgI[x,y]) - (G + B)
                
                imgRGB[x,y,0] = R
                imgRGB[x,y,1] = G
                imgRGB[x,y,2] = B
    return imgRGB


"""
Überprüft die Korrektheit eurer Implementierung, indem ihr das Farbbild
mandrillFarbe.png aus dem Moodle vom RGB-Farbraum jeweils in den CMY- bzw. 
den HSI-Farbraum konvertiert und wieder zurückrechnet.
"""
plt.close('all')

mandrill = imread('./mandrillFarbe.png')

imgHSI = RGBtoHSI(mandrill)
imgRGB = HSItoRGB(imgHSI) #Problem! image wird irgendwie als NaN gelesen
print(imgRGB)

plt.imshow(imgRGB)

plt.show()