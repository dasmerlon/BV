# -*- coding: utf-8 -*-

"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
         
         
Die Definition des Mittelwerts I eines Bildes I könnt ihr den Folien entnehmen. Ein Durchlauf bedeutet
dabei, dass jedes Pixel nur einmal betrachtet wird. In Formel 2 ist dies daran zu erkennen, dass
der Mittelwert I nicht mehr in jedem Summanden benötigt wird, sondern nur noch einmal am Ende
abgezogen wird. Das heißt, dass der Mittelwert im selben Durchlauf parallel zur Doppelsumme in der
Varianz berechnet werden kann.
"""

"""
1. Schreibt zunächst eine Funktion, welche die Varianz nach Formel 1 in zwei Durchläufen durch
das Bild berechnet. Im ersten Durchlauf soll dabei der Mittelwert I berechnet werden und im
zweiten Durchlauf schließlich die Varianz. Nutzt dazu unbedingt zwei verschachtelte for-Schleifen
pro Durchlauf, um über die Pixel zu iterieren, und nutzt zur Berechnung keine Funktionen wie
np.mean() oder np.var(). Testet eure Funktion an dem bekannten Testbild mandrill.png aus
dem Moodle.
Tipp: Zur Abschätzung der Richtigkeit euer Ergebnisse, nicht zur Berechnung, könnt ihr das
Resultat der Funktion numpy.var(img) nutzen.
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave

img = imread('mandrill.png')
img1 = np.copy(img)

def varMit_2(img):
    m= 0
    row= img.shape[0]
    column=img.shape[1]
    for x in range(row) :
        for y in range(column):
            m += img[x,y]
    m = m/(row * column)
    v = 0
    for x in range(row):
        for y in range(column):
            v = v + ((img[x,y]-m)*(img[x,y]-m) / (row * column))
    return v 
    
print(varMit_2(img1), np.var(img)) #vergleich unsererer funktion mit der in-built numpy funktion


"""
2. Implementiert nun eine Funktion für die Varianzberechnung in einem Durchlauf nach Formel 2.
Nutzt dazu erneut unbedingt zwei verschachtelte for-Schleifen pro Durchlauf, um über die Pixel
zu iterieren, und nutzt zur Berechnung erneut keine Funktionen wie np.mean() oder np.var().
Testet eure Funktion wieder am Testbild mandrill.png.
"""


def varMit_1(img):
    m= 0
    row = img.shape[0]
    column =img.shape[1]
    for x in range(row) :
        for y in range(column):
            m += img[x,y]
    m = m/(row * column)
    v = 0
    for x in range(row):
        for y in range(column):
            v = v + (img[x,y] * img[x,y])
    v = v / (row * column)
    v = v - (m * m)
    return v 

     


"""
3. Vergleicht nun eure Implementationen im Hinblick auf das Ergebnis und auf die Ausführungszeit.
Findet und notiert eine Erklärung, warum die Ergebnisse leicht voneinander abweichen. Zum Vergleich
der Ausführungszeiten soll je Funktion 10 mal die Varianz auf dem Testbild mandrill.png
berechnet werden. Für die Zeitmessung solltet ihr auf die Funktion time.time(), die auf dem
Aufgabenblatt 1 beschrieben wurde, zurückgreifen.
"""
