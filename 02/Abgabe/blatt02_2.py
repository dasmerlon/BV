# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 2 — Abtastung und Quantisierung

Erstellt ein Python-Skript, das ein Bild mit 100 identischen Bildzeilen 
erzeugt. Jede Bildzeile soll dabei die identische Abtastung und Quantisierung 
der Gauß-Funktion enthalten.
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


"""
Erzeugt ein 1-D Array aus 51 zufälligen float-Werten, 
die zwischen -5 und 5 liegen.
"""
random_row = np.random.uniform(-5, 5, (51,))


"""
Die Funktion gaussian() berechnet die Gaußfunktion für einen Wert x mit 
mu = 0 und sigma = 1.
"""
def gaussian(x, mu=0, sigma=1):
    return stats.norm.pdf(x, mu, sigma)


"""
Tastet die Bildzeile von random_row mit der Gaußfunktion ab.
"""
random_gaussian = np.apply_along_axis(gaussian, 0, random_row)


"""
Wiederholt die Bildzeile 100 mal.
"""
random_gaussian = np.repeat(random_gaussian, 100, axis=0)


"""
Erzeugt aus dem 1-D Array ein Array der Form (51, 100).
"""
random_gaussian = random_gaussian.reshape(51, 100)


"""
Transponiert das Array, sodass es nun die Form (100, 51) hat, wobei die 100
Zeilen alle gleich sind.
"""
random_gaussian = random_gaussian.T


"""
Skaliert alle Pixelwerte so, dass der höchste Wert des Bildes bei 255 und der
niedrigste Wert bei 0 liegt. Der Wertebereich ist also [0..255].
"""
random_gaussian_m = random_gaussian - np.min(random_gaussian)
random_gaussian_s = 255 * (random_gaussian_m / np.max(random_gaussian_m))


"""
Rundet die Werte des Arrays kaufmännisch.
"""
random_gaussian_s = np.rint(random_gaussian_s)


"""
Ändert den Datentyp des Arrays auf np.uint8
"""
random_gaussian_s = random_gaussian_s.astype(np.uint8)


"""
Zeigt das Bild an.
"""
plt.close('all')
plt.imshow(random_gaussian_s, cmap='gray')
plt.show()

