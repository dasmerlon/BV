# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 4 — Bildskalierung und Interpolation

Durch die geometrische Transformation von Bildern, bspw. die uniforme 
Skalierung um einen Faktor s, werden Pixelwerte an Koordinaten des Ursprungs-
bildes benötigt, die zwischen den eigentlichen Koordinaten liegen. So kann es 
etwa vorkommen, dass ein Wert an der Koordinate (0.2, 0.8) benötigt wird. 
Da es in Bildern aber nur ganzzahlige Koordinaten gibt, muss der Pixelwert an 
der Koordinate (0.2, 0.8) interpoliert werden. Dies soll in dieser Aufgabe mit 
der nearest neighbor Interpolation im Rahmen der Bildskalierung umgesetzt 
werden. Bei der nearest neighbor Interpolation wird, wie in Abbildung 3a 
dargestellt, der Pixelwert der Koordinate genommen, die der benötigten 
Koordinate (bspw. (0.2, 0.8)) am nächsten liegt. In diesem Beispiel wäre dies 
die Koordinate (0,1).
"""

import numpy as np
import matplotlib.pyplot as plt
import itertools 
from skimage.io import imread


"""
1. Schreibt eine Python-Funktion, die ein Bild um einen gegebenen Faktor, der 
   nicht ganzzahlig sein muss, uniform skaliert. Nutzt dazu die nearest 
   neighbor Interpolation. 
   Hinweis 1: Rechnet die Koordinaten des Zielbildes in die Koordinaten des 
   Ausgangsbildes zurück und interpoliert dort.
   Hinweis 2: Die Funktion itertools.product() kann nützlich sein, um aus den 
   einzelnen x- bzw. y-Koordinaten alle Koordinaten des Bildes zu erzeugen.
"""
def scaleImg(img, factor):
    orgH, orgW = img.shape
    newH = round(orgH*factor) #neue Bildhöhe berechnen und auf int runden
    newW = round(orgW*factor) #neue Bildbreite berechnen und auf int runden
    interpolatedIndices = list(itertools.product(np.linspace(0,orgH-1,newH),
                                                 np.linspace(0,orgW-1,newW)))
    #Indizes des neuen Bildes in alten Bild (d.h. Indizes als reelle Zahlen) 
    #Details: mit np.linspace werden nur die x bzw. y-Koordinaten des neuen 
    # Bildes im alten Bild unabhängig voneinander generiert. Dazu werden so 
    # viele Indizes generiert eie es Reihen bzw. Spalten im neuen Bild gibt 
    # (newH bzw. newW). Diese Indizes liegen im Bereich 0 bis zur Höhe bzw. 
    # Breite des alten Bildes. Der Abstand zwischen den Indizes wird 
    # entsprechend gleich verteilt. 
    #itertools.product erzeugt alles mögichen elementweisen Konbinationen 
    # (kartesisches Produkt) von zwei gegebenen Listen oder Arrays. Daraus wird
    # eine Liste erzeugt, da die Funktion einen Iterator erzeugt. 

    #Alle nachfolgenden Schritte werden per Broadcasting über alle Koordinaten 
    # gieichzeitig durchgeführt. Die Nutzung von Schleifen ist aber auch 
    # möglich. 

    roundedIndices = np.round(interpolatedIndices).astype(np.int) 
    #für die nearest neighbor Interpolation muss nun lediglich jeder Index von 
    # der reellen Zahl auf eine ganze Zahl gerundet werden, um den nächsten 
    # Index im alten Bild zu bekommen. 

    return img[roundedIndices[:,0], roundedIndices[:,1]].reshape(newH,newW)
    #Diese gerundeten Indices können nun benutzt werden, um für jede Koordinate 
    # des neuen Bildes einen Pixelwert aus dem alten Bild auszulesen. Da 
    # die Indizes vorher zeilenweise erzeugt wurden, muss das Ergebnis nun 
    # lediglich in die Form des neuen Bildes gebracht werden. 


"""
2. Testet nun eure Skalierung am Bild tv.png aus dem Moodle.
"""
img = imread('tv.png') 
plt.figure(1).suptitle('Originalbild')
plt.imshow(img, cmap='gray') 

rescaledImg = scaleImg(img, 5) 
#Vergrößerung um den Faktor 5, neue Informationen werden dabei nicht gewonnen 
plt.figure(2).suptitle('vergrößertes Bild')
plt.imshow(rescaledImg, cmap='gray') 

plt.figure(3).suptitle('zunächst verkleinertes, dann vergrößertes Bild')
plt.imshow(scaleImg(scaleImg(img, .5), 2), cmap='gray') 
#Zunächst das Bild zu verkleinern und anschließend das Bild zu vergrößern führt 
# zu einem Informationsverlust, da das verkleinern einen Informationsverlust 
# nach sich zieht und das vergößern keine neuen Informationen generiert.

