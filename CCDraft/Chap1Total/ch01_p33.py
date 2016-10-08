#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p33.py
#   Description : - Image Derivatives ( Sobel Filter )
#   Author      : CHLEE / 2016. 8. 26 (금)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p16)
#######################################################################

from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im1 = array(Image.open('empire.jpg'))
figure('1.Original Image ')
imshow(im1)

im2 = array(Image.open('empire.jpg').convert('L'))
figure('2.Gray Image')

gray()
imshow(im2)

# Sobel derivative filters
imx = zeros(im2.shape)
print(imx)
filters.sobel(im2, 1, imx)
figure('3x.Sobel x-derivative')
imshow(imx)

imy = zeros(im2.shape)
filters.sobel(im2, 0, imy)
figure('3y.Sobel y-derivative')
imshow(imy)

magnitude = sqrt(imx**2+imy**2)
figure('3xy.Sobel gradient')
imshow(magnitude)

# p34 ---------------------------------------------------
sigma = 5                               # standard deviation
imx_g = zeros(im2.shape)
filters.gaussian_filter(im2, (sigma,sigma), (0,1), imx_g)
figure('4x.Gaussian Derivative Filter x')
imshow(imx_g)

imy_g = zeros(im2.shape)
filters.gaussian_filter(im2, (sigma,sigma), (1,0), imy_g)
figure('4y.Gaussian Derivative Filter y')
imshow(imy_g)

show()
