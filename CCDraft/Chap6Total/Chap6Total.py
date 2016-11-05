
from scipy import ndimage
from PIL import Image
from pylab import *
from scipy.cluster.vq import *

#N(\mu, \sigma^2), 
#sigma * np.random.randn(...) + mu
#Generate Matrix 100-row, 2-col dimension which have normal distribution N(0, 1.5^2)
class1= 1.5* randn(100,2)
print('class1=' ,class1)
#Generate Matrix 100-row, 2-col dimension which have normal distribution N(5, 1)
class2= randn(100,2) + bytearray([5,5])
print('class1=' ,class2)
features= vstack((class1, class2))
print('features=' ,features)

centroids, variance= kmeans(features, 2)

code, distance= vq(features, centroids)

figure()
#where���� [0]�� ���� ������ where�� return���ִ� data type�� tuple�ε� �� tuple�ȿ� ����ִ� item�� data type�� array(���ǿ� �����ϴ� index������ ������ ������, ��Ī) �� �ȴ�.
ndx= where(code==0)[0] 
plot(features[ndx,0], features[ndx,1], '*')
ndx=where(code==1)[0]
plot(features[ndx,0], features[ndx,1], 'r.')
plot(centroids[:,0], centroids[:,1], 'go')
axis('off')
show()