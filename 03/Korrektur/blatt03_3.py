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

plt.close('all')


img1 = imread('./findetDieFehler/ohneFehler.png')
img2 = imread('./findetDieFehler/mitFehler.png')

"""
1. Ermittelt zunächst ein Bild, das die Veränderungen zwischen den beiden 
   Bildern zeigt als Verknüpfung der Bilder mit einem sinnvollen arithmetischen 
   Operator.
   
2. Wandelt das Ergebnis anschließend in ein Binärbild um, das veränderte Pixel 
   als Vordergrund und unveränderte Pixel als Hintergrund beinhaltet. 
   Wenn ihr euch das Bild nun anzeigen lasst, könnt ihr zwar die Positionen 
   der Veränderungen selbst ermitteln und die Anzahl zählen, aber das soll nun 
   ebenfalls der Computer machen.
"""
diff = 1-np.isclose(img1, img2, atol=0)
# np.isclose vergleicht elementweise, ob die Grauwerte nicht weiter als atol
# auseinander sind. D.h., es wird die absolute Differenz betrachtet. Am Ende
# muss das Ergebnis noch umgedreht werden, damit alle Pixel, bei denen diese
# Bedingung nicht zutrifft (Veränderung des Grauwerts) 1 werden und alle
# anderen 0.
#diff = np.abs(img1-img2)>0   # Alternativ
plt.imshow(diff, cmap='gray')


"""
3. Erweitert daher euer Skript, um die Funktionalität des Zählens der 
   Veränderungen. Dabei ist jeder zusammenhängende Bereich an Pixeln, der sich 
   verändert hat, als ein Bereich zu zählen.
   
a) Ermittelt dazu zunächst alle Koordinaten von Pixeln, die sich verändert 
   haben.
"""
xs, ys = np.nonzero(diff)
# An welchen Koordinaten ist diff != 0, sprich, es gibt eine Veränderung der 
# Grauwerte zwischen den beiden Bildern an diesen Koordinaten. xs und ys sind
# jeweils alle x- und y-Koordinaten.
coords = set(zip(xs, ys))
# Zusammenführen der Koordinaten zu Paaren (Tupeln) mit zip und erstellen einer
# Koordinatenmenge.

"""
b) Startet nun bei einem beliebigen Pixel und prüft ob dessen Nachbarn auch 
   verändert wurden. So könnt ihr euch durch die Menge der Vordergrund-
   koordinaten hangeln und iterativ die zusammenhängenden, veränderten Bereiche
   vollständig aufspüren.
"""
# Besserer Algorithmus: Raster Scan 
# Youtube: "Intro2Robotics: Connected Components in a Binary Image"

numComponent = 0
while len(coords) != 0:  # solange nach Koordinaten in der Menge sind
    numComponent +=1   # neue Veränderung gefunden
    neighbours = set([coords.pop()])
    # gib mir irgendeine Koordinate und setze sie in die Menge der Nachbarn
    while len(neighbours) != 0: # solange es noch Nachbarn gibt
        x, y = neighbours.pop() #gib mir einen Nachbarn als aktuelle Koordinate
        if (x+1, y) in coords:
        # ist der untere Nachbar auch in coords (wurde auch verändert und 
        # noch nicht betrachtet)
            coords.remove((x+1,y)) # lösche ihn aus coords
            neighbours.add((x+1,y)) # füge ihn in die Menge der Nachbarn ein
        if (x-1, y) in coords:  # oberer Nachbar
            coords.remove((x-1,y)) 
            neighbours.add((x-1,y)) 
        if (x, y+1) in coords:  # rechter Nachbar
            coords.remove((x,y+1)) 
            neighbours.add((x,y+1))
        if (x, y-1) in coords:  # linker Nachbar
            coords.remove((x,y-1)) 
            neighbours.add((x,y-1)) 


print(numComponent, 'Fehler im Bild gefunden')  # 8 Fehler im Bild gefunden

plt.show()