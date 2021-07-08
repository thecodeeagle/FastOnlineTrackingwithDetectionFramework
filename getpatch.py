import numpy as np
import math
def getpatch(now_im=[[[1,2,3], [1,2,3]]],now_pos=[1,2,3],now_sz=[7,2,3,4],*args,**kwargs):


    xs = list(range(1,now_sz[1]+1))
    ys = list(range(1, now_sz[1]+1))

    for i in range(len(xs)):
        xs[i] += math.floor(now_pos[1] - (now_sz[1] / 2))

    for i in range(len(ys)):
        ys[i] += math.floor(now_pos[0] - (now_sz[0] / 2))

    #the borders
    for i in range(len(xs)):
        if(xs[i]<1):
            xs[i] = 1

    for i in range(len(ys)):
        if(ys[i]<1):
            ys[i] = 1

    for i in range(len(xs)):
        if(xs[i]>np.shape(now_im)[1]):
            xs[i]= np.shape(now_im)[1]

    for i in range(len(ys)):
        if(ys[i]> np.shape(now_im)[0]):
            ys[i]= np.shape(now_im)[0]

    im_patch= now_im[:len(ys)][:len(xs)][:]

    return im_patch

if __name__ == '__main__':
    getpatch()
