# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 1 — Bildverbesserung

Abbildung 1 zeigt drei Bilder, die im Rahmen dieser Aufgabe mit Hilfe von 
jeweils einer Intensitätstransformation so verbessert werden sollen, dass 
eine vorgegebene Information einfacher aus den Bildern ausgelesen werden kann. 
Überlegt euch dazu zunächst welche Intensitätstransformation passend erscheint
(mit kurzer Begründung) und implementiert diese in jeweils einer 
Python-Funktion.
Hinweis: Für die realistische Darstellung mit Hilfe von matplotlib.imshow 
nutzt die Parameter vmin und vmax. Diese Parameter sorgen dafür, dass die 
Grauwerte des Bildes nicht auf den Bereich 0 bis 255 skaliert werden. Diese 
Skalierung verzerrt den Kontrast künstlich, wenn ein Bild keine hohen oder 
niedrigen Grauwerte hat.  
"""

import numpy as np
import matplotlib.pyplot as plt
import math as math
from skimage.io import imread


img1 = imread('./bildverbesserung/bild1.png')
img2 = imread('./bildverbesserung/bild2.png')
img3 = imread('./bildverbesserung/bild3.png')

plt.close('all')

"""
1. Verbessert die Sichtbarkeit des linken unteren Bildbereichs in Bild 1 
   und ermittelt, wie viele Poller es am Rande einer kleinen Grüninsel in der 
   unteren linken Bildecke gibt?
"""

"""
Gelöst mit einer Power Law Transformation. Es gibt 8 Poller.
"""

beforeAImage = img1
afterAImage = img1 ** 1.55

beforeA = plt.figure(1)
beforeA.suptitle('Image 1 before gamma correction')
plt.imshow(beforeAImage, cmap = 'gray', vmin=0, vmax=255)

afterA = plt.figure(2)
afterA.suptitle("Image 1 after gamma correction")
plt.imshow(afterAImage, cmap = 'gray', vmin=0, vmax=255)


"""
2. Sorgt dafür, dass sich die Skyline in Bild 2 besser vom Himmel abhebt.
"""

"""
Contrast Stretching/Intensity Slicing
"""

def ContrastStretching(image):
    
    result = np.copy(image)
    for x in range(result.shape[0]):
        for y in range(result.shape[1]):
            if(result[x,y] < 145):
                result[x,y] = result[x,y] ** 0.8
            elif(result[x,y] > 150):
                result[x,y] = result[x,y] ** 1.05
    return result

beforeBImage = img2
afterBImageContrastStretching = ContrastStretching(img2)

schwellWert = (beforeBImage > 147) * 255

afterBImage = beforeBImage + schwellWert

beforeB = plt.figure(3)
beforeB.suptitle('Image 2 Before')
plt.imshow(beforeBImage, cmap = 'gray', vmin=0, vmax=255)

afterB = plt.figure(4)
afterB.suptitle("Image 2 with Intensity Level Slicing")
plt.imshow(afterBImage, cmap = 'gray', vmin=0, vmax=255)

afterB = plt.figure(5)
afterB.suptitle("Image 2 with Contrast Stretching")
plt.imshow(afterBImageContrastStretching, cmap = 'gray', vmin=0, vmax=255)


"""
3. Verändert das Bild 3 so, dass in etwa der Bereich der Autobahn in der 
   Bildmitte weiß ist und der Rest des Bildes seine Graufärbung behält.
   Hinweis: Das Ergebnis wird nicht perfekt werden!
"""

"""
Gelöst mit Intensity Level Slicing!
"""

beforeCImage = img3

schwellWert = (beforeCImage > 104) * 255

afterCImage = beforeCImage + schwellWert

beforeC = plt.figure(6)
beforeC.suptitle('Image 3 before Intensity Slicing')
plt.imshow(beforeCImage, cmap = 'gray', vmin=0, vmax=255)

afterC = plt.figure(7)
afterC.suptitle("Image 3 after Intensity Slicing")
plt.imshow(afterCImage, cmap = 'gray', vmin=0, vmax=255)

# für den Grauwertbereich 0 bis 1
#plt.imshow(result, cmap='gray', vmin=0, vmax=1)
# oder für den Grauwertbereich 0 bis 255
#plt.imshow(result, cmap='gray', vmin=0, vmax=255)