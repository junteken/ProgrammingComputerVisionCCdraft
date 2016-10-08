#-*- coding: utf-8 -*-
"""=================================================================
   Program Id  : Test0010.py
   Description : - 함수 Test
   Author      : CHLEE / 2016. 8. 25 (목)
   Remark      :
================================================================="""
import os

def get_imlist(path):

   """ Returns a list of filenames for
   all jpg images in a directory. """
   return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def tax(bill):
    bill *= 1.08
    print( "With tax: %f" % bill )
    return bill

def tip(bill):
    bill *= 1.15
    print( "With tip: %f" % bill )
    return bill

bill = 100
bill_with_tax = tax(bill)
bill_with_tip = tip(bill)