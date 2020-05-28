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
# Gelöst mit einer Power Law Transformation. Es gibt 8 Poller.
beforeAImage = img1
afterAImage = img1 ** 1.55 
# Um den Kontrast von dem dunklem Bereich zu erhöhen, benutzten wir eine 
# Exponentialfunktion und rechnen jeden Pixel hoch einen Wert größer als 1.

f, f1 = plt.subplots(1,2) 
f.suptitle('Image 1 before and after gamma correction')
f1[0].imshow(beforeAImage, cmap = 'gray', vmin=0, vmax=255)
f1[1].imshow(afterAImage, cmap = 'gray', vmin=0, vmax=255)


"""
2. Sorgt dafür, dass sich die Skyline in Bild 2 besser vom Himmel abhebt.
"""
# Contrast Stretching
def ContrastStretching(image): 
    # Eine Funktion, die auf einer Pixel-per-Pixel-Basis jeden Wert auf seinen 
    # Grauwert untersucht und dann entsprechend, den Kontrast erhöht oder
    # verringert.
    result = np.copy(image)
    for x in range(result.shape[0]):
        for y in range(result.shape[1]):
            if(result[x,y] < 145): # Die Skyline liegt ca. zwischen 145 und 150
                result[x,y] = result[x,y] ** 0.8 #hellere Eerte --> heller
            elif(result[x,y] > 150):
                result[x,y] = result[x,y] ** 1.05 #dunklere werte --> dunkler
    return result

beforeBImage = img2
afterBImageContrastStretching = ContrastStretching(img2)
# Hier einmal noch ein Versuch mit Intensity Level Slicing.
schwellWert = (beforeBImage > 147) * 255 
afterBImage = beforeBImage + schwellWert

#beforeB = plt.figure(2)
#beforeB.suptitle('Image 2 Before')
#plt.imshow(beforeBImage, cmap = 'gray', vmin=0, vmax=255)
f, f2 = plt.subplots(1,2) 
f.suptitle('Image 2 with Intensity Level Slicing and Contrast Stretching')
f2[0].imshow(afterBImage, cmap = 'gray', vmin=0, vmax=255)
f2[1].imshow(afterBImageContrastStretching, cmap = 'gray', vmin=0, vmax=255)


"""
3. Verändert das Bild 3 so, dass in etwa der Bereich der Autobahn in der 
   Bildmitte weiß ist und der Rest des Bildes seine Graufärbung behält.
   Hinweis: Das Ergebnis wird nicht perfekt werden!
"""
# Gelöst mit Intensity Level Slicing.
beforeCImage = img3

schwellWert = (beforeCImage > 104) * 255 
# Wir erzeugen eine Maske und färben alle Pixel über dem Grauwert 104 weiß.
afterCImage = beforeCImage + schwellWert 
# Indem wir die Maske mit dem Bild addieren sorgen wir dafür das alle richtigen 
# Pixel automatisch den wert 255 im fertigen Bild haben.

f, f3 = plt.subplots(1,2) 
f.suptitle('Image 3 before and after Intensity Slicing')
f3[0].imshow(beforeCImage, cmap = 'gray', vmin=0, vmax=255)
f3[1].imshow(afterCImage, cmap = 'gray', vmin=0, vmax=255)

plt.show()