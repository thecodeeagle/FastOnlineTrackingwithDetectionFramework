

def get_feature_map(im_patch=None,features=None,w2c=None,*args,**kwargs):


    # out = get_feature_map(im_patch, features, w2c)
    # Extracts the given features from the image patch. w2c is the
    # Color Names matrix, if used.

    if nargin < 3:
        w2c=[]


    # the names of the features that can be used
    valid_features=cellarray(['gray','cn'])

    # the dimension of the valid features
    feature_levels=concat([1,10]).T

    num_valid_features=length(valid_features)
    used_features=false(num_valid_features,1)

    # get the used features
    for i in arange(1,num_valid_features).reshape(-1):
        used_features[i]=any(strcmpi(valid_features[i],features))


    # total number of used feature levels
    num_feature_levels=sum(multiply(feature_levels,used_features))

    level=0

    # If grayscale image
    if size(im_patch,3) == 1:
        # Features that are available for grayscale sequances
        # Grayscale values (image intensity)
        out=single(im_patch) / 255 - 0.5

    else:
        # Features that are available for color sequances
        # allocate space (for speed)
        out=zeros(size(im_patch,1),size(im_patch,2),num_feature_levels,'single')

        if used_features(1):
            out[arange(),arange(),level + 1]=single(rgb2gray(im_patch)) / 255 - 0.5
            level=level + feature_levels(1)

        # Color Names
        if used_features(2):
            if isempty(w2c):
                # load the RGB to color name matrix if not in input
                temp=load('w2crs')

                w2c=temp.w2crs

            # extract color descriptor
            out[arange(),arange(),level + (arange(1,10))]=im2c(single(im_patch),w2c,- 2)

            level=level + feature_levels(2)
