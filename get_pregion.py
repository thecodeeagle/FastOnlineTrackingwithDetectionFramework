import math
import numpy as np
def get_pregion(im=None,pos=[7,8,3],sz=[4,5,3],*args,**kwargs):

    # [out_npca, out_pca] = get_subwindow(im, pos, sz, non_pca_features, pca_features, w2c)

    # Extracts the non-PCA and PCA features from image im at position pos and
# window size sz. The features are given in non_pca_features and
# pca_features. out_npca is the window of non-PCA features and out_pca is
# the PCA-features reshaped to [prod(sz) num_pca_feature_dim]. w2c is the
# Color Names matrix if used.


    #check for out-of-bounds coordinates, and set them to the values at
    #the borders
    xs = list(range(1,sz[0]+1))
    ys = list(range(1,sz[1]+1))

    for i in range(len(xs)):
        xs[i] = math.floor(pos[0]+np.dot(3,xs[i])-np.dot(1.5, math.floor(sz[0])))

    for i in range(len(ys)):
        ys[i] += math.floor(pos[1]+np.dot(3,ys[i])-np.dot(1.5, math.floor(sz[1])))

    for i in range(len(xs)):
        if(xs[i]<1):
            xs[i] = 1

    for i in range(len(ys)):
        if(ys[i]<1):
            ys[i] = 1

    for i in range(len(xs)):
        if(xs[i]>np.shape(im)[1]):
            xs[i]= np.shape(im)[1]

    for i in range(len(ys)):
        if(ys[i]> np.shape(im)[0]):
            ys[i]= np.shape(im)[0]


    x1=xs[0]
    x2=xs[len(xs)-1]
    y1=ys[1]
    y2=ys[len(ys)-1]
    return x1,y1,x2,y2

if __name__ == '__main__':
    pass
