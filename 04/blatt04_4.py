# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 4 — Bildskalierung und Interpolation

Durch die geometrische Transformation von Bildern, bspw. die uniforme 
Skalierung um einen Faktor s, werden Pixelwerte an Koordinaten des Ursprungs-
bildes benötigt, die zwischen den eigentlichen Koordinaten liegen. So kann es 
etwa vorkommen, dass ein Wert an der Koordinate (0.2, 0.8) benötigt wird. 
Da es in Bildern aber nur ganzzahlige Koordinaten gibt, muss der Pixelwert an 
der Koordinate (0.2, 0.8) interpoliert werden. Dies soll in dieser Aufgabe mit 
der nearest neighbor Interpolation im Rahmen der Bildskalierung umgesetzt 
werden. Bei der nearest neighbor Interpolation wird, wie in Abbildung 3a 
dargestellt, der Pixelwert der Koordinate genommen, die der benötigten 
Koordinate (bspw. (0.2, 0.8)) am nächsten liegt. In diesem Beispiel wäre dies 
die Koordinate (0,1).
"""

import numpy as np
import matplotlib.pyplot as plt
import itertools as it
from skimage.io import imread


"""
1. Schreibt eine Python-Funktion, die ein Bild um einen gegebenen Faktor, der 
   nicht ganzzahlig sein muss, uniform skaliert. Nutzt dazu die nearest 
   neighbor Interpolation. 
   Hinweis 1: Rechnet die Koordinaten des Zielbildes in die Koordinaten des 
   Ausgangsbildes zurück und interpoliert dort.
   Hinweis 2: Die Funktion itertools.product() kann nützlich sein, um aus den 
   einzelnen x- bzw. y-Koordinaten alle Koordinaten des Bildes zu erzeugen.
"""


"""
2. Testet nun eure Skalierung am Bild tv.png aus dem Moodle.
"""
tv = imread('./tv.png')

