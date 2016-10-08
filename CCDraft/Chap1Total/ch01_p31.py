#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p31.py
#   Description : - Blurring Image
#   Author      : CHLEE / 2016. 8. 26 (금)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p16)
#######################################################################

from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

#  p31 --------------------
im1 = array(Image.open('empire.jpg'))
im2 = array(Image.open('empire.jpg').convert('L'))
im3 = filters.gaussian_filter(im2, 10)

figure('1.Original Image')
imshow(im1)

figure('2.Gray Image')
imshow(im2)

figure('3.Gaussian Filter Image')
imshow(im3)


#  p32  --------------------
im11 = array(Image.open('empire.jpg'))
im12 = zeros(im11.shape)
for i in range(3):
   im12[:,:,i] = filters.gaussian_filter(im11[:,:,i],5)
im12 = uint8(im12)

figure('4.Gaussian Filter Image(p32)')
imshow(im12)

show()

