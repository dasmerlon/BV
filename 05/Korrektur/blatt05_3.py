# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 3 — Farbräume umrechnen in Python

Schreibt vier Python-Funktionen, die jeweils eine der folgenden Umrechnungen 
zwischen Farbräumen für ein ganzes Bild durchführen:
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2hsv, hsv2rgb 


"""
RGB zu CMY
"""
def rgbTOcmy(img): 
    #C = 255-R
    #M = 255-G
    #Y = 255-B
    return 255-img #per Broadcasting für alle Pixel 255-Wert rechnen 


"""
CMY zu RGB
"""
def cmyTOrgb(img):
    #R = 255-C 
    #G = 255-M
    #B = 255-Y
    return 255-img #per Broadcasting für alle Pixel 255-Wert rechnen 


"""
RGB zu HSI
"""
def rgbTOhsi(img): 
    #Alle Berechnungen werden jeweils per Broadcasting gleichzeitig für alle 
    # Pixel durchgeführt 
    e = 1e-10 #kleine Konstante für den Bruch unten 
    img = img.astype(np.float)/255 #Normierung des Bildes 0...255 -> 0...1 
    R = img[:,:,0] #Rot-Kanal extrahieren
    G = img[:,:,1] #Grün-Kanal extrahieren 
    B = img[:,:,2] #Blau-Kanal extrahieren 
    #Formeln s. VL 5, Teil 2, Folie 11 
    I = np.mean(img, axis=2) #Intensität als Mittelwert der Farbwerte 
    S = 1-(3/(e+R+G+B))*np.minimum(R,np.minimum(G,B)) #Sättigung 
    #np.minimum berechnet das elementweise Minimum zweier Arrays
    theta = np.arccos(0.5*((R-G)+(R-B))/
                      (e+(R-G)**2+(R-B)*(G-B))**0.5)*180/np.pi 
    #180/np.pi ist nötig, um den Winkel von Radians in Grad umzurechnen 
    H = np.zeros_like(I) 
    H[B<=G]=theta[B<=G] 
    #dort wo B<=G ist, wird der entsprechende theta-Wert direkt eingesetzt 
    H[B>G]=360-theta[B>G] 
    #dort wo B>G ist, wird 360 - der entsprechende theta-Wert eingesetzt 
    H/=360 #Division, um auch H in den Bereich 0 ... 1 zu bekommen 
    return np.dstack([H,S,I]) #Zusammenfügen zu einem Array/Bild


"""
HSI zu RGB
"""
def hsiTOrgb(img): 
    #Alle Berechnungen werden jeweils per Broadcasting gleichzeitig für alle 
    # Pixel durchgeführt 
    H = img[:,:,0]*360 #Uhrechnung zurück in Grad 
    S = img[:,:,1]
    I = img[:,:,2]
    R = np.zeros_like(H) #zunächst leere Bilder für die Kanäle anlegen 
    G = np.zeros_like(H)
    B = np.zeros_like(H)

    rg_sector = H<120 
    #rg_sector enthält für jedes Pixel, das zum RG-Sektor gehört, eine 1. 
    # Dadurch werden die nachfolgenden Operationen nur auf diesen Bereichen 
    # ausgeführt, da rg_sector jeweils als Auswahl für die Arrays angegeben 
    # wird. 
    B[rg_sector]=I[rg_sector]*(1-S[rg_sector])
    R[rg_sector]=I[rg_sector]*(1+(S[rg_sector]*np.cos(H[rg_sector]*np.pi/180))/
     (np.cos((60-H[rg_sector])*np.pi/180)))
    #np.pi/180 ist nötig, um den Winkel von Grad in Radians umzurechnen 
    G[rg_sector]=3*I[rg_sector]-(R[rg_sector]+B[rg_sector]) 

    gb_sector = np.logical_and(H>=120,H<240)
    #np.logical_and verknüpft die beiden Bedingungen je Pixel 
    H[gb_sector]-=120 #H senken um 120 nur für die Pixel des GB-Sektors 
    R[gb_sector] = I[gb_sector]*(1-S[gb_sector]) 
    G[gb_sector] = I[gb_sector]*(1+(S[gb_sector]* 
     np.cos(H[gb_sector]*np.pi/180))/(np.cos((60-H[gb_sector])*np.pi/180))) 
    B[gb_sector] = 3*I[gb_sector]-(R[gb_sector]+G[gb_sector])
    
    br_sector = H>=240
    H[br_sector]-=240 #H senken um 240 nur für die Pixel des BR-Sektors 
    G[br_sector] = I[br_sector]*(1-S[br_sector]) 
    B[br_sector] = I[br_sector]*(1+(S[br_sector]* 
     np.cos(H[br_sector]*np.pi/180))/(np.cos((60-H[br_sector])*np.pi/180))) 
    R[br_sector] = 3*I[br_sector]-(G[br_sector]+B[br_sector])
    
    return np.dstack([R,G,B]) #Zusammenführen zu einem Array/Bild
    

"""
Überprüft die Korrektheit eurer Implementierung, indem ihr das Farbbild
mandrillFarbe.png aus dem Moodle vom RGB-Farbraum jeweils in den CMY- bzw. 
den HSI-Farbraum konvertiert und wieder zurückrechnet.
"""
plt.close('all')

img = imread('./mandrillFarbe.png')
plt.figure(1).suptitle('Originalbild RGB')
plt.imshow(img)

cmy = rgbTOcmy(img)
rgb = cmyTOrgb(cmy)
plt.figure(2).suptitle('RGB to CMY')
plt.imshow(cmy)
plt.figure(3).suptitle('CMY to RGB')
plt.imshow(rgb)

hsi = rgbTOhsi(img)
rgb = hsiTOrgb(hsi)
plt.figure(4).suptitle('RGB to HSI')
plt.imshow(hsi)
plt.figure(5).suptitle('HSI to RGB')
plt.imshow(rgb)



hsv = rgb2hsv(img)
#Umrechnung in den sehr ähnlichen HSV-Farbraum mit der entsprechenden Funktion
# von skimage.
rgb2 = hsv2rgb(hsv)
plt.figure(6).suptitle('RGB to HSV')
plt.imshow(hsv)
plt.figure(7).suptitle('HSV to RGB')
plt.imshow(rgb2)

#Umrechnung einzelner Pixel, das Pixel wird dazu als einelementiges 3D-Array
# dargestellt.
print(np.round(hsiTOrgb(rgbTOhsi(np.array([[[255,0,0]]])))*255),
      np.round(rgbTOhsi(np.array([[[255,0,0]]])), decimals=3))
print(np.round(hsiTOrgb(rgbTOhsi(np.array([[[0,255,0]]])))*255),
      np.round(rgbTOhsi(np.array([[[0,255,0]]])), decimals=3))
print(np.round(hsiTOrgb(rgbTOhsi(np.array([[[0,0,255]]])))*255),
      np.round(rgbTOhsi(np.array([[[0,0,255]]])), decimals=3))


plt.show()