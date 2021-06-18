# Generated with SMOP  0.41
from libsmop import *
# .\get_feature_map.m

    
@function
def get_feature_map(im_patch=None,features=None,w2c=None,*args,**kwargs):
    varargin = get_feature_map.varargin
    nargin = get_feature_map.nargin

    # out = get_feature_map(im_patch, features, w2c)
    
    # Extracts the given features from the image patch. w2c is the
# Color Names matrix, if used.
    
    if nargin < 3:
        w2c=[]
# .\get_feature_map.m:9
    
    # the names of the features that can be used
    valid_features=cellarray(['gray','cn'])
# .\get_feature_map.m:13
    # the dimension of the valid features
    feature_levels=concat([1,10]).T
# .\get_feature_map.m:16
    num_valid_features=length(valid_features)
# .\get_feature_map.m:18
    used_features=false(num_valid_features,1)
# .\get_feature_map.m:19
    # get the used features
    for i in arange(1,num_valid_features).reshape(-1):
        used_features[i]=any(strcmpi(valid_features[i],features))
# .\get_feature_map.m:23
    
    # total number of used feature levels
    num_feature_levels=sum(multiply(feature_levels,used_features))
# .\get_feature_map.m:27
    level=0
# .\get_feature_map.m:29
    # If grayscale image
    if size(im_patch,3) == 1:
        # Features that are available for grayscale sequances
        # Grayscale values (image intensity)
        out=single(im_patch) / 255 - 0.5
# .\get_feature_map.m:36
    else:
        # Features that are available for color sequances
        # allocate space (for speed)
        out=zeros(size(im_patch,1),size(im_patch,2),num_feature_levels,'single')
# .\get_feature_map.m:41
        if used_features(1):
            out[arange(),arange(),level + 1]=single(rgb2gray(im_patch)) / 255 - 0.5
# .\get_feature_map.m:45
            level=level + feature_levels(1)
# .\get_feature_map.m:46
        # Color Names
        if used_features(2):
            if isempty(w2c):
                # load the RGB to color name matrix if not in input
                temp=load('w2crs')
# .\get_feature_map.m:53
                w2c=temp.w2crs
# .\get_feature_map.m:54
            # extract color descriptor
            out[arange(),arange(),level + (arange(1,10))]=im2c(single(im_patch),w2c,- 2)
# .\get_feature_map.m:58
            level=level + feature_levels(2)
# .\get_feature_map.m:59
    