import os
import pickle
import scipy

from PIL import Image
from pylab import *
from numpy import *
from scipy.cluster.vq import *



def get_imlist(path):
    """    Returns a list of filenames for
        all jpg images in a directory. """
    rrr= [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
    return rrr


# get list of images
#imlist =  get_imlist(os.getcwd()+'\\fontimages\\a_thumbs')
imlist =  get_imlist(os.getcwd()+'\\selectedfontimages\\a_selected_thumbs')
imnbr = len(imlist)
# load model file
with open('a_pca_modes.pkl','rb') as f:
    immean = pickle.load(f)
    V = pickle.load(f)
# create matrix to store all flattened images
immatrix = array([array(Image.open(im)).flatten()
            for im in imlist],'f')
# project on the 40 first PCs
immean = immean.flatten()
projected = array([dot(V[:40],immatrix[i]-immean) for i in range(imnbr)])
# k-means
projected = whiten(projected)
centroids,distortion = kmeans(projected,4)
code,distance = vq(projected,centroids)

# plot clusters
for k in range(4):
    ind = where(code==k)[0]
    figure()
    gray()
    for i in range(minimum(len(ind),40)):
        subplot(4,10,i+1)
        imshow(immatrix[ind[i]].reshape((25,25)))
        axis('off')
show()