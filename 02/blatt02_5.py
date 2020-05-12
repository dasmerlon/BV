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
fig1.suptitle('without noise')
plt.imshow(mandrill, cmap = 'gray')


def scaling_image(img):
    img_m = img - np.min(img)
    img_s = 255 * (img_m / np.max(img_m))
    return img_s


def gaussian_noise(img, sigma):
    noise = np.random.normal(0, sigma, img.shape)
    img_n = img + noise
    img_s = scaling_image(img_n)
    plt.imshow(img_s, cmap = 'gray')

#the smaller the SNR, the larger the noise ratio.
    
#def salt_and_pepper_noise(img, p):
#    noise = salt + pepper
#    img_n = img + #salt and pepper noise
#    plt.imshow(img_n, cmap = 'gray')


fig2 = plt.figure(2)
fig2.suptitle('gaussian noise')
gaussian_noise(mandrill, 20)

fig3 = plt.figure(3)
fig3.suptitle('salt-and-pepper noise')
#salt_and_pepper_noise(mandrill, 0.5)

plt.show()