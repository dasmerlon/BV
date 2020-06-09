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

plt.imshow(imgR)
plt.imshow(imgG)
plt.imshow(imgB)


