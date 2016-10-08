#-*- coding: utf-8 -*-
"""=================================================================
   Program Id  : Test0010.py
   Description : - 함수 Test
   Author      : CHLEE / 2016. 8. 25 (목)
   Remark      :
================================================================="""

from numpy import loadtxt

# f = loadtxt( 'test.txt' )
f = loadtxt( 'empire.sift'  )

f1 = f[:, :4]
f2 = f[:, 4:]

print "f=", f
print "f1=", f1
print "f2=", f2


