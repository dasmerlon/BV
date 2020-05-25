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
frame1 = imread('./serienbild/bild1.png')
frame2 = imread('./serienbild/bild2.png')
frame3 = imread('./serienbild/bild3.png')
frame4 = imread('./serienbild/bild4.png')
frame5 = imread('./serienbild/bild5.png')

frameStack = np.dstack([frame1, frame2, frame3, frame4, frame5])
# Bilder zu einem 3D-Array stapeln, dritte Dimension gibt dann die Anzahl der
# Bilder (hier 5)

backgroundMean = np.mean(frameStack, axis=2).astype(np.uint8)
# Mittelwert über dritte Dimension berechnen, also über die fünf Grauwerte an 
# einer Koordinate in den fünf Bildern
fig1 = plt.figure(1)
fig1.suptitle('Mittelung über die Bilder nach dem Gesetz der großen Zahlen')
plt.imshow(backgroundMean, cmap='gray')  # 5 Bilder reichen nicht aus


"""
2. Überprüft das Ergebnis visuell und überlegt euch eine bessere aber sehr 
   ähnliche Möglichkeit für das Verknüpfen der fünf Pixel an jeweils einer 
   Koordinate. Betrachtet dabei keine anderen Koordinaten wie etwa die der 
   Nachbarn! Das Ergebnis soll dabei dem in Abbildung 1b so nahe wie möglich 
   kommen.
"""
background = np.median(frameStack, axis=2).astype(np.uint8)
# Mit Hilfe des Medians lässt sich ein deutlich besseres Ergebnis erziehlen, da
# im Idealfall ein Wert (Hintergrund) viermal vorkommen sollte. Der eine 
# Ausreißer hat also keinen Einfluss.
fig2 = plt.figure(2)
fig2.suptitle('Hintergrundbild')
plt.imshow(background, cmap='gray')

bgOrg = np.copy(background)
# Original des Hintergrunds anlegen, da dieser gleich sukzessive verändert wird


"""
3. Nutzt nun euer erzeugtes Hintergrundbild, um die veränderten Pixel in jedem 
   der fünf Einzelbilder zu ermitteln. Damit ihr wirkliche Veränderungen vom 
   Grundrauschen unterscheiden könnt, empfiehlt sich die Nutzung eines 
   Schwellenwerts für die Mindeststärke der Veränderung. Den Schwellenwert 
   müsst ihr selbst ermitteln. Ein perfektes Ergebnis werdet ihr aber 
   vermutlich nicht bekommen, wie auch im Ergebnisbild 1c zu erkennen ist.
   
4. Ersetzt nacheinander für jedes der fünf Bilder die veränderten Pixel im 
   Hintergrundbild durch die entsprechenden Pixel des Einzelbildes. D.h. die 
   Pixel, die sich zwischen dem Hintergrundbild und dem ersten Einzelbild 
   verändert haben, werden im Hintergrundbild durch die entsprechenden Pixel 
   des ersten Einzelbilds ersetzt usw.
"""
fig3 = plt.figure(3)
plt.imshow(np.isclose(background, frame1, atol=15), cmap='gray')
# Optionale Visualisierung der gefundenen Veränderungen

# Bild 1:
diff = 1-np.isclose(bgOrg, frame1, atol=15)
# np.isclose vergleicht elementweise, ob die Grauwerte nicht weiter als atol
# auseinander sind. D.h., es wird die absolute Differenz betrachtet. Am Ende
# muss das Ergebnis noch umgedreht werden, damit alle Pixel, bei denen diese
# Bedingung nicht zutrifft (Veränderung des Grauwerts) 1 werden und alle
# anderen 0.
#diff = np.abs(bgOrg-frame1)>15   # Alternativ
xs, ys = np.nonzero(diff)
# Ähnlich wie np.where:
# An welchen Koordinaten ist diff != 0, sprich, es gibt eine Veränderung der 
# Grauwerte zwischen den beiden Bildern an diesen Koordinaten. xs und ys sind
# jeweils alle x- und y-Koordinaten.
background[xs,ys]=frame1[xs,ys]
# Austauschen des veränderten Bildbereichs. Die Pixel aus Bild 1, die zum
# Hintergrund stark unterschiedlich sind (>15) ersetzen im Hintergrund die 
# entsprechenden Pixel.

# Bild 2:
xs, ys = np.nonzero(1-np.isclose(bgOrg, frame2, atol=15))
background[xs,ys]=frame2[xs,ys]

# Bild 3:
xs, ys = np.nonzero(1-np.isclose(bgOrg, frame3, atol=15))
background[xs,ys]=frame3[xs,ys]

# Bild 4:
xs, ys = np.nonzero(1-np.isclose(bgOrg, frame4, atol=15))
background[xs,ys]=frame4[xs,ys]

# Bild 5:
xs, ys = np.nonzero(1-np.isclose(bgOrg, frame5, atol=15))
background[xs,ys]=frame5[xs,ys]

fig4 = plt.figure(4)
fig4.suptitle('alle Bälle')
plt.imshow(background, cmap='gray')


"""
5. Speichert das Ergebnisbild ab. Es sollte in etwa dem in Abbildung 1c 
   entsprechen.
"""
#imsave('./serienbild/alle_baelle.png', background)




