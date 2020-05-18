# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
         

Aufgabe 6 — Bildstatistiken in NumPy

In dieser Aufgabe geht es um das Finden, Kombinieren und effiziente Benutzung
von NumPy-Funktionen auf Bildern. D.h. im Rahmen dieser Aufgabe ist nur die 
Verwendung von NumPy-Funktionen und skimage.io.imread zum Laden eines Bildes
erlaubt. Explizit nicht erlaubt ist die Verwendung von Schleifen zum Iterieren
über Bilder.
"""

import numpy as np
from skimage.io import imread


"""
1. Ladet erneut das Bild mandrill.png in Python.
"""
mandrill = imread('./mandrill.png')


"""
2. Ermittelt Minimum, Maximum, Durchschnitt und die Standardabweichung des 
   Bildes mithilfe der entsprechenden NumPy-Funktionen.
"""
mandrill_min = np.min(mandrill)      # Minimum: 0
mandrill_max = np.max(mandrill)      # Maximum: 232
mandrill_av  = np.average(mandrill)  # Durchschnitt: 129.53657913208008
#print('Mittelwert:', np.mean(mandrill))       # Alternative zu np.average
mandrill_std = np.std(mandrill)      # Standardabweichung: 43.27355497483949
#print(mandrill_min, mandrill_max, mandrill_av, mandrill_std)


# Alternative:
#print('Minimum:', np.min(mandrill))            # 0
#print('Maximum:', np.max(mandrill))            # 232
#print('Durchschnitt:', np.average(mandrill))   # 129.53657913208008
#print('Standardabweichung:', np.std(mandrill)  # 43.27355497483949


"""
3. Lokalisiert das Minimum und das Maximum im Bild. Gebt dazu die x- und 
   y-Koordinate eines Minimums und Maximums auf der Konsole aus. Tipp: 
   Schaut in die Dokumentation der entsprechenden Funktionen, um zu erfahren,
   wie ihr aus dem einen Ergebnisindex zwei Koordinaten generiert.
"""
print(np.unravel_index(np.argmin(mandrill), mandrill.shape)) #Minimum(511, 177)
print(np.unravel_index(np.argmax(mandrill), mandrill.shape)) #Maximum(74, 295)


"""
4. Zählt wie viele Pixel es mit einem geraden bzw. einem ungeraden Wert im 
   Bild gibt. Nutzt auch hierfür wiederum keine Schleifen!
"""
mandrill_even = mandrill % 2 == 0  # erzeugt ein Array, welches an den Stellen
# True ist, an denen sich die Zahl ohne Rest durch 2 teilen lässt.
amount_even = np.count_nonzero(mandrill_even)  # 0 == False
amount_all = mandrill.shape[0] * mandrill.shape[1]
amount_odd = amount_all - amount_even
#print(f'gerade: {amount_even}, ungerade: {amount_odd}')


# Alternative:
#print('Anzahl gerade Werte:', np.sum(mandrill % 2 == 0))
#print('Anzahl ungerade Werte:', np.sum(mandrill % 2 == 1))

"""
5. Ermittelt außerdem alle Koordinaten an denen Pixel mit geradem Wert 
   lokalisiert sind. Die Form der Koordinaten bspw. ((x1, y1),(x2, y2),
   (x3, y3), . . .) oder ((x1, x2, x3, . . .),(y1, y2, y3, . . .)) ist 
   unerheblich.
"""
indices_even = np.where(mandrill_even == 1)  # erzeugt ein Array, welches alle
# Indices aller geraden Zahlen enthält
indices_list = list()
for x in range(len(indices_even[0])):  # Iteriert so häufig, wie die Länge des 
    # ersten Arrays im Indexarray der geraden Zahlen
    indices_list.append(f'({indices_even[0][x]}, {indices_even[1][x]})') # fügt
    # der Liste innerhalb von Klammern die jeweiligen Werte aus der ersten und 
    # zweiten Liste des Indexarrays hinzu

#print(indices_list)  # schreibt die Liste der Koordinaten auf die Konsole
    
# Alternative:
#print(np.where(img % 2 == 0))
# np.where gibt die Koordinaten wie folgt zurück: 
# ((x1, x2, x3, ..., xn), (y1, y2, y3, ..., yn))
 
    
#list(zip(*np.where(img%2==0)))  #order
#list(zip(np.where(img%2==0)[0], np.where(img%2==0)[1]))
# sorgt für die Form ((x1, y1), (x2, y2), ...) Der * teilt das von where
# zurückgegebene Tupel in zwei eigenständige Teile auf ->
# np.where(...)[0] und np.where(...)[1], die dann wieder per Zip elementweise
# zusammengeschlossen werden (x1 mit y1, x2 mit y2, ...).