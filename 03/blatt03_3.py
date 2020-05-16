# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 3 — Findet die Fehler

Das Finden von Fehlern in der manipulierten Variante eines Originalbilds ist 
ein beliebtes Rätsel. Im Rahmen dieser Aufgabe soll dieses Problem nun 
strukturiert angegangen und mithilfe eines Python-Skripts gelöst werden. 
Dazu findet ihr im Moodle zwei Varianten eines Bilds, die eine ohne 
Veränderungen, die andere mit Veränderungen.
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread


ohneFehler = imread('./findetDieFehler/ohneFehler.png')
mitFehler = imread('./findetDieFehler/mitFehler.png')

plt.close('all')


"""
1. Ermittelt zunächst ein Bild, das die Veränderungen zwischen den beiden 
   Bildern zeigt als Verknüpfung der Bilder mit einem sinnvollen arithmetischen 
   Operator.
"""
unterschiede = mitFehler - ohneFehler


"""
2. Wandelt das Ergebnis anschließend in ein Binärbild um, das veränderte Pixel 
   als Vordergrund und unveränderte Pixel als Hintergrund beinhaltet. 
   Wenn ihr euch das Bild nun anzeigen lasst, könnt ihr zwar die Positionen 
   der Veränderungen selbst ermitteln und die Anzahl zählen, aber das soll nun 
   ebenfalls der Computer machen.
"""
maske = unterschiede > 0
plt.imshow(maske, cmap='gray')


"""
3. Erweitert daher euer Skript, um die Funktionalität des Zählens der 
   Veränderungen. Dabei ist jeder zusammenhängende Bereich an Pixeln, der sich 
   verändert hat, als ein Bereich zu zählen.
   
a) Ermittelt dazu zunächst alle Koordinaten von Pixeln, die sich verändert 
   haben.
"""
koordinaten = np.where(maske == 1)


"""
b) Startet nun bei einem beliebigen Pixel und prüft ob dessen Nachbarn auch 
   verändert wurden. So könnt ihr euch durch die Menge der Vordergrund-
   koordinaten hangeln und iterativ die zusammenhängenden, veränderten Bereiche
   vollständig aufspüren.
"""

 

plt.show()