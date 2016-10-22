from scipy import ndimage
from PIL import Image
from pylab import *
from scipy.cluster.vq import *


class1= 1.5* randn(3,3,3)
print('class1=' ,class1)

ndx= where(class1>0)

print('ndx=', ndx)