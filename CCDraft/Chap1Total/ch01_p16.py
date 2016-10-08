#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p16.py
#   Description : - PIL ( Python Imaging Library ) 사용
#                 - 지정 폴더의 이미지 파일의 리스트 생성
#   Author      : CHLEE / 2016. 8. 25 (목)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p16)
#######################################################################

from PIL import Image
from pylab import *

# read image to array
im = array(Image.open('empire.jpg'))

# plot the image
imshow(im)

# some points
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# plot the points with red star-markers
plot(x, y, 'wo')

# line plot connecting the first two points
# plot(x[:2], y[:2])
plot(x[:2], y[:2])
plot([100,200,300,400], [100,200,300,400])

axis('off')


# add title and show the plot
title('Plotting: "empire.jpg"')
show()

