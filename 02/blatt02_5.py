# -*- coding: utf-8 -*-
"""
@author: Merle Hoffmann (7031673), 
         Abdulssatar Khateb (6976879), 
         Felix Swimmer (7162123)
         
   
    
Aufgabe 5 — Rauschen
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread


plt.close('all')
mandrill = imread('./mandrill.png')
fig1 = plt.figure(1)
fig1.suptitle('kein Rauschen')
plt.imshow(mandrill, cmap = 'gray')


def gaussian_noise(img, sigma):
    noise = np.random.normal(0, sigma, img.shape)
    img_n = img + noise
    plt.imshow(img_n, cmap = 'gray')


#def salt_and_pepper_noise(img, p):
#    img_n = img + #salt and pepper noise
#    plt.imshow(img_n, cmap = 'gray')


fig2 = plt.figure(2)
fig2.suptitle('Gaußsches Rauschen')
gaussian_noise(mandrill, 20)


plt.show()