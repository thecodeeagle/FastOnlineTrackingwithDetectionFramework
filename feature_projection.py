# Generated with SMOP  0.41
from libsmop import *
# .\feature_projection.m

    
@function
def feature_projection(x_npca=None,x_pca=None,projection_matrix=None,cos_window=None,*args,**kwargs):
    varargin = feature_projection.varargin
    nargin = feature_projection.nargin

    # z = feature_projection(x_npca, x_pca, projection_matrix, cos_window)
    
    # Calculates the compressed feature map by mapping the PCA features with
# the projection matrix and concatinates this with the non-PCA features.
# The feature map is then windowed.
    
    if isempty(x_pca):
        # if no PCA-features exist, only use non-PCA
        z=copy(x_npca)
# .\feature_projection.m:11
    else:
        # get dimensions
        height,width=size(cos_window,nargout=2)
# .\feature_projection.m:14
        num_pca_in,num_pca_out=size(projection_matrix,nargout=2)
# .\feature_projection.m:15
        # to a window
        x_proj_pca=reshape(dot(x_pca,projection_matrix),concat([height,width,num_pca_out]))
# .\feature_projection.m:19
        if isempty(x_npca):
            z=copy(x_proj_pca)
# .\feature_projection.m:23
        else:
            z=cat(3,x_npca,x_proj_pca)
# .\feature_projection.m:25
    
    # do the windowing of the output
    z=bsxfun(times,cos_window,z)
# .\feature_projection.m:30
    return z
    
if __name__ == '__main__':
    pass
    