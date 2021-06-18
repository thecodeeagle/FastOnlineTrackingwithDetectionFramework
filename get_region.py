# Generated with SMOP  0.41
from libsmop import *
# .\get_region.m

    
@function
def get_region(im=None,pos=None,sz=None,*args,**kwargs):
    varargin = get_region.varargin
    nargin = get_region.nargin

    # [out_npca, out_pca] = get_subwindow(im, pos, sz, non_pca_features, pca_features, w2c)
    
    # Extracts the non-PCA and PCA features from image im at position pos and
# window size sz. The features are given in non_pca_features and
# pca_features. out_npca is the window of non-PCA features and out_pca is
# the PCA-features reshaped to [prod(sz) num_pca_feature_dim]. w2c is the
# Color Names matrix if used.
    
    if isscalar(sz):
        sz=concat([sz,sz])
# .\get_region.m:12
    
    xs=floor(pos(1)) + (arange(1,sz(1))) - floor(sz(1) / 2)
# .\get_region.m:15
    ys=floor(pos(2)) + (arange(1,sz(2))) - floor(sz(2) / 2)
# .\get_region.m:16
    #check for out-of-bounds coordinates, and set them to the values at
#the borders
    xs[xs < 1]=1
# .\get_region.m:20
    ys[ys < 1]=1
# .\get_region.m:21
    xs[xs > size(im,2)]=size(im,2)
# .\get_region.m:22
    ys[ys > size(im,1)]=size(im,1)
# .\get_region.m:23
    x1=xs(1)
# .\get_region.m:25
    x2=xs(end())
# .\get_region.m:26
    y1=ys(1)
# .\get_region.m:27
    y2=ys(end())
# .\get_region.m:28
    return x1,y1,x2,y2
    
if __name__ == '__main__':
    pass
    