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

plt.close('all')

"""
1. Verbessert die Sichtbarkeit des linken unteren Bildbereichs in Bild 1 
   und ermittelt, wie viele Poller es am Rande einer kleinen Grüninsel in der 
   unteren linken Bildecke gibt?
"""
img1 = imread('./bildverbesserung/bild1.png').astype(np.float)

# Power-law transformation mit c = 1 und gamma = 0.2. Es gibt 8 Poller.
c = 1
gamma = 0.2
result1 = c*img1**gamma

# Skalierung des Ergebnis auf den Bereich 0...1
result1-=np.min(result1)
result1*=(np.max(result1)**-1)

f, f1 = plt.subplots(1,2) 
f.suptitle('Image 1 before and after gamma correction')
f1[0].imshow(img1, cmap = 'gray', vmin=0, vmax=255)
f1[1].imshow(result1, cmap = 'gray', vmin=0, vmax=1)
# vmin und vmax verhindern die Skalierung der Grauwerte auf den Bereich 0 bis 1
# Dabei würde, sofern es keinen Grauwert 0 bzw. 255 gibt im Bild, der Kontrast
# beim Anzeigen erhöht werden, da das Minimum auf 0 und das Maximum auf 255 
# abgebildet werden.


"""
2. Sorgt dafür, dass sich die Skyline in Bild 2 besser vom Himmel abhebt.
"""
img2 = imread('./bildverbesserung/bild2.png').astype(np.float)/255

# Contrast Stretching mit der Sigmoidfunktion von VL 4, Teil 1, Folie 7
# oder piecewise linear transformation functions von VL 4, Teil 2, Folie 10
result2 = np.e**(img2*16-10)/(1+np.e**(img2*16-10))
# Sigmoidfunktion e^t/(1+e^t)

# Alternativ: Skalierung (nicht optimal)
#result2 = img2-np.min(img2)
#result2 = result2/np.max(img2)

f, f2 = plt.subplots(1,2) 
f.suptitle('Image 2 with Intensity Level Slicing and Contrast Stretching')
f2[0].imshow(img2, cmap = 'gray', vmin=0, vmax=1)
f2[1].imshow(result2, cmap = 'gray', vmin=0, vmax=1)


"""
3. Verändert das Bild 3 so, dass in etwa der Bereich der Autobahn in der 
   Bildmitte weiß ist und der Rest des Bildes seine Graufärbung behält.
   Hinweis: Das Ergebnis wird nicht perfekt werden!
"""
img3 = imread('./bildverbesserung/bild3.png')

# Intensity-level slicing, VL 4, Teil 2, Folie 11
result3 = np.copy(img3)
result3[np.logical_and(img3 > 100, img3 < 150)] = 255
# np.logical_and(img3 > 100, img3 < 150) bedeutet, dass Pixel, die > 100 und 
# < 150 sind, den Wahrheitswert True bekommen und nachfolgend verändert werden
# result3[np.logical_and(img3 > 100, img3 < 150)] = 255 bedeutet, dass alle 
# Pixel, für die der innere Ausdruck zu True evaluiert, verändert werden zu 255

f, f3 = plt.subplots(1,2) 
f.suptitle('Image 3 before and after Intensity Slicing')
f3[0].imshow(img3, cmap = 'gray', vmin=0, vmax=255)
f3[1].imshow(result3, cmap = 'gray', vmin=0, vmax=1)

plt.show()