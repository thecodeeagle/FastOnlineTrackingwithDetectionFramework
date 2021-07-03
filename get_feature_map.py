import numpy as np

def get_feature_map(im_patch=None,features=None,w2c=None,*args,**kwargs):
    # out = get_feature_map(im_patch, features, w2c)

    # Extracts the given features from the image patch. w2c is the
    # Color Names matrix, if used.

    if len(kwargs) < 3:
        w2c=[]


    # the names of the features that can be used
    valid_features= np.array(['gray','cn'])

    # the dimension of the valid features
    feature_levels= np.transpose(np.concatenate([1,10]))

    num_valid_features= len(valid_features)

    used_features= np.zeros(num_valid_features)

    # get the used features
    for i in range(num_valid_features):
        used_features[i]=any(valid_features[i]==features)


    # total number of used feature levels
    num_feature_levels= np.sum(np.multiply(feature_levels,used_features))

    level=0

    # If grayscale image
    if np.shape(im_patch)[2] == 1:
        # Features that are available for grayscale sequances
        # Grayscale values (image intensity)
        out= im_patch*1.0 / 255 - 0.5

    else:
        # Features that are available for color sequances
        # allocate space (for speed)
        out= np.zeros((np.shape(im_patch)[0],np.shape(im_patch)[1],num_feature_levels), dtype="float")

        if used_features[0]:
        #    out[:,:,level + 1]=  rgb2gray(im_patch)) / 255 - 0.5 ..

            level=level + feature_levels[0]

        # Color Names
        if used_features[1]:
            if isempty(w2c):
                # load the RGB to color name matrix if not in input
                temp=load('w2crs')

                w2c=temp.w2crs

            # extract color descriptor
    #        out[:,:,level:level+10]=  im2c(single(im_patch),w2c,- 2) ..

            level=level + feature_levels[3]
