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
fig1.suptitle('image without noise')
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

    
def salt_and_pepper_noise(img, p):
    img_n = np.empty(img.shape, np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            r = np.random.random_sample()
            if r < (p/2):
                img_n[i][j] = 0     # pepper noise
            elif r > (1 - p/2):
                img_n[i][j] = 255   # salt noise
            else:
                img_n[i][j] = img[i][j]
    plt.imshow(img_n, cmap = 'gray')


fig2 = plt.figure(2)
fig2.suptitle('image with gaussian noise')
gaussian_noise(mandrill, 30)

fig3 = plt.figure(3)
fig3.suptitle('image with salt-and-pepper noise')
salt_and_pepper_noise(mandrill, 0.2)

plt.show()