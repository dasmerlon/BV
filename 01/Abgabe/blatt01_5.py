# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
         
         
Aufgabe 5 — Broadcasting vs. Schleifen in NumPy

Nun wollen wir die Vorteile des Broadcastings in NumPy gegenüber Schleifen 
bemessen. Dazu soll eine Abfrage am Bild einmal mit Schleifen und einmal 
mittels Broadcasting ausgeführt werden. Nebenbei wird die Ausführungszeit mit 
Hilfe der Funktion time.time gemessen. Ein Beispiel für die Verwendung von 
time.time zur Messung von Ausführungszeiten findet ihr unten. Im Rahmen dieser
Aufgabe ist nur die Nutzung von NumPy, skimage.io.imread zum Laden eines Bildes
sowie der Funktion time.time zur Zeitmessung erlaubt.
"""

import time
import numpy as np
from skimage.io import imread


"""
1. Schreibt eine Python-Funktion, die ein Bild als NumPy-Array annimmt und für
   jeden Arrayeinträge bzw. Pixel prüft, ob der Pixelwert zwischen 99 und 200
   liegt. Umgesetzt werden soll dies durch einer Iteration über das Bild 
   mittels zweier for-Schleifen.
"""
# Die Funktion erhält ein Bild als NumPy-Array und prüft alle Pixelwerte,
# ob sie zwischen 99 und 200 liegen. Die Funktion erzeugt ein NumPy-Array mit 
# booleschen Werten, wobei True bedeutet, dass der Pixel an dieser Stelle in 
# dem Bereich lag und False das Gegenteil.
def range_check_with_loops(img):
    bool_list = list()                # Deklaration einer leeren Liste
    for x in range(img.shape[0]):     # Iteration über die Zeilen des Bildes
        for y in range(img.shape[1]): # Iteration über die Spalten des Bildes
            if 99 < img[x,y] < 200:   # prüft den Pixel an der Stelle (x,y)
                bool_list += [True]      # fügt der Liste True hinzu
            else:
                bool_list += [False]      # fügt der Liste False hinzu
    np.reshape(np.array(bool_list), (img.shape))  # erzeugt ein 
    # Array aus der Liste in Form des übergebenen Bildes
    

"""
2. Schreibt eine zweite Funktion für selbigen Zweck. Diesmal jedoch mit 
   Broadcasting, d.h. komplett ohne die Benutzung von Schleifen.
"""
# Die Funktion erhält ein Bild als NumPy-Array und prüft alle Pixelwerte,
# ob sie zwischen 99 und 200 liegen. Die Funktion erzeugt ein NumPy-Array mit 
# booleschen Werten, wobei True bedeutet, dass der Pixel an dieser Stelle in 
# dem Bereich lag und False das Gegenteil.
def range_check_with_broadcasting(img):
    min_array = np.full(img.shape, 99)   # erzeugt ein Array nur mit 99
    max_array = np.full(img.shape, 200)  # erzeugt ein Array nur mit 200
    bigger_array = min_array < img  # erzeugt ein Array mit Boolwerten, wobei
    # an den Stellen, an denen der Pixelwert größer als 99 ist, True ist
    smaller_array = img < max_array # -"- ...kleiner als 200 ist, True ist
    bigger_array == smaller_array  # erzeugt ein Array mit Bool-
    # werten, wenn in beiden Arrays auf der gleichen Stelle das gleiche steht
        
      
"""
3. Messt wie lange 100 Aufrufe der beiden Funktionen jeweils auf das Bild
   mandrill.png aus dem Moodle dauern. Um die beiden Funktionen aufzurufen, 
   dürft ihr natürlich Schleifen verwenden. Wie groß ist der Unterschied?
"""
def measure_time(function):
    tic = time.time()     # speichert die Startzeit
    for x in range(100):  # Iteriert 100 mal
        function(imread('./mandrill.png')) # führt die übergebene Funktion auf
        # dem Bild mandrill.png aus
    toc = time.time()     # speichert die Endzeit
    diff = toc-tic        
    print(diff)           # schreibt die vergangene Zeit auf die Konsole


measure_time(range_check_with_loops)         # ca. 70 sec
measure_time(range_check_with_broadcasting)  # ca   0.5 sec
# Die Funktion mit den for-Schleifen braucht wesentlich länger, als die
# Funktion mit Broadcasting.
# 