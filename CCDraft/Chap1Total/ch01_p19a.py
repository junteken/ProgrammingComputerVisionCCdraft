#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p19a.py
#   Description : - Matplotlib 사용
#                 - 이미지 파일에서 클릭한 부분 표시
#   Author      : CHLEE / 2016. 8. 25 (목)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p16)
#######################################################################

from PIL import Image
from pylab import *

im = array(Image.open('empire.jpg'))
imshow(im)

print 'Please click 3 points'
x = ginput(3)

print 'you clicked:',x
show()
