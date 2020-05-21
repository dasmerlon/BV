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


without_mistakes = imread('./findetDieFehler/ohneFehler.png')
with_mistakes = imread('./findetDieFehler/mitFehler.png')

"""
1. Ermittelt zunächst ein Bild, das die Veränderungen zwischen den beiden 
   Bildern zeigt als Verknüpfung der Bilder mit einem sinnvollen arithmetischen 
   Operator.
"""
# Hintergrundsubtraktion zeigt Unterschiede (Pixelwert=0 -> keine Veränderung)
differences = with_mistakes - without_mistakes

"""
2. Wandelt das Ergebnis anschließend in ein Binärbild um, das veränderte Pixel 
   als Vordergrund und unveränderte Pixel als Hintergrund beinhaltet. 
   Wenn ihr euch das Bild nun anzeigen lasst, könnt ihr zwar die Positionen 
   der Veränderungen selbst ermitteln und die Anzahl zählen, aber das soll nun 
   ebenfalls der Computer machen.
"""
mask = differences > 0  # Einfügen des Schwellenwerts 0: Werte > 0 werden zu 1
plt.imshow(mask, cmap='gray')


"""
3. Erweitert daher euer Skript, um die Funktionalität des Zählens der 
   Veränderungen. Dabei ist jeder zusammenhängende Bereich an Pixeln, der sich 
   verändert hat, als ein Bereich zu zählen.
   
a) Ermittelt dazu zunächst alle Koordinaten von Pixeln, die sich verändert 
   haben.
"""
# Vordergrundkoordinaten als Menge in der Form {(x1,y1), (x2,y2), ...}
coordinates = set(zip(*np.where(mask == 1)))


"""
b) Startet nun bei einem beliebigen Pixel und prüft ob dessen Nachbarn auch 
   verändert wurden. So könnt ihr euch durch die Menge der Vordergrund-
   koordinaten hangeln und iterativ die zusammenhängenden, veränderten Bereiche
   vollständig aufspüren.
"""
clusters = []  # erzeugt eine leere Liste

# Die Funktion erhält eine Vordergrundkoordinate, die aktuelle 
# Gruppen-ID und eine Menge der bereits überprüften Koordinaten.
def find_all_neighbors(coordinate, cluster_id, checked):
    if cluster_id is None:  # passiert nur beim ersten Aufruf der Rekursion
        cluster_id = len(clusters)  # erhält die nächste Gruppen-ID
        clusters.append([])  #fügt eine leere Liste (die neue Gruppe) hinzu
     
    (x, y) = coordinate  # trennt die Koordinaten in x und y 
    # neighbors erhält alle möglichen Nachbarkoordinaten
    neighbors = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
    
    # iteriert über alle Nachbarn der Vordergrundkoordinaten
    for neighbor in neighbors:  
        # überprüft ob Nachbar in den Vordergrundkoordinaten enthalten ist
        if neighbor in coordinates:  
            # ignoriert den Nachbar, wenn er schon überprüft wurde
            if neighbor in checked:
                continue

            # fügt die Nachbarkoordinate zur aktuellen Gruppe
            clusters[cluster_id].append(neighbor)
            # fügt den Nachbarn zur checked-Menge, um sich zu merken,
            # dass Nachbar bereits überprüft wurde
            checked.add(neighbor)
            # überprüfen des Nachbars Nachbarn (Rekursionsaufruf)
            find_all_neighbors(neighbor, cluster_id, checked)  

checked = set()  # erzeugt eine leere Menge
for coordinate in coordinates:  # iteriert über alle Vordergrundkoordinaten
    # ignoriert Koordinate, wenn sie bereits in der Rekursion überprüft wurde
    if coordinate in checked:  
        continue
    # ruft die Funktion an der aktuellen Koordinate auf
    find_all_neighbors(coordinate, None, checked)

# Die Länge der Gruppenliste ist die Anzahl der Gruppen
print('Anzahl der Fehler:', len(clusters))  

plt.show()