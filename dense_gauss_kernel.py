def dense_gauss_kernel(sigma=None,x=None,y=None,*args,**kwargs):

    # k = dense_gauss_kernel(sigma, x, y)
    # Computes the kernel output for multi-dimensional feature maps x and y using a Gaussian kernel with standard deviation sigma.

    xf=fft2(x)


    xx=dot(ravel(x).T,ravel(x))

    if nargin >= 3:
        yf=fft2(y)
        yy=dot(ravel(y).T,ravel(y))
    else:
        yf=copy(xf)
        yy=copy(xx)

    xyf=multiply(xf,conj(yf))
    xy=real(ifft2(sum(xyf,3)))

    k=exp(dot(- 1 / sigma ** 2,max(0,(xx + yy - dot(2,xy)) / numel(x))))
    return k

if __name__ == '__main__':
    dense_gauss_kernel()
