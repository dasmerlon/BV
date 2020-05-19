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


without_mistakes = imread('./findetDieFehler/ohneFehler.png')
with_mistakes = imread('./findetDieFehler/mitFehler.png')

plt.close('all')


"""
1. Ermittelt zunächst ein Bild, das die Veränderungen zwischen den beiden 
   Bildern zeigt als Verknüpfung der Bilder mit einem sinnvollen arithmetischen 
   Operator.
"""
differences = with_mistakes - without_mistakes


"""
2. Wandelt das Ergebnis anschließend in ein Binärbild um, das veränderte Pixel 
   als Vordergrund und unveränderte Pixel als Hintergrund beinhaltet. 
   Wenn ihr euch das Bild nun anzeigen lasst, könnt ihr zwar die Positionen 
   der Veränderungen selbst ermitteln und die Anzahl zählen, aber das soll nun 
   ebenfalls der Computer machen.
"""
mask = differences > 0
plt.imshow(mask, cmap='gray')


"""
3. Erweitert daher euer Skript, um die Funktionalität des Zählens der 
   Veränderungen. Dabei ist jeder zusammenhängende Bereich an Pixeln, der sich 
   verändert hat, als ein Bereich zu zählen.
   
a) Ermittelt dazu zunächst alle Koordinaten von Pixeln, die sich verändert 
   haben.
"""
coordinates = set(zip(*np.where(mask == 1)))


"""
b) Startet nun bei einem beliebigen Pixel und prüft ob dessen Nachbarn auch 
   verändert wurden. So könnt ihr euch durch die Menge der Vordergrund-
   koordinaten hangeln und iterativ die zusammenhängenden, veränderten Bereiche
   vollständig aufspüren.
"""
clusters = []

def find_all_neighbors(coordinate, cluster_id, checked):
    # This only happens in the very first time this recursion is called
    # Get the next cluster id (next slot in the clusters list) and
    # initialize the cluster
    if cluster_id is None:
        cluster_id = len(clusters)
        clusters.append([])
     
    (x, y) = coordinate
    # Get all neighborings coordinates
    neighbors = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
    # Iterate over everything and check if the neighbor is in the 
    # list of changed coordinates
    for neighbor in neighbors:
        if neighbor in coordinates:
            # Ignore this node, in case we already checked it
            if neighbor in checked:
                continue

            # Push the neighbor coordinate to the current cluster
            clusters[cluster_id].append(neighbor)
            # Remember that we already checked this node
            checked.add(neighbor)
            # We have to check the neighbor's neighbors as well :PP
            find_all_neighbors(neighbor, cluster_id, checked)

# Iterate through all coordinates until
checked = set()
for coordinate in coordinates:
    # We already checked this coordinate somewhere in the recursive lookup
    if coordinate in checked:
        continue
    
    find_all_neighbors(coordinate, None, checked)


print('Anzahl der Fehler:', len(clusters))

plt.show()