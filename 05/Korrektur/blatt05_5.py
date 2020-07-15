# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
         
         
Aufgabe 5 — Grauwert vs. Farbton
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2hsv


"""
1. Wandelt zunächst die vier Blumenbilder in Grauwertbilder um und berechnet 
   den mittleren Grauwert des in der Maske mit Einsen markierten Bereichs je 
   Bild.
   Hinweis: Ihr könnt dazu z.B. die maskierten Arrays von numpy.ma benutzen. 
   Achtet dabei darauf, dass die Maskeneinträge dort eine entgegengesetzte 
   Wirkung haben. Werte, die in der Maske eine 1 tragen, werden ignoriert.

2. Ermittelt nun den Farbton (über HSI oder HSV) für jeden Pixel und berechnet 
   je Bild den mittleren Farbton für den mit Einsen markierten Bereich.
"""
for imageID, classLabel in zip(['02881','02890','04650','04666'], 
                               ['Malve', 'Malve', 'Hahnenfuß', 'Hahnenfuß']):
    #gleichzeitiges iterieren über zwei Listen 
    print(imageID, classLabel) 
    img = imread('./blumen/image_'+imageID+'.jpg') 
    mask = imread('./blumen/image_'+imageID+'_maske.png') 
    #die Maske kann ganz normal gelesen werden
    grey = np.mean(img, axis=2) 
    #Grauwert als Mittelwert der drei Farbwerte -> Mittelung über die Achse 2 
    hue = rgb2hsv(img)[:,:,0] 
    #Unwandlung in HSV-Farbraun und Extraktion des Farbwert-Kanals 
    plt.figure(plt.gcf().number+1) 
    plt.imshow(img) 
    plt.figure(plt.gcf().number+1) 
    plt.imshow(mask*255, cmap='gray') 

    maskedGrey = np.ma.array(grey, mask=1-mask)
    #gegebene Maske muss gedreht werden, da hier 1 Hintergund bedeutet 
    maskedHue = np.ma.array(hue, mask=1-mask) 
    greyMean = np.ma.mean(maskedGrey) 
    #Mittelwert auf Vordergrund berechnen über np.ma.mean 
    hueMean = np.ma.mean(maskedHue)

    #Alternative:
#    hueMean = np.mean(hue[mask==1])
#    greyMean = np.mean(img[mask==1])
    print(greyMean, hueMean)
    
    
"""
3. Vergleicht die Werte und beschreibt was euch auffällt. Sind der mittlere 
   Farbton bzw. Grauwert gleich gut geeignet, um die beiden Blumenarten zu 
   unterschieden? Warum oder warum nicht?
"""