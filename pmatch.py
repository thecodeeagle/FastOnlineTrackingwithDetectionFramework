import numpy as np
import math

def pmatch(vir_im=None,virobjects=None,now_im=None,now_pos=None,now_sz=None,non_compressed_features=None,compressed_features=None,w2c=None,*args,**kwargs):

    num_compressed_dim=2
    lambda_=0.01
    output_sigma_factor=1 / 16
    sigma=0.2
    pre_pos=virobjects[0, 0:2]
    pre_sz= virobjects[0, 2:4]

    xo_npca,xo_pca=get_subwindow(vir_im, np,array([pre_pos[1],pre_pos[0]]), np.array([pre_sz[1],pre_sz[0]]),non_compressed_features,compressed_features,w2c)
    im_patch=getpatch(now_im,now_pos,now_sz)
    im2 = im_patch
#    im2= mexResize(im_patch, np.array([pre_sz[1],pre_sz[0]]))
    z_npca,z_pca=get_subwindow(im2, np.dot(1 / 2, np.array([pre_sz[1],pre_sz[0]])), np.array([pre_sz[1],pre_sz[0]]),non_compressed_features,compressed_features,w2c)
    data_mean=mean(z_pca,1)
    data_matrix=bsxfun(minus,z_pca,data_mean)
    cov_matrix= np.dot(1 / (math.prod(now_sz) - 1),(np.dot(np.transpose(data_matrix),data_matrix)))
    pca_basis,pca_variances, temp = np.linalg.svd(cov_matrix,nargout=3)

    projection_matrix= pca_basis[:,0:num_compressed_dim]
    projection_variances= pca_variances[0:num_compressed_dim,0:num_compressed_dim]

    cos_window= np.dot(np.hanning(pre_sz[1]), np.transpose(np.hanning(pre_sz[0])))

    zp=feature_projection(z_npca,z_pca,projection_matrix,cos_window)
    x=feature_projection(xo_npca,xo_pca,projection_matrix,cos_window)
    kf=np.fft.fft2(dense_gauss_kernel(sigma,zp))

    output_sigma= np.dot(sqrt(math.prod(pre_sz)),output_sigma_factor)


    rs_temp = list(range(1,pre_sz[1]+1))
    cs_temp = list(range(1,pre_sz[0]+1))

    for i in range(len(rs_temp)):
        rs_temp[i] -= math.floor(sz[1]/2)

    for i in range(len(cs_temp)):
        cs_temp[i] -= math.floor(sz[0]/2)

    rs,cs= np.mgrid(rs_temp, cs_temp)
    y= np.exp(np.dot(- 0.5 / output_sigma ** 2,(rs ** 2 + cs ** 2)))

    yf= np.fft.fft2(y)
    alphaf_num= np.multiply(yf,kf)
    alphaf_den= np.multiply(kf,(kf + lambda_))
    kf= np.fft.fft2(dense_gauss_kernel(sigma,x,zp))
    res= np.real(np.fft.ifft2(np.multiply(alphaf_num,kf) / alphaf_den))
    virscore= res[math.floor(pre_sz[1] / 2), math.floor(pre_sz[0] / 2)]
    return virscore

if __name__ == '__main__':
    pass
