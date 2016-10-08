#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p24.py
#   Description : - Numpy 사용
#                 - Histogram
#   Author      : CHLEE / 2016. 8. 26 (금)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p16)
#######################################################################

from PIL import Image
from numpy import *
from pylab import *

def imresize(im,sz):
   """  Resize an image array using PIL. """
   pil_im = Image.fromarray(uint8(im))
   return array(pil_im.resize(sz))

def histeq(im,nbr_bins=256):
   """ Histogram equalization of a grayscale image. """

   # get image histogram
   imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
   print('bins=', bins)# 0~255사이의 값들이 
   cdf = imhist.cumsum() # cumulative distribution function
   print('cdf=', cdf)#0~1사이의 값들이255개 쭉 나온다
   cdf = 255 * cdf / cdf[-1] # normalize
   print('norm cdf=', cdf)

   # use linear interpolation of cdf to find new pixel values
   im2 = interp(im.flatten(),bins[:-1],cdf)

   return im2.reshape(im.shape), cdf

#  Main ===============================================================
figure('1.Original Image')
im1 = array(Image.open('AquaTermi_lowcontrast.jpg'))
imshow(im1)

figure('2.Gray Image')
im2 = array(Image.open('AquaTermi_lowcontrast.jpg').convert('L'))
gray()
imshow(im2)

figure('3.histeq Image')
# im2, cdf = imtools.histeq(im)
im3, cdf = histeq(im2)
imshow(im3)

figure('4.histogram')
hist(im2.flatten(), 256)

figure('4a.histogram cum')
# x = range(0, 256)
x = range(0, 256)
y = cdf
print ('x=', len(x), ' ', x)
print ('y=', len(y), ' ', y)
plot(x, y)

figure('5.cdf')
hist(cdf.flatten(), 256)

print ('im3=', im3)
print ('cdf=', cdf)

show()
