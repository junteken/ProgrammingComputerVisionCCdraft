#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p22.py
#   Description : - Numpy 사용
#                 - Image Transformation
#                   1. Original Image
#                   2. Gray Scale Image
#                   3. Invert Image
#                   4. Clamp (0 ~ 255) -> (100 ~ 200) 변환 Image
#                   5. Squared (0 ~ 255) -> (100 ~ 200) 변환 Image
#                   6. reverse of array 변환 Image
#                   7. ( uint8 + reverse of array ) 변환 Image
#   Author      : CHLEE / 2016. 8. 26 (금)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p16)
#######################################################################

from PIL import Image
from numpy import *
from pylab import *

#   1. Original Image
figure('1.Original Image')
im1 = array(Image.open('empire.jpg'))
imshow(im1)

print( int(im1.min()), int(im1.max()))

#   2. Gray Scale Image
figure('2.Gray Scale Image')
im2 = array(Image.open('empire.jpg').convert('L'))
print(im2.shape)
imshow(im2)

#   3. Invert Image
figure('3.Invert')
im3 = 255 - im2                                       # invert image
imshow(im3)

#   4. Clamp (0 ~ 255) -> (100 ~ 200) 변환 Image
figure('4.Clamp 100~255')
im4 = (100.0/255) * im2 + 100                         # clamp to interval 100...200
imshow(im4)

#   5. Squared (0 ~ 255) -> (100 ~ 200) 변환 Image
figure('5.Squared')
im5 = 255.0 * (im2/255.0)**2                          # squared
imshow(im5)

#   6. reverse of array 변환 Image
figure('6.reverse of array')
pil_im = Image.fromarray(im2)
imshow(pil_im)

#   7. ( uint8 + reverse of array ) 변환 Image
figure('7.uint8 + reverse of array')
pil_im2 = Image.fromarray(uint8(im2))
imshow(pil_im2)

show()
