import numpy as np

def dense_gauss_kernel(sigma=20.3,x=[[[2,3], [3,2]]],y=[[[2,3], [3,2]]],*args,**kwargs):

    # k = dense_gauss_kernel(sigma, x, y)
    # Computes the kernel output for multi-dimensional feature maps x and y using a Gaussian kernel with standard deviation sigma.

    xf= np.fft.fft2(x)


    xx= np.dot(np.transpose(np.ravel(x)),np.ravel(x))

    if len(kwargs) >= 3:
        yf= np.fft2(y)
        yy= np.dot(np.transpose(np.ravel(y)), np.ravel(y))
    else:
        yf= xf.copy()
        yy= xx.copy()

    xyf= np.multiply(xf, np.conj(yf))
    xy=  np.real(np.fft.ifft2(np.sum(xyf,2)))  #temporary change in axes to suit the example
    #k=2

    k= np.exp(np.dot(- 1 / sigma*sigma,max(0,(xx.all() + yy.all() - np.dot(2,xy.all()))) / len(x))) #check if sigma*sigma is fine substitute for sigma squared

    #return k

if __name__ == '__main__':
    dense_gauss_kernel()
