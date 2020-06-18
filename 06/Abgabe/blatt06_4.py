# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
import math

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
histogram2 = np.histogram(bild2, bins = 256, range = (0,256), density = True)

f, f1 = plt.subplots(1,2)
f.suptitle('Image #1: Normalized Histogram vs Equalized Histogram')
f, f2 = plt.subplots(1,2)
f.suptitle('Image #2: Normalized Histogram vs Equalized Histogram')

f1[0].hist(bild1.flatten(), bins = 256, range = (0,256), density = True)
f1[0].hist(histogram1, bins = 256, range = (0,256), density = True)

f2[0].hist(bild2.flatten(), bins = 256, range = (0,256), density = True)
f2[0].hist(histogram2, bins = 256, range = (0,256), density = True)


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


def EqualizeHistogram(histogram, image):
    referenceHistogram = histogram
    transformFunc = np.array(range(0,256))
    #print(referenceHistogram[0][0] * 255)
    
    transformFunc[0] = referenceHistogram[0][0] * 255
    for i in range(1,256):
        transformFunc[i] = transformFunc[i-1] + referenceHistogram[0][i] * 255
        histogram[0][i] = transformFunc[i]
       
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x,y] = transformFunc[image[x,y]]
    return transformFunc


eq_bild1 = bild1.copy()
transformFunction1 = EqualizeHistogram(histogram1, eq_bild1)
f1[1].hist(bild1.flatten(), bins = 256, range = (0,256), density = True)
f1[1].hist(histogram1, bins = 256, range = (0,256), density = True)

eq_bild2 = bild2.copy()
transformFunction2 = EqualizeHistogram(histogram2, eq_bild2)
f2[1].hist(bild2.flatten(), bins = 256, range = (0,256), density = True)
f2[1].hist(histogram2, bins = 256, range = (0,256), density = True)

f, f5 = plt.subplots(1,3)
f.suptitle('Image #1 vs Intensity Transformation vs Histogram Equalization')
f, f6 = plt.subplots(1,3) 
f.suptitle('Image #2 vs Intensity Transformation vs Histogram Equalization')
f, f7 = plt.subplots(1,2) 
f.suptitle('Image #1: Transformation Function of Intensity Transformation vs Histogram Equalization')
f, f8 = plt.subplots(1,2) 
f.suptitle('Image #2: Transformation Function of Intensity Transformation vs Histogram Equalization')

f5[0].imshow(bild1, cmap='gray', vmin=0, vmax=255)
f5[2].imshow(eq_bild1, cmap = 'gray')

f6[0].imshow(bild2, cmap='gray', vmin=0, vmax=255)
f6[2].imshow(eq_bild2, cmap = 'gray')


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

def IntensityTransform1(image):
    return ((image ** 0.2) * (255 ** 0.8))

def IntensityTransform2(image):
    return (255 * (math.e ** (image/255) * 16 - 10))/ (1 + math.e ** (image/255) * 16 - 10)


afterImage1 = IntensityTransform1(bild1)
f5[1].imshow(afterImage1, cmap = 'gray')

afterImage2 = IntensityTransform2(bild2)
f6[1].imshow(afterImage2, cmap = 'gray')

f7[0].plot(range(0,256), list(map(IntensityTransform1,range(0,256))))
#plt.show()

f8[0].plot(range(0,256), list(map(IntensityTransform2,range(0,256))))
#plt.show()

f7[1].plot(range(len(transformFunction1)), transformFunction1)
#plt.show()

f8[1].plot(range(len(transformFunction2)), transformFunction2)
#plt.show()