# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
         
         
Aufgabe 4 — Fortgeschrittene Bearbeitung von Bildern 

In dieser Aufgabe sollen weitere Manipulationen an einem Beispielbild erprobt 
werden. Schreibt dazu wieder ein Python-Skript, das alle Schritte eurer 
Manipulationen beinhaltet. Im Rahmen dieser Aufgabe ist nur die Nutzung von 
NumPy, Matplotlib sowie skimage.io.imread zum Laden eines Bildes erlaubt.
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread


"""
1. Erstellt ein neues Bild basierend auf drei Variationen des Bildes 
   mandrill.png aus dem Moodle sowie dem Originalbild.
   
a) Ladet dazu zunächst erneut das Bildmandrill.pngaus dem Moodle in Python.
"""
mandrill = imread('./mandrill.png')


"""
b) Spiegelt das Bild an der vertikalen Achse (linke und rechte Seite tasuchen) 
   und speichert das Ergebnis in eine neue Variable als erste Variation.
"""
#top_right = mandrill[:,::,-1]
top_right = np.fliplr(mandrill)


"""
c) Spiegelt das Originalbild (mandrill.png) nun an der horizontalen Achse und 
   speichert das Ergebnis erneut in einer neuen Variable. Dies ist die ist die 
   zweite Variation.
"""
bottom_left = np.flipud(mandrill)


"""
d) Führt jetzt beide Spiegelungen nacheinander auf dem Originalbild aus,
   speichert das Ergebniswiederum in einem neuen Bild als dritte Variation.
"""
bottom_right = np.flipud(top_right)   # top_right beinhaltet die 1. Spiegelung
#bottom_right = np.flipud(np.fliplr(mandrill))  # Alternative


"""
e) Erzeugt nun ein neues Bild, das doppelt so hoch und breit ist wie das 
   Bild mandrill.png. Setzt in jeden Quadranten des neuen Bildes eine der vier
   Versionen des Bildes ein. Oben links soll das Origianlbild zu sehen sein, 
   rechts daneben das an der vertikalen Achse gespiegelte Bild, links unten 
   das an der horizontalen Achse gespiegelte Bild und rechts unten das 
   an beiden Achsen gespiegelte Bild. Das Ergebnis sollte etwa wie in 
   Abbildung 1b aussehen.Tipp: Zum Erzeugen von Arrays bzw. Bildern gibt es 
   in NumPy mehrere Funktionen neben np.array.
"""
mandrill_big = np.block([[mandrill, top_right], 
                         [bottom_left, bottom_right]])
# Alternative:
#mandrill_big = np.zeros((mandrill.shape[0]*2, mandrill.shape[1]*2))
#mandrill_big[:512, :512] = mandrill
#mandrill_big[:512, 512:] = top_right
#mandrill_big[512:, :512] = bottom_left
#mandrill_big[512:, 512:] = bottom_right
plt.close('all')
plt.imshow(mandrill_big, cmap = 'gray')


"""
2. Erzeugt nun ein Negativ des Originalbilds (mandrill.png). In einem Negativ
   sind alle Helligkeitswerte umgedreht. D.h. schwarz wird zu weiß, weiß wird 
   zu schwarz und alle Werte dazwischenwerden ebenso gedreht. Lasst euch das 
   Bild zur Kontrolle anzeigen.
"""
mandrill_inverted = np.invert(mandrill)  # funktioniert weil Wertebereich passt
#mandrill_inverted = ~mandrill       # Alternative
#mandrill_inverted = 255 - mandrill  # Alternative
plt.figure(2)
plt.imshow(mandrill_inverted, cmap = 'gray')


"""
3. Schneidet erneut die Nasenspitze des Mandrills wie in Abbildung 1a 
   dargestellt als neues Bild aus. Ändert nun in dem neu erzeugten Ausschnitt
   ein Pixel und findet heraus, ob diese Änderung auch im Originalbild 
   durchgeführt wird.
"""
mandrill_nose = mandrill[340:450, 150:340]
mandrill_nose[60,90] = 0       # Färbt den Pixel an (60,90) schwarz
#plt.imshow(mandrill_nose, cmap = 'gray')    # Der Pixel ist zu sehen
#plt.imshow(mandrill, cmap = 'gray')     # Im Originalbild ebenfalls (zoomen)

#Alternative:
#nase = mandrill[340:450, 150:340]
#print('vorher', nase[0,0]==mandrill[340,150], nase[0,0], mandrill[340,150])
#nase[0,0] += 1
#print('nachher', nase[0,0]==mandrill[340,150], nase[0,0], mandrill[340,150])


"""
4. Erstellt euch nun eine Maske für den Bereich der Nasenspitze des Mandrills.

a) Erzeugt dazu zunächst ein neues Bild, das nur aus Nullen besteht, und die 
   gleiche Größe wie das Originalbild hat. Dieses Bild wird eure Maske.
"""
mask = np.zeros_like(mandrill)  # erzeugt ein schwarzes Bild 


"""
b) Setzt nun in der Maske alle Pixel, die in dem Bereich liegen, der die 
   Nasenspitze beinhaltet, auf 1.
"""
mask[340:450, 150:340] = 1


"""
c) Verrechnet anschließend Maske und Originalbild, sodass der Bereich 
   außerhalb der Nasenspitze schwarz ist und nur im Bereich der Nasenspitze 
   das eigentliche Bild zu sehen ist. Das Ergebnis sollte etwa wie in 
   Abbildung 1c aussehen.
"""
mandrill_mask = mask * mandrill  
# Der schwarze Bereich bleibt schwarz, denn 0 * x = 0
# und der weiße Bereich wird zum Bild, denn 1 * x = x
plt.figure(3)
plt.imshow(mandrill_mask, cmap = 'gray')


plt.show()