# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
         
         
Aufgabe 04 — Umgang mit Farbbildern in Python
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2hsv, hsv2rgb, rgb2gray


"""
1. Ladet das Bild mandrillFarbe.png aus dem Moodle und zeigt es an.
"""
img = imread('mandrillFarbe.png')
plt.figure(1).suptitle('Originalbild RGB')
plt.imshow(img) #kein cmap


"""
2. Invertiert das Bild, indem ihr jeden Farbwert einzeln im RGB-Modell 
   invertiert. Welche Farben des Ursprungsbildes werden dabei auf welche Farben 
   im neuen Bild abgebildet?
"""
inv = 255-img #Bild invertieren per Broadcasting über alle Pixel und Farbkanäle 
#Die Invertierung entspricht im Prinzp einer Umwandlung in den CMY-Farbraum, 
# wobei das Ergebnis beim Anzeigen im RGB-Farbraum interpretiert wird. Farben 
# werden als in ihre Komplementärfarben in RGB-Farbraun umgewandelt 
# (Rot -> Cyan), (Grün -> Magenta), (Blau -> Gelb) 
plt.figure(2).suptitle('invertiertes Bild')
plt.imshow(inv) #kein cmap 


"""
3. Zerlegt das Bild in seine einzelnen Farbkanäle als Graustufenbilder und 
   zeigt diese an. Was sagen euch die Helligkeitswerte in den drei 
   Einzelbildern?
"""
R =img[:,:,0] #Farbkanal auswählen 
G =img[:,:,1]
B =img[:,:,2]
plt.figure(3).suptitle('Rotkanal')
plt.imshow(R, cmap='gray', vmin=0, vmax=255) 
#Helle Werte zeigen Bereiche, die viel Rot enthalten 
plt.figure(4).suptitle('Grünkanal')
plt.imshow(G, cmap='gray', vmin=0, vmax=255) 
#Helle Werte zeigen Bereiche, die viel Grün enthalten 
plt.figure(5).suptitle('Blaukanal')
plt.imshow(B, cmap='gray', vmin=0, vmax=255) 
#Helle Werte zeigen Bereiche, die viel Blau enthalten 


"""
4. Setzt nun die drei Farbkanäle wieder zusammen zu einem RGB-Bild. Tauscht 
   dabei aber die Kanäle Rot und Blau. Wie verändert sich das Bild und warum 
   ist das so?
""" 
imgFalseColors = np.dstack([B,G,R])
plt.figure(6).suptitle('Falschfarbenbild (Rot und Blau getauscht)')
plt.imshow(imgFalseColors)
#Da die Farbkanäle Rot und Blau nun getauscht sind, ist der Mittelteil der Nase
# des Mandrills nun leuchtend blau und die umliegenden Bereiche orange-rötlich. 


"""
5. Wandelt das RGB-Bild in ein Grauwertbilder um. Nehmt dabei an, dass sich der 
   Grauwert je Pixel als Mittelwert der drei Farbwerte an dieser Position 
   berechnet.
"""
imgGray = np.mean(img, axis=2)
#Intensität als Mittelwert der Farbwerte, daher Mittelung aber die Achse der 
# Farbkanäle 
plt.figure(7).suptitle('Grauwertbild')
plt.imshow(imgGray, cmap='gray', vmin=0, vmax=255) 

#Alternative: 
imgGray2 = rgb2gray(img) #aus skimage.color 
#Hier wird jedoch gewichtet gemittelt nach Wahrnehmung des Menschen. Nicht alle
# Farbkanäle werden von Menschen als gleich hell wahrgenommen, daher ist eine 
# Gewichtung sinnvoll: 0.2125*R + 0.7154*G + 0.0721*B. 
#Das Ergebnis liegt dann im Bereich 0...1. 
plt.figure(8).suptitle('Grauwertbild mit Gewichtung')
plt.imshow(imgGray2, cmap='gray', vmin=0, vmax=1) 


"""
6. Wie verändert sich das Bild, wenn ihr die Sättigung des Bildes voll aufdreht 
   (1) oder komplett herunterdreht (0)? Probiert es aus und erklärt die 
   Veränderungen.
   Hinweis 1: Nutzt den HSI-Farbraum und führt dort die Veränderung durch. 
   Vor dem Anzeigen müsst ihr das Bild wieder in den RGB-Farbraum zurück 
   umwandeln.
   Hinweis 2: Für die Umwandlung in den HSI-Farbraum könnt ihr eure Funktionen 
   aus Aufgabe 3 nutzen oder ihr verwendet die Funktionen skimage.color.rgb2hsv 
   bzw. skimage.color.hsv2rgb für den eng verwandten HSV-Farbraum, der sich 
   hauptsächlich in der Berechnung der Helligkeit vom HSI-Farbraum 
   unterscheidet.
"""
hsvIMG = rgb2hsv(img) #Bild in HSV-Farbraum umwandeln 
hsvIMG[:,:,1]=1 #Sättigung voll aufdrehen 
highSaturation = hsv2rgb(hsvIMG) 
plt.figure(9).suptitle('Bild mit voller Sättigung')
plt.imshow(highSaturation)
#Bei voller Sättigung gibt es wesentlich weniger Abstufungen im Bild. Jeweils 
# eine der drei Farbkomponenten ist 0. Jeder Pixel besteht daher nur noch aus 
# zwei Farben -> weniger Abstufungen. 

hsvIMG[:,:,1]=0 #Sättigung herausnehmen 
lowSaturation = hsv2rgb(hsvIMG) 
plt.figure(10).suptitle('Bild ohne Sättigung')
plt.imshow(lowSaturation)
#ohne Sättigung bleiben nur Grauwerte über 


"""
7. Verändert die Farbtöne (hue) des Bildes indem ihr alle Farbtöne im Bild um 
   jeweils 60°; 120° und 240° im HSI-Farbkreis dreht (bspw. 0° auf 60°, 
   0° auf 120°, 0° auf 240°). Welche Auswirkungen haben diese Veränderungen?
"""
for i, degree in enumerate([60,120,240]): #enumerate erzeugt einen Index -> i
    hsvIMG = rgb2hsv(img) #Biid in HSV-Farbraum umwandeln 
    rotation = degree/360 #Drehung in den Bereich 0...1 umrechnen 
    hsvIMG[:,:,0]+=rotation 
    #Alle Farbtöne um die berechnete Rotation drehen durch Aufaddieren auf
    # bisherige "Gradzahl". 
    hsvIMG = hsvIMG%1
    #Alle Werte, die jetzt größer oder gleich 1 sind wurden aus dem 
    # eigentlichen Wertebereich herausgedreht und müssen angepasst werden 
    # -> modulo 1. 
    plt.figure(11+i)
    plt.imshow(hsv2rgb(hsvIMG)) #Bild zurück umwandeln in RGB 
    #Als Ergebnis werden die Farben jeweils durch den Farbkreis rotiert und der
    # rote Mittelteil der Nase wird prägnant umgefärbt. Alle anderen Farben 
    # werden zudem gleichfarbig mitumgefärbt, sodass eine stetige aber 
    # unrealistische Farbwahrnehmung entsteht. 
    #Bei 60 wird aus der Nase, die eigentlich im von 0 Grad liegt 60 Grad, was 
    # Gelb entspricht. Bei den beiden anderen Drehungen sind es entsprechend 
    # 120 und 240 Grad, was Grün und Blau entspricht (0 Grad in den jeweiligen 
    # Sektoren)
    