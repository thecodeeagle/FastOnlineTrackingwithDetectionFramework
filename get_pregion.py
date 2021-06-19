
def get_pregion(im=None,pos=None,sz=None,*args,**kwargs):


    # [out_npca, out_pca] = get_subwindow(im, pos, sz, non_pca_features, pca_features, w2c)
    # Extracts the non-PCA and PCA features from image im at position pos and window size sz. The features are given in non_pca_features and
# pca_features. out_npca is the window of non-PCA features and out_pca is
# the PCA-features reshaped to [prod(sz) num_pca_feature_dim]. w2c is the
# Color Names matrix if used.

    if isscalar(sz):
        sz=concat([sz,sz])


    xs=floor(pos(1)) + dot(3,(arange(1,sz(1)))) - dot(1.5,floor(sz(1)))
    ys=floor(pos(2)) + dot(3,(arange(1,sz(2)))) - dot(1.5,floor(sz(2)))
    #check for out-of-bounds coordinates, and set them to the values at
#the borders
    xs[xs < 1]=1
    ys[ys < 1]=1
    xs[xs > size(im,2)]=size(im,2)
    ys[ys > size(im,1)]=size(im,1)
    x1=xs(1)
    x2=xs(end())
    y1=ys(1)
    y2=ys(end())
    return x1,y1,x2,y2

if __name__ == '__main__':
    get_pregion()
