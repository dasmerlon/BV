# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 3 — Serienbild

In der Vorlesung wurde das Mitteln über mehrere zeitlich versetzt aufgenommene 
Bilder einer identischen Szene als Möglichkeit zur Unterdrückung des Rauschens 
präsentiert. Diese Idee soll in dieser Aufgabe genutzt werden, um die 
Einzelbilder eines Serienfotos zu einem Bild zusammenzusetzen. Dabei zeigt das 
Serienfoto die Bewegung eines Balls über eine Tischplatte. Das Endergebnis soll 
alle fünf Stadien der Bewegung aus den Einzelbildern auf einem Bild vereinen.
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave


plt.close('all')

"""
1. Ladet die fünf Einzelbilder des serienbild.zip aus dem Moodle in Python. 
   Zunächst muss aus den fünf Einzelbildern ein möglichst perfektes 
   Hintergrundbild ohne Ball erzeugt werden, ähnlich dem in Abbildung 1b. 
   Wenn man den Ball als Rauschen annimmt, kann man nach dem Gesetz der großen 
   Zahlen durch Mittelung über die Bilder das Rauschen, bzw. hier den Ball, 
   zumindest recht gut entfernen. 
   Reichen fünf Bilder dafür aus? Probiert es aus!
"""
bild1 = imread('./serienbild/bild1.png')
bild2 = imread('./serienbild/bild2.png')
bild3 = imread('./serienbild/bild3.png')
bild4 = imread('./serienbild/bild4.png')
bild5 = imread('./serienbild/bild5.png')

test = 1/5 * bild1 + 1/5 * bild2 + 1/5 * bild3 + 1/5 * bild4 + 1/5 * bild5
fig1 = plt.figure(1)
fig1.suptitle('Mittelung über die Bilder nach dem Gesetz der großen Zahlen')
plt.imshow(test, cmap='gray')  # 5 Bilder reichen nicht


"""
2. Überprüft das Ergebnis visuell und überlegt euch eine bessere aber sehr 
   ähnliche Möglichkeit für das Verknüpfen der fünf Pixel an jeweils einer 
   Koordinate. Betrachtet dabei keine anderen Koordinaten wie etwa die der 
   Nachbarn! Das Ergebnis soll dabei dem in Abbildung 1b so nahe wie möglich 
   kommen.
"""
bilder = np.stack((bild1, bild2, bild3, bild4, bild5), axis=2)
# Ersetzt jeden Pixel durch den Mittelwert der Bilderfolge
hintergrund = np.median(bilder, axis=2).astype(np.uint8)

fig2 = plt.figure(2)
fig2.suptitle('Hintergrundbild')
plt.imshow(hintergrund, cmap='gray')


"""
3. Nutzt nun euer erzeugtes Hintergrundbild, um die veränderten Pixel in jedem 
   der fünf Einzelbilder zu ermitteln. Damit ihr wirkliche Veränderungen vom 
   Grundrauschen unterscheiden könnt, empfiehlt sich die Nutzung eines 
   Schwellenwerts für die Mindeststärke der Veränderung. Den Schwellenwert 
   müsst ihr selbst ermitteln. Ein perfektes Ergebnis werdet ihr aber 
   vermutlich nicht bekommen, wie auch im Ergebnisbild 1c zu erkennen ist.
"""
ball1 = (bild1 - hintergrund) > 10
ball2 = ((bild2 - hintergrund) > 15) * ((bild2 - hintergrund) < 250)
ball3 = ((bild3 - hintergrund) > 10) * ((bild3 - hintergrund) < 240)
ball4 = ((bild4 - hintergrund) > 10) * ((bild4 - hintergrund) < 240)
ball5 = ((bild5 - hintergrund) > 13) * ((bild5 - hintergrund) < 220)

print(bild4)
print(hintergrund)
plt.imshow(ball5, cmap='gray') 

"""
4. Ersetzt nacheinander für jedes der fünf Bilder die veränderten Pixel im 
   Hintergrundbild durch die entsprechenden Pixel des Einzelbildes. D.h. die 
   Pixel, die sich zwischen dem Hintergrundbild und dem ersten Einzelbild 
   verändert haben, werden im Hintergrundbild durch die entsprechenden Pixel 
   des ersten Einzelbilds ersetzt usw.
"""
ball1 = np.where(ball1==1, bild1, hintergrund)
ball2 = np.where(ball2==1, bild2, ball1)
ball3 = np.where(ball3==1, bild3, ball2)
ball4 = np.where(ball4==1, bild4, ball3)
ball5 = np.where(ball5==1, bild5, ball4)

fig3 = plt.figure(3)
fig3.suptitle('alle Bälle')
plt.imshow(ball5, cmap='gray')


"""
5. Speichert das Ergebnisbild ab. Es sollte in etwa dem in Abbildung 1c 
   entsprechen.Tipp: Nehmt selbst ein Serienfotos oder Einzelfotos auf und 
   versucht euer Verfahren darauf anzuwenden. Achtet dabei auf eine möglichst 
   ruhige Kamera und benutzt wenn möglich ein Stativ. Um ein Farbbild in ein 
   Graustufenbild umzuwandeln, könnt ihr die Funktion skimage.color.rgb2gray 
   nutzen und das Ergebnis mit 255 multiplizieren. Originelle Ergebnisse werden 
   in den Lösungsvideos gezeigt.
"""
imsave('./serienbild/alle_baelle.png', ball5)

plt.show()










