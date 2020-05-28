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
afterAImage = img1 ** 1.55 #um den contrast zu erhöhen von dem dunklem bereich, benutzten wir eine exponentialfunktion und 
                           #rechnen jeden pixel hoch einen wert der größer als 1 ist

#beforeA = plt.figure(1)
#beforeA.suptitle('Image 1 before gamma correction')
#plt.imshow(beforeAImage, cmap = 'gray', vmin=0, vmax=255)

afterA = plt.figure(2)
afterA.suptitle("Image 1 after gamma correction")
plt.imshow(afterAImage, cmap = 'gray', vmin=0, vmax=255)


"""
2. Sorgt dafür, dass sich die Skyline in Bild 2 besser vom Himmel abhebt.
"""

"""
Contrast Stretching/Intensity Slicing
"""

def ContrastStretching(image): #eine funktion die auf einer pixel per pixel basis jeden wert auf seinen grauwert untersucht und dann entsprechend, contrast erhöht oder verringert
    
    result = np.copy(image)
    for x in range(result.shape[0]):
        for y in range(result.shape[1]):
            if(result[x,y] < 145): #unsere skyline liegt ca zwischen 145 und 150
                result[x,y] = result[x,y] ** 0.8 #hellere werte sollen heller sein
            elif(result[x,y] > 150):
                result[x,y] = result[x,y] ** 1.05 #dunklere werte sollen dunkler werden
    return result

beforeBImage = img2
afterBImageContrastStretching = ContrastStretching(img2)

schwellWert = (beforeBImage > 147) * 255 #hier einmal noch ein versuch mit intensity level slicing

afterBImage = beforeBImage + schwellWert

#beforeB = plt.figure(3)
#beforeB.suptitle('Image 2 Before')
#plt.imshow(beforeBImage, cmap = 'gray', vmin=0, vmax=255)

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

schwellWert = (beforeCImage > 104) * 255 #wir machen eine maske von allen pixel über dem grauwert 104 und machen die matrix vollständig weiß

afterCImage = beforeCImage + schwellWert #indem wir die maske addieren sorgen wir dafür das alle richtigen pixel automatisch den wert 255
                                         #im fertigen bild haben

#beforeC = plt.figure(6)
#beforeC.suptitle('Image 3 before Intensity Slicing')
#plt.imshow(beforeCImage, cmap = 'gray', vmin=0, vmax=255)

afterC = plt.figure(7)
afterC.suptitle("Image 3 after Intensity Slicing")
plt.imshow(afterCImage, cmap = 'gray', vmin=0, vmax=255)

# für den Grauwertbereich 0 bis 1
#plt.imshow(result, cmap='gray', vmin=0, vmax=1)
# oder für den Grauwertbereich 0 bis 255
#plt.imshow(result, cmap='gray', vmin=0, vmax=255)