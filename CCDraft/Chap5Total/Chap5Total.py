import camera
from numpy import *
from PIL import Image
from pylab import *

im1= array(Image.open('001.jpg'))
im2= array(Image.open('002.jpg'))

points2D= [loadtxt('2D/00'+str(i+1)+'.corners').T for i in range(3)]

points3D= loadtxt('3D/p3D').T

corr= genfromtxt('2D/nview-corners', dtype='int', missing_values='*')

P=[camera.Camera(loadtxt('2D/00'+str(i+1)+'.P')) for i in range(3)]
