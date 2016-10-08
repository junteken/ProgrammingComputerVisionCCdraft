#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p26.py
#   Description : - 2개 이상의 영상 합치기 (compute_average(imlist))
#                 - 영상 Resize & Save
#   Author      : CHLEE / 2016. 8. 26 (금)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p16)
#######################################################################

from PIL import Image
from numpy import *
from pylab import *

def compute_average(imlist):
   """ Compute the average of a list of images. """
   # open first image and make into array of type float
   averageim = array(Image.open(imlist[0]), 'f')
   for imname in imlist[1:]:
      try:
         averageim += array(Image.open(imname))
      except:
         print (imname + '...skipped')
   averageim /= len(imlist)

   # return average as uint8
   return array (averageim, 'uint8')

#  Main ===============================================================
imlist1 = 'empire.jpg'
imlist2 = 'lena.jpg'
imlist3 = 'AquaTermi_lowcontrast.jpg'

imlist1a = 'empire_1.jpg'
imlist2a = 'lena_1.jpg'
imlist3a = 'AquaTermi_lowcontrast_1.jpg'

#  Image 1 Display (empire.jpg)
figure('1a.Original Image (empire.jpg)')
im1 = Image.open( imlist1 )
imshow(im1)
print (size(im1))

#  Image 2 Display (lena.jpg)
figure('1b.Original Image (lena.jpg)')
im2 = Image.open( imlist2 )
imshow(im2)
print (size(im2))

#  Image 3 Display (AquaTermi_lowcontrast_1.jpg)
figure('1c.Original Image (AquaTermi_lowcontrast_1.jpg)')
im3 = Image.open( imlist3 )
imshow(im3)
print (size(im3))

#  Image 1, 2 Size 같게 맞춤 & Save
sizex = 800
sizey = 1000
out_im1 = im1.resize((sizex, sizey))
out_im1.save( imlist1a )

out_im2 = im2.resize((sizex, sizey))
out_im2.save( imlist2a )

out_im3 = im3.resize((sizex, sizey))
out_im3.save( imlist3a )

#  Average Image
imlist = []
imlist.append(imlist1a)
imlist.append(imlist2a)
imlist.append(imlist3a)
im_all = compute_average(imlist)
figure('2.Average Image')
imshow(im_all)
print (size(im_all))

show()
