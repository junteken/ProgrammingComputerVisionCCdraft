#-*- coding: utf-8 -*-
#######################################################################
#   Program Id  : Homography_p75.py
#   Description : - Homogeneous coordicates???? ????
#   Author      : JTLEE / 2016. 9. 27 (ȭ)
#   Remark      : [Book] Programming Computer Vision with Python
#                 Chap 03. Homography (p75)
#######################################################################

from scipy import ndimage
from PIL import Image
from pylab import *
def normalize(points):
    for row in points:
        row/=points[-1]
    return points

def make_homog(points):
    '''Convert a set of points(dim*n array) to homogeneous coordicates'''
    return vstack((points, ones((1, points.shape[1])))) #이렇게 만든 행렬은 구조가 첫번째행에 x좌표, 두번째행에 y좌표를 가지는 행렬이 오른쪽으로 쌓여져 가는 형태이다.


def H_from_points(fp, tp):
    '''Find homography H, such that fp is mapped to tp using the linear DLT method.
    Points are conditioned automatically.'''
    if fp.shape != tp.shape:
        raise RuntimeError('number of points do not match')

    #condition points(important for numerical reasons)
    #--from points--
    m= mean(fp[:2], axis=1)
    maxstd= max(std (fp[:2], axis=1))+1e-9
    C1= max([1/maxstd, 1/maxstd, 1])
    C1[0][2]= -m[0]/maxstd
    C1[1][2]= -m[1]/maxstd
    fp= dot(C1, fp)

    #--to points--
    m= mean(tp[:2], axis=1)
    maxstd= max(std (tp[:2], axis=1))+1e-9
    C2= max([1/maxstd, 1/maxstd, 1])
    C2[0][2]= -m[0]/maxstd
    C2[1][2]= -m[1]/maxstd
    tp= dot(C2, tp)

    #어떤 이유에서 fp-tp 점들을 위와 같이 처리를 하고 있다. 저렇게 해야 되는 먼가 중요한 이유가 있는듯하다

    #create matrix for linear method, 2 rows for each correspondence pair
    nbr_correspondences= fp.shape[1] #DLT Matrix A를 만들기 위해 매칭쌍을 이루는 fp, tp중 하나의 col값을 구한다. 
    # 이 col값의 2배만큼 행을 가지고 9개의 열을 가지는게 행렬 A이다
    A= zeros((2*nbr_correspondences, 9))

    for i in range(nbr_correspondences):#DLT matrix만드는 과정
        A[2*i]= [-fp[0][i], -fp[1][i], -1, 0, 0, 0,
                 tp[0][1]*fp[0][i], tp[0][i]*fp[1][i], tp[0][i]]
        A[2*i+1]= [0,0,0, -fp[0][i], -fp[1][i], -1,
                   tp[1][i]*fp[0][i], tp[1][i]*fp[1][i], tp[1][i]]

    U, S, V= linal.svd(A)
    H= V[8].reshape((3,3))

    #decondition
    H= dot(linalg.inv(C2), dot(H,C1))

    return H/H[2,2]

def Haffine_from_points(fp, tp):
    '''Find H, affine transformation, such that tp is affine transf of fp.'''
    if fp.shape != tp.shape:
        raise RuntimeError('number of points do not match')

    #condition points(important for numerical reasons)
    #--from points--
    m= mean(fp[:2], axis=1)
    maxstd= max(std (fp[:2], axis=1))+1e-9
    C1= diag([1/maxstd, 1/maxstd, 1])
    C1[0][2]= -m[0]/maxstd
    C1[1][2]= -m[1]/maxstd
    fp_cond= dot(C1, fp)

    #--to points--
    m= mean(tp[:2], axis=1)
    maxstd= max(std (tp[:2], axis=1))+1e-9
    C2= C1.copy()
    C2[0][2]= -m[0]/maxstd
    C2[1][2]= -m[1]/maxstd
    tp_cond= dot(C2, tp)

    A= concatenate((fp_cond[:2], tp_cond[:2]), axis=0)
    U, S, V= linalg.svd(A)

    tmp= V[:2].T
    B= tmp[:2]
    C= tmp[2:4]

    tmp2= concatenate((dot(C, linalg.pinv(B)), zeros((2,1))), axis=1)
    H=vstack((tmp2, [0,0,1]))

    #decondition
    H= dot(linalg.inv(C2), dot(H,C1))

    return H/H[2,2]

def image_in_image(im1, im2, tp):
    m,n= im1.shape[:2]
    fp= array([[0,m,m,0], [0,0,n,n], [1,1,1,1]])

    #compute affine transform and apply
    H= Haffine_from_points(tp, fp)

    im1_t= ndimage.affine_transform(im1, H[:2, :2], (H[0,2], H[1,2]), im2.shape[:2])

    alpha= (im1_t>0)

    return (1-alpha)*im2+alpha*im1_t