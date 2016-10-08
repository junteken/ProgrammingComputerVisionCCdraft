import Homography_p75

from scipy import ndimage
from PIL import Image
from pylab import *



'''
im = array(Image.open('empire.jpg').convert('L'))
H = array([[1.4,0.05,-100],[0.05,1.5,-100],[0,0,1]])

#H_test=array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(H[:2, :2])

im2 = ndimage.affine_transform(im,H[:2,:2],(H[0,2],H[1,2]))
figure()
gray()
imshow(im2)
show()
'''

im1= array(Image.open('lena.jpg').convert('L'))
im2= array(Image.open('empire.jpg').convert('L'))

tp= array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])
#tp= array([[1,1,1,1],[100,100,100,100],[1,1,1,1]])#�̷��� ������ lena�̹����� �ȵ��� ������ H���� �����ϴ� �ذ� ���� �����ΰ�?

im3= Homography_p75.image_in_image(im1, im2, tp)

figure()
gray()
imshow(im3)
show()