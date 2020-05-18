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
import matplotlib.pyplot as plt
from scipy.stats import norm


img = np.empty((100,51), dtype=np.float)
#leeres Bild mit 100 Zeilen und 51 Spalten erzeugen mit Elementtyp float

xs = np.linspace(-5, 5, 51)
#51 Abtastpunkte erstellen als Array von -5 (inkl.) bis +5 (inkl.). 
#Die Schrittweite wird automatisch aus den Parametern so berechnet, dass sie
#zwischen allen Punkten gleich groß ist.

img[:,:] = norm.pdf(xs, 0, 1)
#norm.pdf implementiert die Gauß-Funktion vom Aufgabenblatt und durch die 
#Angabe von xs wird die Funktion zeitgleich auf alle x-Werte angewendet. Das
#Ergebnis ist eine Bildzeile, die so in alle Bildzeilen geschrieben wird.

img-=np.min(img)  #Abziehen des Minimums, um das Minimum auf 0 zu bringen
img*=1/np.max(img) 
#Skalierung der Werte mit dem Kehrwert des Maximums, damit das Maximum 1 wird.
img*=255  #Skalierung der Werte mit 255, damit das Maximum 255 wird.
img = np.round(img).astype(np.uint8)
#Rundung der Werte und Umwandlung des Elementtyps

plt.imshow(img, cmap='gray')

#mu ist der Mittelwert der Gaußfunktion und steuert so den höchsten (hellsten)
#Bereich auf der x-Achse, bewirkt als o eine Verschiebung nach links oder 
#rechts
#sigma ist die Standardabweichung und bestimmt die Stauchung der Gauß-Funktion,
#da im Bereich mu-sigma bis mu+sigma 66,8% aller Realisierungen liegen.
#Wird sigma größer, ist die Gaußfunktion somit "breiter" und umgekehrt.