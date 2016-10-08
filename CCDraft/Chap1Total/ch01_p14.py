#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p14.py
#   Description : - PIL ( Python Imaging Library ) 사용
#                 - 다른 Format 의 이미지 파일로 저장
#   Author      : CHLEE / 2016. 8. 25 (목)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p14)
#######################################################################

from PIL import Image
import os

infile = 'empire.jpg'
outfile = os.path.splitext(infile)[0] + ".bmp"
Image.open(infile).save(outfile)

pil_im1 = Image.open('empire.jpg')
pil_im1.show()

pil_im2 = Image.open('empire.bmp')
pil_im2.show()
