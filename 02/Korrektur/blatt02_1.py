# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 1 — Anwendung Fernerkundung

Das Satellitenbild scheint einige grüne Punkte in der Wüste zu zeigen. 
Sind dies Pflanzen? Findet es heraus, indem ihr den Vegetationsindex NDVI 
(normalized difference vegetation index) für jedes Pixel im Bild berechnet.

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
from skimage.io import imread


"""
Ladet die Bänder 3 und 4 mithilfe der Funktion skimage.io.imread in Python.
Band3 ist die Aufnahme des roten Lichts und 
Band4 ist die Aufnmahme des nahen Infrarot.
"""
band3 = imread('./landsatBild/band3.png')
band4 = imread('./landsatBild/band4.png')


"""
Ändert den Datentyp der NumpyArrays auf np.float.
"""
red = band3.astype(np.float)
nir = band4.astype(np.float)


"""
Berechnet den Indikator für lebende, grüne Vegetation NDVI.
Berechnungen des NDVI's resultieren immer in Pixeln, die in dem Bereich 
-1 bis 1 liegen. Werte nahe 0 bedeuten, dass keine Vegetation vorhanden ist, 
Werte nahe 1 zeigen wiederrum Vegetation an.
"""
ndvi = (nir - red) / (nir + red)


"""
Zeigt das Ergebnis als Graustufenbild an.
"""
plt.close('all')
plt.imshow(ndvi, cmap='gray')
plt.show()


"""
Bei den grünen Punkten handelt es sich um künstlich bewässerte, 
landwirtschaftlich genutzte Flächen in der Wüste. Dies ist leicht am hohen 
NDVI im Bereich der grünen Punkte zu erkennen, da das Chlorophyll in den 
Pflanzen rotes Licht absorbiert und die Pflanzenzellen aber nahes Infrarot 
reflektieren (geringe Reflekionen im Rot-Bereich). Die Umgebung ist hingegen 
nahezu vollständig unbewachsen. Die Abstufungen in den Grautönen zeigen die 
Stärke des NDVI an und lassen somit Rückschlüsse auf die Dichte oder die 
Gesundheit der Pflanzen zu.
"""
