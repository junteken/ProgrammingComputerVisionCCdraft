#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch02_p66.py
#   Description : - Matching Geotagged Image
#   Author      : CHLEE / 2016. 8. 29 (월)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 02. Local Image Descriptors
#######################################################################

from ch02.imp import sift
from numpy import *

import os

def get_imlist(path):

   """ Returns a list of filenames for
   all jpg images in a directory. """
   return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

path = '../data1'
# path = 'C:\(PCV_with_Python)\Source\Image'
imlist = get_imlist(path)

nbr_images = len( imlist )
print "imglist=", imlist
print "img no=",nbr_images

featlist = [ imlist[i][:-3]+'sift' for i in range(nbr_images)]
print "featlist=", featlist

matchscores = zeros((nbr_images, nbr_images))
for i in range(nbr_images):
   for j in range(i, nbr_images):                        # only compute upper triangle
      print 'comparing ', imlist[i], imlist[j]

      l1, d1 = sift.read_features_from_file( featlist[i] )
      l2, d2 = sift.read_features_from_file( featlist[j] )
      matches = sift.match_twosided(d1, d2)
      nbr_matches = sum( matches > 0 )
      print 'number of matches = ', nbr_matches
      matchscores[i,j] = nbr_matches

# copy values
for i in range(nbr_images):
   for j in range(i+1,nbr_images): # no need to copy diagonal
      matchscores[j,i] = matchscores[i,j]

