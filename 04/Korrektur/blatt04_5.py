# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 5 — Bilineare Interpolation

Verändert die Implementation aus Aufgabe 4 so, dass statt der nearest neighbor 
Interpolation die bilineare Interpolation genutzt wird. 
"""

import numpy as np
import matplotlib.pyplot as plt
import itertools 
from skimage.io import imread


"""
1. Fügt eurer Skalierungsfunktion aus Aufgabe 4 nun einen Parameter hinzu, der 
   die Interpolation von nearest neighbor auf bilineare Interpolation 
   umschalten kann und implementiert diese Interpolation. Nutzt dazu bspw. die 
   Beschreibung von Wikipedia.
   Hinweis 1: Für die vier benachbarten Koordinaten sucht euch erstmal nur die 
   Koordinate, deren x- und y-Wert kleiner ist. Daraus könnt ihr durch Addition 
   von 1 die anderen drei Koordinaten gewinnen.
   Hinweis 2: Achtet darauf, dass die zur Interpolation benötigten Koordinaten 
   alle im Bereich des Ursprungsbildes liegen müssen oder entsprechend 
   verändert werden müssen.
   Hinweis 3: Am rechten und unteren Seitenrand kann es zu schwarzen Streifen 
   kommen. Dies liegt daran, dass dort die benachbarten Koordinaten tlw. gleich 
   sind. Erzwingt hier eine Änderung.
   Hinweis 4: Bei der Interpolation in Bildern gilt meist, dass die 
   benachbarten Koordinaten zwischen denen interpoliert wird, einen Abstand von 
   1 entlang der x- bzw. y-Achse haben. Daher lassen sich die Formeln der 
   bilinearen Interpolation vereinfachen.
"""
def scaleImgBiI(img, factor): 
    orgH, orgW = img.shape
    newH = round(orgH*factor) #neue Bildhöhe berechnen und auf int runden
    newW = round(orgW*factor) #neue Bildbreite berechnen und auf int runden
    indices = np.array(list(itertools.product(np.linspace(0,orgH-1,newH),
                                              np.linspace(0,orgW-1,newW))))
    #bis hierher ist das Prinzip wie bei Aufgabe 4 

    #Alle nachfolgenden Schritte werden per Broadcasting über alle Koordinaten 
    # gleichzeitig durchgeführt. Die Nutzung von Schleifen ist aber auch 
    # möglich. 

    x = indices[:,0] 
    #x-Koordinaten aller Pixel des neuen Bildes im alten Bild 
    y = indices[:,1] 
    #y-Koordinaten aller Pixel des neuen Bildes im alten Bild 
    x1 = np.clip(np.floor(x).astype(np.int), 0, orgH-2) 
    #Die x-Koordinaten des alten Bildes werden abgerundet, um die 'obere' 
    # Nachbarkoordinate zu finden. Das Clipping dient der Verhinderung von 
    # Überläufern und dem Erzwingen eines unteren Nachbarns (daher -2). 
    x2 = np.clip(x1+1, 0, orgH-1) 
    #die 'untere' Nachbarkoordinate wird aus der 'oberen’ generiert 
    y1 = np.clip(np.floor(y).astype(np.int), 0, orgW-2) 
    #Die y-Koordinaten des alten Bildes werden abgerundet, um die 'linke' 
    # Nachbarkoordinate zu finden. Das Clipping dient der Verhinderung von 
    # Überläufern und dem Erzwingen eines rechten Nachbarns (daher -2). 
    y2 = np.clip(y1+1, 0, orgW-1) 
    #die 'rechte' Nachbarkoordinate wird aus der 'linken' generiert 

    result = (y2-y)*((x2-x)*img[x1,y1]+(x-x1)*img[x2,y1])+\
    (y-y1)*((x2-x)*img[x1,y2]+(x-x1)*img[x2,y2]) 
    #Bilineare Interpolation zunächst entlang der x-Achse bei y1 und y2, dann 
    # entlang der y-Achse zwischen (x‚y1) und (x‚y2). Diese verkürzte Formel 
    # nutzt die Eigenschaft, dass die Koordinaten x1 und x2 bzw. y1 und y2
    # einen Abstand von 1 haben und daher in den Brüchen weggelassen werden 
    # können. 

    #Alternative Berechnung in mehreren Schritten: 
#   Ia = img[ x1, y1 ] 
#   Ib = img[ x2, y1 ] 
#   Ic = img[ x1, y2 ] 
#   Id = img[ x2, y2 ] 
#
#   wa = (y2-y) * (x2-x)  
#   wb = (y2-y) * (x-x1) 
#   wc = (y-y1) * (x2-x) 
#   wd = (y-y1) * (x-x1) 
#
#   result = wa*Ia + wb*Ib + wc*Ic + wd*Id 
    return result.reshape(newH, newW)


def scaleImgNN(img, factor): 
    orgH, orgW = img.shape
    newH = round(orgH*factor) #neue Bildhöhe berechnen und auf int runden
    newW = round(orgW*factor) #neue Bildbreite berechnen und auf int runden
    indices = np.array(list(itertools.product(np.linspace(0,orgH-1,newH),
                                              np.linspace(0,orgW-1,newW))))
    interpolatedIndices = np.round(indices).astype(np.int)    
    return img[interpolatedIndices[:,0],interpolatedIndices[:,1]].reshape(newH,newW)


"""
2. Testet auch die Skalierung mit bilinearer Interpolation am Bild tv.png aus 
   dem Moodle. Welche Unterschiede erkennt ihr in den Ergebnissen?
"""
img = imread('tv.png') 
plt.figure(1).suptitle('Originalbild')
plt.imshow(img, cmap='gray') 

rescaledImg = scaleImgBiI(img, 5) #Vergrößerung um den Faktor 5
plt.figure(2).suptitle('vergrößertes Bild - Bilineare Interpolation')
plt.imshow(rescaledImg, cmap='gray') 

plt.figure(3).suptitle('vergrößertes Bild - Nearest Neighbor Interpolation')
plt.imshow(scaleImgNN(img, 5), cmap='gray') 
#Der Unterschied ist klar zu erkennen, durch die bilineare Interpolation 
# entstehen weichere Kanten als bei der nearest neighbor Interpolation. In 
# echten Bildern entsteht so meist ein realistischerer Eindruck.