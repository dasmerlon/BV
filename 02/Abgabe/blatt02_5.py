# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 5 — Rauschen

Erstellt ein Python-Skript mit zwei Funktionen, die jeweils das Gaußsche 
Rauschen bzw. das salt-and-pepper noise auf ein Bild applizieren. Bei der 
Funktion zum Gaußschen Rauschen soll die Standardabweichung übergeben werden 
können und bei der Funktion zum salt-and-pepper noise die Wahrscheinlichkeit 
für eine Veränderung (salt und pepper sind dann gleich wahrscheinlich).
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread


"""
Ladet das Bild mithilfe der Funktion skimage.io.imread in Python.
"""
plt.close('all')
mandrill = imread('./mandrill.png')


"""
Zeigt das unveränderte Bild mit dem Titel "image without noise" als 
Graustufenbild an.
"""
fig1 = plt.figure(1)
fig1.suptitle('image without noise')
plt.imshow(mandrill, cmap = 'gray')


"""
Die Funktion scaling_image() skaliert ein übergebenes Bildes auf den 
Wertebereich [0...255]. Der höchste Wert des Bildes wird dadurch zu 255 und 
der kleinste zu 0. Alle Werte dazwischen werden dementsprechend eingeordnet.
"""
def scaling_image(img):
    img_m = img - np.min(img)
    img_s = 255 * (img_m / np.max(img_m))
    return img_s

'''
Die Funktion gaussian_noise appliziert auf ein übergebenes Bild das Gaußsche
Rauschen mit der übergebenen Standardabweichung sigma.
Je kleiner der Wert von sigma, desto weniger und je größer der Wert, desto 
mehr Rauschen wird auf das Bild appliziert. 
'''
def gaussian_noise(img, sigma):
    noise = np.random.normal(0, sigma, img.shape)  # erzeugt Gaußsches Rauschen
    img_n = img + noise  # appliziert das Rauschen auf das Bild
    img_s = scaling_image(img_n)  # skaliert das Bild auf den Bereich [0..255]
    plt.imshow(img_s, cmap = 'gray')  # zeigt das Ergebnis an


"""
Die Funktion salt_and_pepper_noise appliziert auf ein übergebenes Bild das 
salt-and-pepper noise mit der übergebenen Wahrscheinlichkeit für Veränderung p.
Der Wert von p kann zwischen 0 und 1 liegen. Je kleiner der Wert von p, desto 
weniger und je größer der Wert, desto mehr Rauschen wird auf das Bild 
appliziert. 
"""
def salt_and_pepper_noise(img, p):
    img_n = np.empty(img.shape, np.uint8)  # erzeugt ein leeres Array
    for i in range(img.shape[0]):  # Schleife über die Zeilen
        for j in range(img.shape[1]):  # Schleife über die Spalten
            r = np.random.random_sample()  # erzeugt eine zufällige float-Zahl 
                                    # zwischen 0 (inklusive) und 1 (exklusive)
            if r < (p/2):           
                img_n[i][j] = 0     # pepper noise auf den Pixel
            elif r > (1 - p/2):
                img_n[i][j] = 255   # salt noise auf den Pixel
            else:
                img_n[i][j] = img[i][j]  # Originalbild auf den Pixel
    plt.imshow(img_n, cmap = 'gray')  # zeigt das Ergebnis an


"""
Testet die Funktionen gaussian_noise an dem Bild mandrill.png und mit
einer Standardabweichung von 30.
"""
fig2 = plt.figure(2)
fig2.suptitle('image with gaussian noise')
gaussian_noise(mandrill, 30)


"""
Testet die Funktionen salt_and_pepper_noise an dem Bild mandrill.png und mit
einer Wahrscheinlichkeit von 0.2, dass das Rauschen auftritt.
"""
fig3 = plt.figure(3)
fig3.suptitle('image with salt-and-pepper noise')
salt_and_pepper_noise(mandrill, 0.2)

plt.show()

