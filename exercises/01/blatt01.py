# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:36:56 2020

@author: Abdulssatar Khateb, Felix Swimmee, Merle Hoffmann 
"""

"""
Aufgabenblatt 01

Aufgabe 02
"""
import numpy as np

#Vektor u als ID-Array mit 100 Nullen.
u=np.zeros((100,))

#Vektor v als ID-Array mit [0,1,2,3,4,5,6,7,8,9,10,11]
v=np.arange(12)

#Formatänderung von v auf 2D-Array
m=np.reshape(v,(3,4))   #oder m=v.reshape(3,4)

#Einträge der Matrix m multipliziert mir dem Faktor 1.2
m=m*1.2

#Hier wird den Datentype von Array m von float auf int geändert.
m=m.astype('int')

#multipliziere m mit dem Faktor 1.2.
m=m*1.2  # Der Datentyp ist wieder float.

#Hadamard-Produkt(elementenweise Multiplikation)
for i in range(3):
    for j in range(4):
        m[i,j]=m[i,j]*m[i,j]
        

"""
Aufgabe 03
"""
#Bild in Python laden
from skimage.io import imread, imsave
img=imread("./mandrill.png")

#Bild zeigen mithilfe von Matplotlib
import matplotlib.pyplot as plt
plt.imshow(img,cmap='gray')

#Bild ausschneiden 
imschnitt=img[320:460,120:350]
plt.imshow(imschnitt,cmap='gray')

#Bildausschnitt speichern
imsave("mandrill_nase.png",imschnitt)

#Bild kopieren 
copy1=np.copy(img)
# Ein Pixel auf schwarz einsetzen.
copy1[387,240]=0

#Bild kopieren 
copy2=np.copy(img)
#Augenbereich auf schwarz einsetzen.
copy2[:200,:]=0

#Hier wird alles außer Nasenbereich auf schwartz eingesetzt.
#copy2[:320,:]=0
#copy2[461:,:]=0
#copy2[:,:120]=0
#copy2[:,351:]=0



"""
Aufgabe 04.1
"""
img=plt.imread("./mandrill.png")

#Bild an der vertikale Achse spiegeln
v_img=np.zeros((512,512))
v_img[:,:256]=img[:,::2]
v_img[:,256:]=np.fliplr(img[:,::2])

#Weitere Möglichkeiten zum vertikalen Spieglung
#Achtung ohne Verkleinerung der Bildgroße.
#np.fliplr=np.flip(img,axsi=0)=img[:,::-1]=img[...,::-1]

#Bild an der horizontale Achse spiegeln
h_img=np.zeros((512,512))
h_img[:256,:]=img[::2,:]
h_img[256:,:]=np.flipud(img[::2,:])

#Weitere Möglichkeiten zur horizontalen Spieglung.
#Achtung ohne Verkleinerung der Bildgroße.
#np.flipud=np.flip(img,axsi=1)=img[::-1,:]=img[::-1,...]
vhimg=v_img
vhimg[:256,:]=v_img[::2,:]
vhimg[256:,:]=np.flipud(v_img[::2,:])

#Bild an den vertikalen und horizontalen Achse spiegeln
vh_img=np.zeros((1024,1024))
vh_img[:512,:512]=img
vh_img[:512,512:]=np.fliplr(img)
vh_img[512:,:512]=np.flipud(img)
vh_img[512:,512:]=np.flipud(np.fliplr(img))


"""
Aufgabe 4.2
"""
#Negativ des Orginalbilds 
n_img=np.copy(img)
n_img=255- img
plt.imshow(n_img,cmap='gray')



"""
Aufgabe 4.3
"""

#Nasenspitze schneiden und ein Pixel ändern.
nase_img=img[320:460,120:350]
nase_img[60,115]=0   #Der Untersied ist nur beim zoomen bemerkbar.
#Das orginale Bild wurde entsprechend geändert


"""
Aufgabe 4.4
"""

mask_img=np.zeros((512,512))
mask_img[320:460,120:350]=1
mask_img=np.multiply(mask_img,img)








































