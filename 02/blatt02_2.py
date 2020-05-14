# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 2 — Abtastung und Quantisierung

Erstellt ein Python-Skript, das ein Bild mit 100 identischen Bildzeilen 
erzeugt. Jede Bildzeile soll dabeidie identische Abtastung und Quantisierung 
der Gauß-Funktion enthalten..
"""

import numpy as np
import math as m
import scipy.stats as stats
import matplotlib.pyplot as plt



random_row = np.random.uniform(-5, 5, (51,))


def gaussian(x):
    return stats.norm.pdf(x, 0, 1)

random_gaussian = np.apply_along_axis(gaussian, 0, random_row)

random_gaussian = np.repeat(random_gaussian, 100, axis=0)
random_gaussian = random_gaussian.reshape(51, 100)
random_gaussian = random_gaussian.T
print(random_gaussian.shape)



'''
Skaliert alle Pixelwerte so, dass der höchste Wert des Bildes bei 255 und der
niedrigste Wert bei 0 liegt. Der Wertebereich ist also [0..255].
'''
g_m = random_gaussian - np.min(random_gaussian)
g_s = 255 * (g_m / np.max(g_m))

print(np.max(g_s), np.min(g_s))


plt.imshow(g_s, cmap='gray')

plt.show()

