#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : Test030.py
#   Description : - fromarray Test
#   Author      : CHLEE / 2016. 8. 26 (금)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p16)
#######################################################################

from PIL import Image
from numpy import *
from pylab import *

#   1. Original Image
figure('1.Original Image')
im1 = array(Image.open('empire.jpg'))
imshow(im1)

#   6. reverse of array 변환 Image
figure('6.reverse of array')
pil_im = Image.fromarray(im1)
imshow(pil_im)

arr = array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
farr = Image.fromarray(arr)

# print 'arr', 'farr'
print 'arr=', arr
print 'farr=', farr

