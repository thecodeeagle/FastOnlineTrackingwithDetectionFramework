import numpy as np
import math
from get_feature_map import get_feature_map

def get_subwindow(im=np.array([((1,2,3), (4,5,6)), ((1,2,3), (4,5,6))]) ,pos=[1,2,3,4],sz=[1,5,3,4],non_pca_features=[1,2,3,4],pca_features=[1,2,3,4],w2c=[1,2,3,4],*args,**kwargs):
    # [out_npca, out_pca] = get_subwindow(im, pos, sz, non_pca_features, pca_features, w2c)

    # Extracts the non-PCA and PCA features from image im at position pos and
# window size sz. The features are given in non_pca_features and
# pca_features. out_npca is the window of non-PCA features and out_pca is
# the PCA-features reshaped to [prod(sz) num_pca_feature_dim]. w2c is the
# Color Names matrix if used.
    im = np.array(im);
    if np.isscalar(sz):
        sz= np.array([sz,sz])

    xs = list(range(1,sz[0]+1))
    ys = list(range(1,sz[1]+1))



    xs = np.array(xs)
    ys = np.array(ys)

    for i in range(len(xs)):
        xs[i] += math.floor(pos[1] - (sz[1] / 2))

    for i in range(len(ys)):
        ys[i] += math.floor(pos[0] - (sz[0] / 2))

    #the borders
    for i in range(len(xs)):
        if(xs[i]<1):
            xs[i] = 1

    for i in range(len(ys)):
        if(ys[i]<1):
            ys[i] = 1

    for i in range(len(xs)):
        if(xs[i]>im.shape[1]):
            xs[i]= im.shape[1]

    for i in range(len(ys)):
        if(ys[i]> im.shape[0]):
            ys[i]= im.shape[0]


    #extract image
    im_patch = im[:len(ys)][:len(xs)][:]


    # compute non-pca feature map
    if len(non_pca_features)!=0:
        out_npca=get_feature_map(im_patch,non_pca_features,w2c)

    else:
        out_npca=[]

    # compute pca feature map
    if len(pca_features)!=0:
        temp_pca= get_feature_map(im_patch,pca_features,w2c)
        pro_sz= math.floor(np.prod(sz))
        out_pca= np.reshape(temp_pca,(pro_sz, temp_pca.shape[2]))
    else:
        out_pca=[]

    return out_npca,out_pca

if __name__ == '__main__':
    get_subwindow()
