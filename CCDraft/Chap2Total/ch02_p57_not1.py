#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch02_p57.py
#   Description : - SIFT : Scale Invariant Feature Transform
#   Author      : CHLEE / 2016. 8. 29 (월)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 02. Local Image Descriptors
#######################################################################

from pylab import *
from numpy import *
from PIL import Image

from ch02.imp import sift

# imname = "../data/empire.jpg"
# imname = 'empire.jpg'
# siftname = 'empire.sift'

imname = '../data1/book_perspective.JPG'
siftname = '../data1/book_perspective.sift'

im1 = array(Image.open(imname).convert('L'))

sift.process_image(imname, siftname)
l1, d1 = sift.read_features_from_file( siftname )

figure()
gray()
sift.plot_features(im1, l1, circle=True)
show()
