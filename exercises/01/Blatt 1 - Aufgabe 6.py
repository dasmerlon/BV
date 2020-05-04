# -*- coding: utf-8 -*-

import numpy as np
import skimage.io as sk

img = sk.imread('mandrill.png')

minimum = np.min(img)
maximum = np.max(img)
average = np.average(img)
std = np.std(img)

#print(np.unravel_index(np.argmin(img), img.shape)) #minimum
#print(np.unravel_index(np.argmax(img), img.shape)) #maximum

imgModulo = img % 2
amountOfValues = img.shape[0] * img.shape[1]
amountOfUnevenNumbers = np.count_nonzero(imgModulo==1)
amountOfEvenNumbers = amountOfValues - amountOfUnevenNumbers

#print(amountOfUnevenNumbers)
print(amountOfEvenNumbers)

evenArrayIndices = np.where(imgModulo == 0)
IndicesList = []
for x in range(len(evenArrayIndices[0])):
    IndicesList.append("(" + str(evenArrayIndices[0][x]) + ", " + str(evenArrayIndices[1][x]) + ")")
print(IndicesList)
