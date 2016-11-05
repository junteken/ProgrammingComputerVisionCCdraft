import os
import pickle
import scipy
import vocabulary
import sift

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
imlist =  get_imlist(os.getcwd()+'\\ukbench\\full')
nbr_images = len(imlist)
featlist = [ imlist[i][:-3]+'sift' for i in range(nbr_images)]

'''
for i in range(nbr_images):
    sift.process_image(imlist[i],featlist[i])
'''

voc = vocabulary.Vocabulary('ukbenchtest')
voc.train(featlist,1000,10)
# saving vocabulary
with open('vocabulary.pkl', 'wb') as f:
    pickle.dump(voc,f)
print ('vocabulary is:', voc.name, voc.nbr_words)



'''
imname = os.getcwd()+'\\book_perspective.jpg'
siftname = os.getcwd()+'\\book_perspective.sift'

im1 = array(Image.open(imname).convert('L'))

sift.process_image(imname, siftname)
l1, d1 = sift.read_features_from_file( siftname )

figure()
gray()
sift.plot_features(im1, l1, circle=True)
show()
'''