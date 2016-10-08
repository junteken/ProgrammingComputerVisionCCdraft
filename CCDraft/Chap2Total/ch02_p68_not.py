#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch02_p68.py
#   Description : - Matching Geotagged Image
#   Author      : CHLEE / 2016. 8. 29 (월)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 02. Local Image Descriptors
#######################################################################

from numpy import *
from PIL import Image
import pydot
import os

def get_imlist(path):
   """ Returns a list of filenames for
   all jpg images in a directory. """
   return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

path = '../data'
# path = 'C:\(PCV_with_Python)\Source\Image'
imlist = get_imlist(path)

nbr_images = len( imlist )
print "imlist=", imlist
print "imlist no=", nbr_images

threshold = 2                                              # min number of matches needed to create link
matchscores = zeros((nbr_images, nbr_images))

g = pydot.Dot(graph_type='graph')                           # don't want the default directed graph

for i in range( nbr_images ):
   for j in range(i+1, nbr_images):
      if matchscores[i, j] > threshold:
         #first image in pair
         im = Image.open(imlist[i])
         im.thumbnail((300, 300))
         filename = str(i) + '.png'
         im.save(filename)                                 # need temporary files of the right size
         g.add_node(pydot.Node(str(i), fontcolor='transparent', shape='rectangle', image=path+filename))

         # second image in pair
         im = Image.open(imlist[j])
         im.thumbnail((300, 400))
         filename = str(j) + '.png'
         im.save(filename)                                 # need temporary files of the right size
         g.add_node(pydot.Node(str(j), fontcolor='transparent', shape='rectangle', image=path+filename))
         g.add_edge(pydot.Edge(str(i), str(j)))

# g.write_png('whitehouse.png')
# g.write('whitehouse.png')

g.write_png('whitehouse.png', prog='neato.bat')
