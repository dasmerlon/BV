# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 1 — Anwendung Fernerkundung


Band No.        Name                    wavelength
1               visible blue            0.45-0.52
2               visible green           0.53-0.61
3               visible red             0.63-0.69
4               near infrared           0.78-0.90
5               middle infrared         1.55-1.75
6               thermal infrared        10.4-12.5
7               shortwave infrared      2.09-2.35
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow


'''
Ladet die Bänder 3 und 4 mithilfe der Funktion skimage.io.imread in Python.
Band3 ist die Aufnahme des roten Lichts und 
Band4 ist die Aufnmahme des nahen Infrarot
'''
band3 = imread('./landsatBild/band1.png')
band4 = imread('./landsatBild/band1.png')


'''
Ändert den Datentyp der NumpyArrays auf np.float 
'''
red = band3.astype(np.float)
nir = band4.astype(np.float)


'''
Skaliert die Werte von dem Bild red auf den zulässigen Bereich
um Overflow zu verhindern
'''
red_m = red - np.min(red)
red_s = 255 * (red_m / np.max(red_m))


'''
Berechnet den Indikator für lebende, grüne Vegetation NDVI
'''
ndvi = (nir - red_s) / (nir + red_s)


'''
Zeigt das Ergebnis als Graustufenbild an
'''
plt.close('all')
imshow(ndvi, cmap='gray')
plt.show()


'''
Berechnungen des NDVI's resultieren immer in Pixeln, die in dem Bereich 
-1 bis 1 liegen. Werte nahe 0 bedeuten, dass keine Vegetation vorhanden ist, 
Werte nahe 1 zeigen wiederrum Vegetation an.
Da die Kreise sehr hell bis weiß angezeigt werden, kann man davon ausgehen,
dass es sich hierbei um Pflanzen handelt. Alles außerhalb der Kreise ist grau,
also nahe 0, was bedeutet, dass dort keine Pflanzen sind.
'''


