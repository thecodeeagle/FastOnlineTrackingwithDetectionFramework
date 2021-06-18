# Generated with SMOP  0.41
from libsmop import *
# dense_gauss_kernel.m

    
@function
def dense_gauss_kernel(sigma=None,x=None,y=None,*args,**kwargs):
    varargin = dense_gauss_kernel.varargin
    nargin = dense_gauss_kernel.nargin

    # k = dense_gauss_kernel(sigma, x, y)
    
    # Computes the kernel output for multi-dimensional feature maps x and y
# using a Gaussian kernel with standard deviation sigma.
    
    xf=fft2(x)
# dense_gauss_kernel.m:8
    
    xx=dot(ravel(x).T,ravel(x))
# dense_gauss_kernel.m:9
    
    if nargin >= 3:
        yf=fft2(y)
# dense_gauss_kernel.m:12
        yy=dot(ravel(y).T,ravel(y))
# dense_gauss_kernel.m:13
    else:
        #auto-correlation of x, avoid repeating a few operations
        yf=copy(xf)
# dense_gauss_kernel.m:16
        yy=copy(xx)
# dense_gauss_kernel.m:17
    
    #cross-correlation term in Fourier domain
    xyf=multiply(xf,conj(yf))
# dense_gauss_kernel.m:21
    xy=real(ifft2(sum(xyf,3)))
# dense_gauss_kernel.m:22
    
    #calculate gaussian response for all positions
    k=exp(dot(- 1 / sigma ** 2,max(0,(xx + yy - dot(2,xy)) / numel(x))))
# dense_gauss_kernel.m:25
    return k
    
if __name__ == '__main__':
    pass
    