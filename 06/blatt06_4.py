# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave

"""

@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
Aufgabe 4 — Histogrammausgleich - 5 + 20 + 15 = 40 Punkte - Programmieraufgabe
Erlaubte (Sub-)Pakete: numpy, skimage.io, matplotlib, time
Zur Verbesserung des Kontrasts im Bild wurde in der Vorlesung der Histogrammausgleich (histogram
equalization) vorgestellt. Dieser Histogrammausgleich soll im Rahmen dieser Aufgabe implementiert und
auf verschiedene Bilder angewendet werden.
Hinweis: Bei allen Teilen dieser Aufgabe sollen zur Visualisierung der Bilder mit matplotlib.pyplot.
imshow() die Parameter vmin=0 und vmax=255 gesetzt werden (siehe auch Aufgabenblatt 4, Aufgabe
1).



1. Ladet euch das bildverbesserung.zip aus dem Moodle herunter und ladet die beiden Bilder
bild1.png und bild2.png in Python. Beide Bilder wurden bereits in Aufgabe 1 von Aufgabenblatt
4 so bearbeitet, dass der Kontrast verbessert wurde. Ermittelt für beide Bilder jeweils das
normierte Histogramm über die Funktion numpy.histogram(). Plottet zudem jeweils die Histogramme
mit Hilfe der Funktion matplotlib.pyplot.hist().
"""

plt.close('all')

bild1 = imread('bildverbesserung/bild1.png')
histogram1 = np.histogram(bild1, bins = 256, range = (0,256), density = True)

bild2 = imread('bildverbesserung/bild2.png')
histogram2 = np.histogram(bild1, bins = 256, range = (0,256), density = True)

plt.figure(1)
plt.hist(bild1.flatten(), bins = 256, range = (0,256), density = True)
plt.hist(histogram1, bins = 256, range = (0,256), density = True)
#plt.imshow(bild1, cmap='gray', vmin=0, vmax=255)

plt.figure(2)
plt.hist(bild2.flatten(), bins = 256, range = (0,256), density = True)
plt.hist(histogram2, bins = 256, range = (0,256), density = True)
#plt.imshow(bild2, cmap='gray', vmin=0, vmax=255)


"""
2. Implementiert nun selbst eine Funktion, die auf einem Bild einen Histogrammausgleich durchführt
(nutzt nicht die Funktion skimage.exposure.equalize_hist()). Verwendet dazu das normierte
Histogramm und berechnet euch die Transformationsfunktion T(rk) für jeden Grauwert nach der
Formel aus der Vorlesung. Die Transformationsfunktion selbst kann beispielsweise als 1D-Array
oder Liste gehalten werden, wobei der Listen- bzw. Arrayindex dem x-Wert und der Listen- bzw.
Arrayeintrag dem y-Wert der Transformationsfunktion entspricht. Achtet darauf, dass das Ergebnis
am Ende wieder im Bereich 0; 1; 2; : : : ; 255 liegen muss. Wendet euren Histogrammausgleich
auf die beiden Bilder bild1.png und bild2.png an. Erstellt und visualisiert erneut die jeweiligen
normierten Histogramme. Was hat sich verändert? Zeigt auch die jeweiligen Ergebnisbilder an.
"""


def EqualizeHistogram(histogram):
    eqHistogram = histogram
    
    for i in range(0,255):
        summe = 0
        for j in range(i,255):
            summe += histogram[0][j]
        eqHistogram[0][i] = 255 * summe
        
    return eqHistogram


plt.figure(3)
normiertHist1 = EqualizeHistogram(histogram1)
plt.hist(normiertHist1, bins = 256, range = (0,256), density = True)

plt.figure(4)
normiertHist2 = EqualizeHistogram(histogram2)
plt.hist(normiertHist2, bins = 256, range = (0,256), density = True)




"""
3. Visualisiert nun die Transformationsfunktionen der beiden Bilder. Dazu könnt ihr die Transformationsfunktion
je Bild als weitere Rückgabe eurer Funktion zum Histogrammausgleich setzen. Das
Plotten selbst kann wie in folgendem Beispiel dann über die Funktion matplotlib.pyplot.plot
durchgeführt werden:
    
Vergleicht nun die Ergebnisse eures Histogrammausgleichs auf den Bildern bild1.png und bild2.png
mit dem Ergebnissen (ggf. der Musterlösung) aus Aufgabe 1 von Aufgabenblatt 4. Was fällt euch
auf? Vergleicht auch die Transformationsfunktionen mit den Intensitätstransformationen der Musterlösung
aus Aufgabe 1 von Aufgabenblatt 4.

Zum Vergleich bietet es sich an, die
jeweilige Transformationsfunktion sowie die jeweilige Intensitätstransformationen zu plotten und
die Kurvenformen zu vergleichen.
"""