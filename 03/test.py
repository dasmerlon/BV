# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:09:32 2020

@author: felix
"""


import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

plt.close('all')

img = imread('./findetDieFehler/ohneFehler.png')
pi = np.pi

result = np.copy(img)
for x in range(img.shape[0]):
    for y in range(50,img.shape[1]):
        result[x,y] = img[int(x * np.cos(pi)- y * np.sin(pi)), 
                          int(x * np.sin(pi)+ y * np.cos(pi))]
            

figure1 = plt.figure(1)
plt.imshow(img)

figure2 = plt.figure(2)
plt.imshow(result)