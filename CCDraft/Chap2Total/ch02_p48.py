#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch02_p48.py
#   Description : - Harris Corner Detectors
#   Author      : CHLEE / 2016. 8. 29 (월)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 02. Local Image Descriptors
#######################################################################

from pylab import *
from numpy import *
from PIL import Image

from ch02.imp import harris

"""
Example of detecting Harris corner points (Figure 2-1 in the book).
"""

# open image
im = array(Image.open('../data/empire.jpg').convert('L'))
# im = array(Image.open('cal010.jpg').convert('L'))

# detect corners and plot
harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim, 10, threshold=0.01)
harris.plot_harris_points(im, filtered_coords)

# plot only 200 strongest
harris.plot_harris_points(im, filtered_coords[:200])

