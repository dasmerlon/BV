# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 3 — Serienbild

In der Vorlesung wurde das Mitteln über mehrere zeitlich versetzt aufgenommene 
Bilder einer identischen Szene als Möglichkeit zur Unterdrückung des Rauschens 
präsentiert. Diese Idee soll in dieser Aufgabe genutzt werden, um die 
Einzelbilder eines Serienfotos zu einem Bild zusammenzusetzen. Dabei zeigt das 
Serienfoto die Bewegung eines Balls über eine Tischplatte. Das Endergebnis soll 
alle fünf Stadien der Bewegung aus den Einzelbildern auf einem Bild vereinen.
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread


"""
1. Ladet die fünf Einzelbilder des serienbild.zip aus dem Moodle in Python. 
   Zunächst muss aus den fünf Einzelbildern ein möglichst perfektes 
   Hintergrundbild ohne Ball erzeugt werden, ähnlich dem in Abbildung 1b. 
   Wenn man den Ball als Rauschen annimmt, kann man nach dem Gesetz der großen 
   Zahlen durch Mittelung über die Bilder das Rauschen, bzw. hier den Ball, 
   zumindest recht gut entfernen. 
   Reichen fünf Bilder dafür aus? Probiert es aus!
"""
bild1 = imread('./serienbild/bild1.png')
bild2 = imread('./serienbild/bild2.png')
bild3 = imread('./serienbild/bild3.png')
bild4 = imread('./serienbild/bild4.png')
bild5 = imread('./serienbild/bild5.png')


def scaling(g):
    g_m = g - np.min(g)
    g_s = 255 * (g_m / np.max(g_m))
    return g_s


test = 1/5 * bild1 + 1/5 * bild2 + 1/5 * bild3 + 1/5 * bild4 + 1/5 * bild5
plt.imshow(scaling(test), cmap='gray')  # 5 Bilder reichen nicht


"""
2. Überprüft das Ergebnis visuell und überlegt euch eine bessere aber sehr 
   ähnliche Möglichkeit für das Verknüpfen der fünf Pixel an jeweils einer 
   Koordinate. Betrachtet dabei keine anderen Koordinaten wie etwa die der 
   Nachbarn! Das Ergebnis soll dabei dem in Abbildung 1b so nahe wie möglich 
   kommen.
"""
