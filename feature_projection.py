

def feature_projection(x_npca=None,x_pca=None,projection_matrix=None,cos_window=None,*args,**kwargs):


    # z = feature_projection(x_npca, x_pca, projection_matrix, cos_window)
    # Calculates the compressed feature map by mapping the PCA features with the projection matrix and concatinates this with the non-PCA features.
    # The feature map is then windowed.

    if isempty(x_pca):
        # if no PCA-features exist, only use non-PCA
        z=copy(x_npca)

    else:
        # get dimensions
        height,width=size(cos_window,nargout=2)

        num_pca_in,num_pca_out=size(projection_matrix,nargout=2)

        # to a window
        x_proj_pca=reshape(dot(x_pca,projection_matrix),concat([height,width,num_pca_out]))

        if isempty(x_npca):
            z=copy(x_proj_pca)

        else:
            z=cat(3,x_npca,x_proj_pca)


    # do the windowing of the output
    z=bsxfun(times,cos_window,z)

    return z

if __name__ == '__main__':
    feature_projection()
