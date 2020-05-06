# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 3 — Basisoperationen mit Bildern

Diese Aufgabe dient dem ersten Kontakt mit Bildern in Python. Dazu sollt ihr 
gegebene Bilder manipulieren und alle Schritte erneut in einem Python-Skript 
festhalten. Im Rahmen dieser Aufgabe ist nur die Nutzung von NumPy, Matplotlib
sowie skimage.io.imread und skimage.io.imsave zum Laden bzw. Speichern eines 
Bildes erlaubt.    
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave


"""
1. Speichert euch das Bild mandrill.png aus dem Moodle ab und ladet es in 
   Python mithilfe der Funktion skimage.io.imread.
"""
mandrill = imread('./mandrill.png')


"""
2. Zeigt das Bild mithilfe von Matplotlib an.
"""
plt.close('all')    # schließt automatisch das Fenster bei erneutem Start
plt.imshow(mandrill, cmap = 'gray')


"""
3. Erstellt ein neues Array als Bildausschnitt, das, wie in Abbildung 1a 
   visualisiert, etwa die Nasenspitze des Mandrill beinhaltet.
"""
mandrill_nose = np.array(mandrill[325:450, 150:340])
#plt.imshow(mandrill_nose, cmap = 'gray')


"""
4. Speichert den Bildausschnitt mit der Funktion skimage.io.imsave ab.
"""
imsave('./mandrill_nose.png', mandrill_nose)


"""
5. Erstellt eine Kopie des Bildes und setzt ein einziges Pixel (Arrayelement 
   bzw. Bildelement) auf schwarz. Lasst euch das manipulierte Bild anzeigen. 
   Erkennt man den Unterschied? (kein Antworttext nötig)
"""
mandrill_black_pixel = np.copy(mandrill)
mandrill_black_pixel[200,200] = 0     # Färbt den Pixel an (200,200) schwarz
#plt.imshow(mandrill_black_pixel, cmap = 'gray') # Man sieht den Pixel (zoomen)


"""
6. Erstellt eine weitere Kopie des Bildes und setzt den gesamten Bereich der 
   Augen des Mandrills auf schwarz. Lasst euch das manipulierte Bild erneut 
   anzeigen. Erkennt man nun den Unterschied? (kein Antworttext nötig)
"""
mandrill_black_eyes = np.copy(mandrill)
mandrill_black_eyes[25:100, 100:400] = 0  # Färbt den Bereich der Augen schwarz
#plt.imshow(mandrill_black_eyes, cmap = 'gray')

