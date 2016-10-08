#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p13.py
#   Description : - PIL ( Python Imaging Library ) 사용
#                 - 이미지 파일 Loading / Display
#                 - 그레이 스케일로 변환
#                 - 미리보기 (p15)
#   Author      : CHLEE / 2016. 8. 25 (목)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p13)
#######################################################################

from PIL import Image

# Image File Load / Display (p14)
pil_im1 = Image.open('empire.jpg')
pil_im1.show()

# Gray Scale (p14)
pil_im2 = Image.open('empire.jpg').convert('L')
pil_im2.show()

# 미리보기 (p15)
# pil_im1.thumbnail((128,128))
# pil_im1.show()

# Copy / Paste (p15)
'''
box = (300, 300, 400, 400)
region = pil_im1.crop(box)
region.show()

# Rotation (180도) (p15)
region2 = region.transpose(Image.ROTATE_180)
region2.show()

# Paste (p15)
pil_im1.paste(region2, box)
pil_im1.show()

# Resize
out = pil_im2.resize((128,128))
out.show()

# Rotation (45도) (p15)
out2 = pil_im2.rotate(45)
out2.show()
'''