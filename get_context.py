import numpy as np
import math

def get_context(im=[[[1,2,3], [1,2,3]]],pos=[1,2,3],sz=[7,2,3,4],window=[[[1,2,3], [1,2,3]]],*args,**kwargs):


    #get and process the context region
    xs = list(range(1,sz[1]+1))
    ys = list(range(1,sz[1]+1))

    for i in range(len(xs)):
        xs[i] += math.floor(pos[1] - (sz[1] / 2))

    for i in range(len(ys)):
        ys[i] += math.floor(pos[0] - (sz[0] / 2))

    #the borders
    for i in range(len(xs)):
        if(xs[i]<1):
            xs[i] = 1

    for i in range(len(ys)):
        if(ys[i]<1):
            ys[i] = 1

    for i in range(len(xs)):
        if(xs[i]>np.shape(im)[1]):
            xs[i]= np.shape(im)[1]

    for i in range(len(ys)):
        if(ys[i]> np.shape(im)[0]):
            ys[i]= np.shape(im)[0]

    l1 = len(ys)
    l2 = len(xs)
    out=im[0:l1][0:l2][:]
    out=(out - np.mean(np.ravel(out)))
    out= np.multiply(window,out)


    return out

if __name__ == '__main__':
    get_context()
