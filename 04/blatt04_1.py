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

"""
1. Verbessert die Sichtbarkeit des linken unteren Bildbereichs in Bild 1 
   und ermittelt, wie viele Poller es am Rande einer kleinen Grüninsel in der 
   unteren linken Bildecke gibt?
"""

"""
2. Sorgt dafür, dass sich die Skyline in Bild 2 besser vom Himmel abhebt.
"""

"""
3. Verändert das Bild 3 so, dass in etwa der Bereich der Autobahn in der 
   Bildmitte weiß ist und der Rest des Bildes seine Graufärbung behält.
   Hinweis: Das Ergebnis wird nicht perfekt werden!
"""


# für den Grauwertbereich 0 bis 1
#plt.imshow(result, cmap='gray', vmin=0, vmax=1)
# oder für den Grauwertbereich 0 bis 255
#plt.imshow(result, cmap='gray', vmin=0, vmax=255)