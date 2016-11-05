import os
import pickle
import sift
import imagesearch


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

# load vocabulary
with open('vocabulary.pkl', 'rb') as f:
    voc = pickle.load(f)
# create indexer
indx = imagesearch.Indexer('test.db',voc)

indx.create_tables()
# go through all images, project features on vocabulary and insert
for i in range(nbr_images)[:100]:
    locs,descr = sift.read_features_from_file(featlist[i])
    indx.add_to_index(imlist[i],descr)
# commit to database
indx.db_commit()