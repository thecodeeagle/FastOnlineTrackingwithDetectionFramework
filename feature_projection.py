
import numpy as np


def feature_projection(x_npca=[],x_pca=[[1,2,3,4],[1,2,3,4], [1,2,3,4],[1,2,3,4]] ,projection_matrix=[[1,2,3,4], [3,4,3,4], [5,6,3,4], [7,8,3,4]],cos_window=[[[1,2,3,4], [3,4,3,4]], [[1,2,3,4], [3,4,3,4]]],*args,**kwargs):

    # z = feature_projection(x_npca, x_pca, projection_matrix, cos_window)

    # Calculates the compressed feature map by mapping the PCA features with the projection matrix and concatinates this with the non-PCA features.
    # The feature map is then windowed.

    if len(x_pca)==0:
        # if no PCA-features exist, only use non-PCA
        z= np.copy(x_npca)

    else:
        # get dimensions
        height= np.array(cos_window).shape[0]
        width = np.array(cos_window).shape[1]

        num_pca_in,num_pca_out= np.shape(projection_matrix)

        # to a window
        x_proj_pca= np.reshape(np.dot(x_pca,projection_matrix),(height,width,num_pca_out))

        if len(x_npca)==0:
            z=np.copy(x_proj_pca)

        else:
            z= np.concatenate((x_npca,x_proj_pca), axis=3)


    # do the windowing of the output

    z = cos_window*z

    return z

if __name__ == '__main__':
    feature_projection()
