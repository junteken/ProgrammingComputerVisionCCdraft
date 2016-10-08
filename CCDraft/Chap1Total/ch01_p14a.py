#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : ch01_p14a.py
#   Description : - PIL ( Python Imaging Library ) 사용
#                 - 지정 폴더의 이미지 파일의 리스트 생성
#   Author      : CHLEE / 2016. 8. 25 (목)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 01. Basic Image Handling and Processing (p14)
#######################################################################

import os
def get_imlist(path):

   """ Returns a list of filenames for
   all jpg images in a directory. """
   return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

path = 'C:\(PCV_with_Python)\Source\Image'
rtnstr = get_imlist(path)
print rtnstr

""" Result
Input = 'C:\(PCV_with_Python)\Source\Image'
Output = ['C:\\(PCV_with_Python)\\Source\\Image\\empire.jpg',
          'C:\\(PCV_with_Python)\\Source\\Image\\empire_1.jpg',
          'C:\\(PCV_with_Python)\\Source\\Image\\empire_2.jpg',
          'C:\\(PCV_with_Python)\\Source\\Image\\lena.jpg',
          'C:\\(PCV_with_Python)\\Source\\Image\\miraflores.jpg',
          'C:\\(PCV_with_Python)\\Source\\Image\\miraflores2.jpg',
          'C:\\(PCV_with_Python)\\Source\\Image\\pigeon.jpg']
"""
