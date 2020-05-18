# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)



Aufgabe 2 — Erste Schritte in NumPy
   
In dieser Aufgabe sollen Matrizen und Vektoren aus NumPy-Arrays erzeugt und 
manipuliert werden. Alle Schritte sollen in Python programmiert und in einem 
Python-Skript festgehalten werden. 
Im Rahmen dieser Aufgabe ist nur die Nutzung von NumPy erlaubt.
"""

import numpy as np


"""
1. Erzeugt zunächst einen Vektor u als 1D-Array mit 100 Nullen.
"""
u = np.zeros(100)


"""
2. Erzeugt zudem einen Vektor v als 1D-Array aus der Liste:
   [0,1,2,3,4,5,6,7,8,9,10,11].
"""
#v = np.array(range(12))  # Alternative: range(12) erzeugt eine Liste von 0-11
v = np.arange(12)
# np.arange funktioniert wie range, lässt aber auch steps zu, die nicht ganzen
# Zahlen entsprechen

"""
 3. Formt den Vektor v nun in eine Matrix m (2D-Array) um, die aus drei
    Zeilen und vier Spalten besteht. Tipp: NumPy kennt eine Funktion, 
    um die Form (engl. shape) eines Arrays zu ändern.
"""
#m = np.reshape(v, (3, 4))  # Alternative
m = v.reshape((3,4))    #3*4 = 12 = Arrayinhalt

"""
4. Multipliziert alle Einträge der Matrix m mit dem konstanten Faktor 1.2.
"""
m = m * 1.2


"""
5. Ändert nun den Datentyp der Matrix m auf np.int. Tipp: Nutzt die Methode
   astype eines NumPy-Arrays.
"""
m = m.astype(np.int)


"""
6. Multipliziert alle Einträge der Matrix m erneut mit dem konstanten Faktor
   1.2. Von welchem Datentyp ist jetzt das Ergebnis?
"""
m = m * 1.2
print(m.dtype)     # Die Matrix hat nun den Datentyp float64


"""
7. Berechnet das Hadamard-Produkt (elementweise Multiplikation) der Matrix m 
   mit sich selbst.
"""
m = m * m
#print(m)

