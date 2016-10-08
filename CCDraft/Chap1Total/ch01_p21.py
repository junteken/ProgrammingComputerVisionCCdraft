#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p21.py
#   Description : - Numpy 사용
#                 - im.shape() : (800L, 569L, 3L) (rows, columns, color channel) return
#                 - im.dtype() : uint8, float32 등 data type return
#   Author      : CHLEE / 2016. 8. 25 (목)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p16)
#######################################################################

from PIL import Image
from numpy import *

im = array(Image.open('empire.jpg'))
print(im.shape, im.dtype)

im = array(Image.open('empire.jpg').convert('L'),'f')
print (im.shape, im.dtype)
