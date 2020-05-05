# -*- coding: utf
import matplotlib as mp
from skimage.io import imread, imsave

img = imread('mandrill.png')

#mp.pyplot.imshow(img, cmap = 'gray')

imgcropped = img[325:450, 150:350] #Y then X, not the otherway around
mp.pyplot.imshow(imgcropped, cmap = 'gray') #Teilaufgabe 3
imsave('mandrillCropped.png', imgcropped)

imgPlusOnePixel = img
imgPlusOnePixel[200,200] = 0 #Teilaufgabe 5
mp.pyplot.imshow(imgPlusOnePixel, cmap = 'gray')

imgEyesBlack = img
imgEyesBlack[25:100, 100:400] = 0
mp.pyplot.imshow(imgEyesBlack, cmap = 'gray') #teilaufgabe 6

#das program scheint nur eine figur anzuzeigen, also muss man jeweils alle anderen plots ausblenden um das
#um das richtige anzuzeigen