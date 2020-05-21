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
import skimage.color as color

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
img1 = imread('./serienbild/bild1.png')
img2 = imread('./serienbild/bild2.png')
img3 = imread('./serienbild/bild3.png')
img4 = imread('./serienbild/bild4.png')
img5 = imread('./serienbild/bild5.png')

law_ln = 1/5 * img1 + 1/5 * img2 + 1/5 * img3 + 1/5 * img4 + 1/5 * img5
fig1 = plt.figure(1)
fig1.suptitle('Mittelung über die Bilder nach dem Gesetz der großen Zahlen')
plt.imshow(law_ln, cmap='gray')  # 5 Bilder reichen nicht aus


"""
2. Überprüft das Ergebnis visuell und überlegt euch eine bessere aber sehr 
   ähnliche Möglichkeit für das Verknüpfen der fünf Pixel an jeweils einer 
   Koordinate. Betrachtet dabei keine anderen Koordinaten wie etwa die der 
   Nachbarn! Das Ergebnis soll dabei dem in Abbildung 1b so nahe wie möglich 
   kommen.
"""
# erzeugt eine Folge der Bilder
images = np.stack((img1, img2, img3, img4, img5), axis=2)
# ersetzt jeden Pixel durch den Mittelwert der Bilderfolge
background = np.median(images, axis=2).astype(np.uint8)

fig2 = plt.figure(2)
fig2.suptitle('Hintergrundbild')
plt.imshow(background, cmap='gray')


"""
3. Nutzt nun euer erzeugtes Hintergrundbild, um die veränderten Pixel in jedem 
   der fünf Einzelbilder zu ermitteln. Damit ihr wirkliche Veränderungen vom 
   Grundrauschen unterscheiden könnt, empfiehlt sich die Nutzung eines 
   Schwellenwerts für die Mindeststärke der Veränderung. Den Schwellenwert 
   müsst ihr selbst ermitteln. Ein perfektes Ergebnis werdet ihr aber 
   vermutlich nicht bekommen, wie auch im Ergebnisbild 1c zu erkennen ist.
"""
# erzeugt für jedes Bild eine Vordergrundmaske durch Hintergrundsubtraktion 
# und unteren und oberen Schwellenwerten
ball1 = (img1 - background) > 10
ball2 = ((img2 - background) > 15) * ((img2 - background) < 250)
ball3 = ((img3 - background) > 10) * ((img3 - background) < 240)
ball4 = ((img4 - background) > 10) * ((img4 - background) < 240)
ball5 = ((img5 - background) > 13) * ((img5 - background) < 220)


"""
4. Ersetzt nacheinander für jedes der fünf Bilder die veränderten Pixel im 
   Hintergrundbild durch die entsprechenden Pixel des Einzelbildes. D.h. die 
   Pixel, die sich zwischen dem Hintergrundbild und dem ersten Einzelbild 
   verändert haben, werden im Hintergrundbild durch die entsprechenden Pixel 
   des ersten Einzelbilds ersetzt usw.
"""
# ersetzt die entsprechenden Pixel des Hintergrunds mit den Vordergrundpixeln 
# der Vordergrundmasken (also alle Pixel mit dem Wert 1)
bg1 = np.where(ball1==1, img1, background)
bg2 = np.where(ball2==1, img2, bg1)
bg3 = np.where(ball3==1, img3, bg2)
bg4 = np.where(ball4==1, img4, bg3)
all_balls = np.where(ball5==1, img5, bg4)

fig3 = plt.figure(3)
fig3.suptitle('alle Bälle')
plt.imshow(all_balls, cmap='gray')


"""
5. Speichert das Ergebnisbild ab. Es sollte in etwa dem in Abbildung 1c 
   entsprechen.
"""
imsave('./serienbild/alle_baelle.png', all_balls)


"""
Tipp: Nehmt selbst ein Serienfotos oder Einzelfotos auf und 
      versucht euer Verfahren darauf anzuwenden. Achtet dabei auf eine 
      möglichst ruhige Kamera und benutzt wenn möglich ein Stativ. Um ein 
      Farbbild in ein Graustufenbild umzuwandeln, könnt ihr die Funktion 
      skimage.color.rgb2gray nutzen und das Ergebnis mit 255 multiplizieren. 
      Originelle Ergebnisse werden in den Lösungsvideos gezeigt.
"""
# ladet die Bilder als Graustufenbilder in Python
b0 = (color.rgb2gray(imread('./serienbild2/bild0.png')) * 255).astype(np.uint8)
b1 = (color.rgb2gray(imread('./serienbild2/bild1.png')) * 255).astype(np.uint8)
b2 = (color.rgb2gray(imread('./serienbild2/bild2.png')) * 255).astype(np.uint8)
b3 = (color.rgb2gray(imread('./serienbild2/bild3.png')) * 255).astype(np.uint8)
b4 = (color.rgb2gray(imread('./serienbild2/bild4.png')) * 255).astype(np.uint8)

# erzeugt für jedes Bild eine Vordergrundmaske
arm1 = (b1 - b0) > 5
arm2 = ((b2 - b0) > 30) * ((b2 - b0) < 180)
arm3 = ((b3 - b0) > 20) * ((b3 - b0) < 200)
arm4 = ((b4 - b0) > 30) * ((b4 - b0) < 200)

# fügt die Vordergrundmasken und den Hintergrund zusammen
arm1 = np.where(arm1==1, b1, b0)
arm2 = np.where(arm2==1, b2, arm1)
arm3 = np.where(arm3==1, b3, arm2)
arm4 = np.where(arm4==1, b4, arm3)

fig4 = plt.figure(4)
fig4.suptitle('Eigene Serienfotos:')
plt.imshow(arm4, cmap='gray')

plt.show()


