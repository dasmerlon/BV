# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 5 — Rauschen

Erstellt ein Python-Skript mit zwei Funktionen, die jeweils das Gaußsche 
Rauschen bzw. das salt-and-pepper noise auf ein Bild applizieren. Bei der 
Funktion zum Gaußschen Rauschen soll die Standardabweichung übergeben werden 
können und bei der Funktion zum salt-and-pepper noise die Wahrscheinlichkeit 
für eine Veränderung (salt und pepper sind dann gleich wahrscheinlich).
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread


def createGaussianNoise(img, scale):
    rng = np.random.default_rng()  #Zufallsgenerator erzeugen
    gaussNoise = rng.normal(scale = scale, size=img.shape)
    # Am Zufallsgenerator für jedes Pixel im Bild einen Zufallswert aus einer 
    #Normalverteilung (Gaußverteilung) ziehen, scale gibt die 
    #Standardabweichung an
    imgGauss = img + gaussNoise
    #Addition von Originalbild mit Rauschen
    imgGauss = np.clip(imgGauss, 0, 255).astype(np.uint8)
    #clip setzt Werte unterhalb und außerhalb des angegebenen Bereichs auf die
    #Maximalwerte (x < 0 -> x=0 und x > 255 -> 255)
    return imgGauss
    
def createSPNoise(img, prob):
    rng = np.random.default_rng()
    imgSP = np.copy(img)
    spNoise = rng.random(imgSP.shape)
    #Aus einer Gleichverteilung werden Werte im Bereich von 0 bis 1 für jedes
    # Pixel gezogen
    imgSP[spNoise<prob] = 0
    #Dort im Bild, wo die gezogenen Werte kleiner als die Auftrittswahr-
    #scheinlichkeit von Salz und Pfeffer zusammen sind, werden die Pixel 
    #zunächst alle(!) auf Pepper (0=schwarz) gesetzt
    imgSP[spNoise<prob/2] = 255
    #Dort im Bild, wo die gezogenen Werte kleiner als die Auftrittswahr-
    #scheinlichkeit von Salz sind, werden die Pixel 
    #auf Salz (255=weiß) gesetzt
    return imgSP

def createSPNoise2(img, prob):
    rg = np.random.default_rng()
    spNoise = rg.choice((0, -255, 255), size=img.shape, 
                        p=(1-prob, prob/2, prob/2))
    #Für jeden Pixel wird ein Wert aus der Menge {0, 255, -255} gezogen, wobei
    #jeder Wert eine eigene Wahrscheinlichkeit hat.
    imgSP=np.clip(spNoise+img, 0, 255).astype(np.uint8)
    #Beim Addieren mit 255 wird jeder Pixel mindestens 255 (Salt) sein und
    #beim Addieren mit -255 maximal 0 (Pepper) sein. Durch das Clipping werden 
    #die Werte außerhalb von 0 und 255 auf 0 bzw. 255 begrenzt. Die Addition
    #an 0 führt zu keiner Veränderung.
    return imgSP

img=imread('mandrill.png')
plt.figure(1)
plt.imshow(img, cmap = 'gray')

imgGauss = createGaussianNoise(img, 10)
plt.figure(2)
plt.imshow(imgGauss, cmap = 'gray')

imgSP = createSPNoise(img, 0.1)
plt.figure(3)
plt.imshow(imgSP, cmap = 'gray')





    
    
    
    
    
    
    