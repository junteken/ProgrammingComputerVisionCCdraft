import camera
from numpy import *
from PIL import Image
from pylab import *


#execfile('Chap5Total.py')

# make 3D points homogeneous and project
X = vstack( (points3D,ones(points3D.shape[1])) )
x = P[0].project(X)
# plotting the points in view 1
figure()
imshow(im1)
plot(points2D[0][0],points2D[0][1],' * ')
axis('off')
figure()
imshow(im1)
plot(x[0],x[1],'r.')
axis('off')

