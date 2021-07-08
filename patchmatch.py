import numpy as np
import math
from get_subwindow import get_subwindow
from get_pregion import get_pregion
from get_region import get_region
import math

def patchmatch(pre_im=[[[1,2,3],[2,3,4]], [[1,2,3],[2,3,4]]],pre_pos=[1,2,3,4],pre_sz=[1,2,3,4],now_im=[1,2,3,4],now_pos=[1,2,3,4],now_sz=[1,2,3,4],non_compressed_features=[1,2,3,4],compressed_features=[1,2,3,4],w2c=None,*args,**kwargs):


    num_compressed_dim=2
    lambda_=0.01
    output_sigma_factor=1 / 16
    sigma=0.2

    xo_npca,xo_pca=get_subwindow(pre_im, np.array([pre_pos[1],pre_pos[0]]),np.array([pre_sz[1],pre_sz[0]]),non_compressed_features,compressed_features,w2c)

    x1,y1,x2,y2=get_pregion(pre_im,pre_pos,pre_sz)
    x11,y11,x22,y22=get_region(now_im,now_pos,now_sz)

    if x11 < x1 or y11 < y1 or x22 > x2 or y22 > y2:
        response=0

    else:
        im_patch=getpatch(now_im,now_pos,now_sz)
        #im2= mexResize(im_patch,concat([pre_sz(2),pre_sz(1)]))
        z_npca,z_pca= get_subwindow(im2, np.dot(1 / 2, np.array([pre_sz[1],pre_sz[0]])), np.array([pre_sz[1],pre_sz[0]]),non_compressed_features,compressed_features,w2c)
        data_mean= mean(z_pca,1)
        data_matrix= z_pca*data_mean

        cov_matrix= np.dot(1 / (math.prod(now_sz) - 1),(np.dot( np.transpose(data_matrix),data_matrix)))
        pca_basis,temp1, temp2= np.linalg.svd(cov_matrix)

        projection_matrix = pca_basis[:, 0:num_compressed_dim]

        cos_window= np.dot(np.hanning(pre_sz[1]), np.hanning(np.transpose(pre_sz[0])))
        zp= feature_projection(z_npca,z_pca,projection_matrix,cos_window)
        x=  feature_projection(xo_npca,xo_pca,projection_matrix,cos_window)
        kf= np.fft.fft2(dense_gauss_kernel(sigma,zp))
        output_sigma= np.dot(sqrt(math.prod(pre_sz)),output_sigma_factor)
    #    rs,cs=ndgrid(((arange(1,pre_sz(2))) - floor(pre_sz(2)) / 2),(arange(1,pre_sz(1))) - floor(pre_sz(1) / 2),nargout=2)
        y= np.exp(dot(- 0.5 / output_sigma ** 2,(rs ** 2 + cs ** 2)))
        yf= np.fft.fft2(y)
        alphaf_num= np.multiply(yf,kf)
        alphaf_den= np.multiply(kf,(kf + lambda_))
        kf= np.fft.fft2(dense_gauss_kernel(sigma,x,zp))
        res= np.real(np.fft.ifft2(np.multiply(alphaf_num,kf) / alphaf_den))
        response= res[math.floor(pre_sz[1] / 2), math.floor(pre_sz[0] / 2)]

        if np.dot(response,1.2) < max(np.ravel(res)):
            response= max(np.ravel(res))

        overlap= com_overlap(now_pos,pre_pos,now_sz,pre_sz)

        response=(response + np.dot(0.5,overlap)) / 1.5


    return response

if __name__ == '__main__':
    patchmatch()
