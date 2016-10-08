#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p28.py
#   Description : - PCA ( Princial Component Analysis )
#   Author      : CHLEE / 2016. 8. 26 (금)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p16)
#######################################################################
import os

from PIL import Image
from pylab import *
from numpy import *

def pca(X):
   """ Principal Component Analysis
   input: X, matrix with training data stored as flattened arrays in rows
   return: projection matrix (with important dimensions first), variance and mean.
   """

   # get dimensions (this exam : 2359 625(25x25))
   num_data, dim = X.shape
   print('numdata and dim', num_data, dim)

   # center data
   mean_X = X.mean(axis=0)
   X = X - mean_X

   if dim > num_data:
      # PCA - compact trick used
      M = dot(X,X.T)                              # covariance matrix
      e,EV = linalg.eigh(M)                       # eigenvalues and eigenvectors
      tmp = dot(X.T,EV).T                         # this is the compact trick
      V = tmp[::-1]                               # reverse since last eigenvectors are the ones we want
      S = sqrt(e)[::-1]                           # reverse since eigenvalues are in increasing order

      for i in range(V.shape[1]):
         V[:,i] /= S
   else:
      # PCA - SVD used
      U, S, V = linalg.svd(X)
      V = V[:num_data]                            # only makes sense to return the first num_data

   # return the projection matrix, the variance and the mean
   return V, S, mean_X

def get_imlist(path):
    """    Returns a list of filenames for
        all jpg images in a directory. """

    print(path)

    rrr= [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

    print(rrr)

    return rrr

#  Main ===============================================================

# from PCV.tools import imtools, pca

# Get list of images and their size
imlist = get_imlist(os.getcwd()+'\\fontimages\\a_thumbs')                  # fontimages.zip is part of the book data set
print(imlist)

im = array(Image.open(imlist[0]))            # open one image to get the size
m, n = im.shape[:2]

# Create matrix to store all flattened images
immatrix = array([array(Image.open(imname)).flatten() for imname in imlist],'f')  ##  이거 안되네???
#immatrix = array([array(Image.open(imlist[0])).flatten() ],'f')
#immatrix += array([array(Image.open(imlist[1])).flatten() ],'f')
#immatrix += array([array(Image.open(imlist[2])).flatten() ],'f')

# Perform PCA
V, S, immean = pca(immatrix)

# Show the images (mean and 7 first modes)
# This gives figure 1-8 (p15) in the book.
figure()
gray()
subplot(2, 4, 1)

imshow(immean.reshape(m,n))

for i in range(7):
    subplot(2, 4, i+2)
    imshow(V[i].reshape(m,n))

show()
