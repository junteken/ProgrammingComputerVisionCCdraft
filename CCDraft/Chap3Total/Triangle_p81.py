import Homography_p75

from scipy import ndimage
from PIL import Image
from pylab import *


im1= array(Image.open('lena.jpg').convert('L'))
im2= array(Image.open('empire.jpg').convert('L'))

tp= array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])

m,n= im1.shape[:2]
fp= array([[0,m,m,0], [0,0,n,n], [1,1,1,1]])

#first triangle
tp2= tp[:,:3]
fp2= fp[:,:3]

#compute H
H= Homography_p75.Haffine_from_points(tp2, fp2)
im1_t= ndimage.affine_transform(im1, H[:2, :2], (H[0,2], H[1,2]), im2.shape[:2])

#alpha for triangle
alpha= warp.alpha_for_triangle(tp2, im2.shape[0], im2.shape[1])
im3= (1-alpha)*im2+alpha*im1_t

#second traingle
tp2= tp[:, [0,2,3]]
fp2= fp[:, [0,2,3]]

H= Homography_p75.Haffine_from_points(tp2, fp2)
im1_t= ndimage.affine_transform(im1, H[:2, :2], (H[0,2], H[1,2]), im2.shape[:2])

#alpha for triangle
alpha= warp.alpha_for_triangle(tp2, im2.shape[0], im2.shape[1])
im4= (1-alpha)*im3+alpha*im1_t


figure()
gray()
imshow(im4)
axis('equal')
axis('off')
show()