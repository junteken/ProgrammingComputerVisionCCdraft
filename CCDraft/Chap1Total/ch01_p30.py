#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p30.py
#   Description : - Pickle
#   Author      : CHLEE / 2016. 8. 26 (금)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p16)
#######################################################################

import pickle
from PIL import Image
from numpy import *
from pylab import *

# save lena.jpg -> lena.pkl
# im1 = Image.open( 'lena.jpg' )
im1 = Image.open( 'empire.jpg' )
f = open('empire.pkl', 'wb')
pickle.dump(im1, f)
f.close()

# load lena.pkl -> lena_2.jpg
# f = open( 'lena.pkl', 'rb' )
f = open( 'empire.pkl', 'rb' )
im2 = pickle.load(f)
f.close()

# im2.save('lena_2.jpg')
im2.save('empire_2.jpg')           # Pickle 로 만들었다가 재생한 파일 Size 가 더 작음

print size(im1)
print size(im2)

