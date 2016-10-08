#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p19.py
#   Description : - Matplotlib 사용
#                 - 이미지를 Array 로 변환
#                 - 히스토그램 ( hist() )
#                 - 윤곽선 ( contour() )
#   Author      : CHLEE / 2016. 8. 25 (목)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p16)
#######################################################################

from PIL import Image
from pylab import *

# read image to array
pil_im1 = Image.open('empire.jpg')
pil_im1.show()

# read image to array
#im = array(Image.open('empire.jpg').convert('L'))
im = Image.open('empire.jpg').convert('L')
#imshow(im)
im.show()

print('im.shape=', im.shape)
#show()

# create a new figure
figure('histogram')
hist(im.flatten(), 8)
# hist(im.flatten(), 10)
# show()

# histogram 함수 Test
imhist, bins = histogram(im.flatten(), 8)  # ??? hist 와 차이는?
cdf = imhist.cumsum()
n_imhist, n_bins = histogram(im.flatten(), 8, normed=True)
n_cdf = n_imhist.cumsum()
print('imhist=', imhist)
print('bins=', bins)
print( 'cdf=', cdf, ' 569*800=', 569*800)

print ('n_imhist=', n_imhist)
print ('n_bins=', n_bins)
print ('n_cdf=', n_cdf, ' 569*800=', 569*800)

""" Result
( normed = False Case )
imhist= [ 12953  48315  51732 129628  99030  58933  30468  24141]
bins= [   3.    34.5   66.    97.5  129.   160.5  192.   223.5  255. ]
cdf= [ 12953  61268 113000 242628 341658 400591 431059 455200]  569*800= 455200

( normed = True Case )
n_imhist= [ 0.00090335  0.00336953  0.00360783  0.00904037  0.00690644  0.00411004  0.00212486  0.00168361]
n_bins= [   3.    34.5   66.    97.5  129.   160.5  192.   223.5  255. ]
n_cdf= [ 0.00090335  0.00427288  0.00788072  0.01692108  0.02382752  0.02793755  0.03006242  0.03174603]  569*800= 455200
"""

# don't use colors
gray()

# show contours with origin upper left corner
figure()
contour(im, origin='image')
axis('equal')
# axis('off')
show()
