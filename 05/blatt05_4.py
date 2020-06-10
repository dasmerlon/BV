"""
Aufgabe 04  Umgang mit Farbbildern in Python

4.1
Ladet das BildmandrillFarbe.pngaus dem Moodle und zeigt es an
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
import skimage.color as color

img = imread('mandrillFarbe.png')
#plt.imshow(img)


"""
4.2
Invertiert das Bild, indem ihr jeden Farbwert einzeln im RGB-Modell invertiert. Welche Farben
des Ursprungsbildes werden dabei auf welche Farben im neuen Bild abgebildet?
"""
# Es wird die Rotfarbe auf Blaufarbe abgebildet. Grün wird auf Grünabgebildet 
imgInvert = np.copy(img)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        r,g,b=img[x,y,:]
        invert_r = 255 - r
        invert_g = 255 - g
        invert_b = 255 - b
        imgInvert[x,y,:] = invert_r,invert_g,invert_b
plt.imshow(imgInvert)
#imgInvert1 = 255 - img    gleiche Ergebinss mit Broadcasting



"""
4.3
Zerlegt das Bild in seine einzelnen Farbkanäle als Graustufenbilder und zeigt diese an. Was sagen
euch die Helligkeitswerte in den drei Einzelbildern?
"""


imgR = img[:,:,0]
imgG = img[:,:,1]
imgB = img[:,:,2]

#plt.imshow(imgR)
#plt.imshow(imgG)
#plt.imshow(imgB)


"""
4.4
Setzt nun die drei Farbkanäle wieder zusammen zu einem RGB-Bild. Tauscht dabei aber die
Kanäle Rot und Blau. Wie verändert sich das Bild und warum ist das so?
"""

imgBR = np.dstack((imgB,imgG,imgR))
#plt.imshow(imgBR)

"""
4.5
Wandelt das RGB-Bild in ein Grauwertbilder um. Nehmt dabei an, dass sich der Grauwert je
Pixel als Mittelwert der drei Farbwerte an dieser Position berechnet.
"""

imgGray = np.mean(img,axis=2)
#plt.imshow(imgGray)


"""
4.6
Wie verändert sich das Bild, wenn ihr die Sättigung des Bildes voll aufdreht (1) oder komplett
herunterdreht (0)? Probiert es aus und erklärt die Veränderungen.
Hinweis 1: Nutzt den HSI-Farbraum und führt dort die Veränderung durch. Vor dem Anzeigen
müsst ihr das Bild wieder in den RGB-Farbraum zurück umwandeln.
Hinweis 2: Für die Umwandlung in den HSI-Farbraum könnt ihr eure Funktionen aus Aufgabe
3 nutzen oder ihr verwendet die Funktionen skimage.color.rgb2hsv bzw. skimage.color.
hsv2rgb für den eng verwandten HSV-Farbraum, der sich hauptsächlich in der Berechnung der
Helligkeit vom HSI-Farbraum unterscheidet.
"""


#Die Sättigung des Bildes auf 1 stellen
hsvS1 = color.rgb2hsv(img)
hsvS1[:,:,1] = 1
img = color.hsv2rgb(hsvS1)
plt.imshow(img)


#Die Sättigung des Bildes auf 0 stellen
hsvS0 = color.rgb2hsv(img)
hsvS0[:,:,1]= 0
#img = color.hsv2rgb(hsvS0)
#plt.imshow(img)


"""
4.7
Verändert die Farbtöne (hue) des Bildes indem ihr alle Farbtöne im Bild um jeweils 60; 120 und
240 im HSI-Farbkreis dreht (bspw. 0 auf 60, 0 auf 120, 0 auf 240). Welche Auswirkungen
haben diese Veränderungen?
"""



hsvHue = color.rgb2hsv(img)
hsvHue[:,:,0] = 60 #120,240
img=color.hsv2rgb(hsvHue)
plt.imshow(img)


