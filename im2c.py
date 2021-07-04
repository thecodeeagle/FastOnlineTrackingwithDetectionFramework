import numpy as np
import math

def im2c(im=None,w2c=None,color=None,*args,**kwargs):


    # input im should be DOUBLE !
    # color=0 is color names out
    # color=-1 is colored image with color names out
    # color=1-11 is prob of colorname=color out;
    # color=-1 return probabilities
    # order of color names: black ,   blue   , brown       , grey       , green   , orange   , pink     , purple  , red     , white    , yellow
    color_values= np.array([np.array([0,0,0]), np.array([0,0,1]), np.array([0.5,0.4,0.25]),np.array([0.5,0.5,0.5]),np.array([0,1,0]), np.array([1,0.8,0]), np.array([1,0.5,1]), np.array([1,0,1]), np.array([1,0,0]), np.array([1,1,1]), np.array([1,1,0])])

    if (len(kwargs) < 3):
        color=0


    RR=im[:,:,0]
    GG=im[:,:,1]
    BB=im[:,:,2]

    index_im= 1 + math.floor(np.ravel(RR) / 8) + np.dot(32, math.floor(np.ravel(GG) / 8)) + np.dot(np.dot(32,32),math.floor(np.ravel(BB) / 8))

    if (color == 0):
        max1,w2cM=max(w2c,[],2,nargout=2)
        out=  np.reshape(w2cM(np.ravel(index_im)), im.size()[0],im.size()[1])


    if (color > 0 and color < 12):
        w2cM=w2c[:,color]

        out= np.reshape(w2cM(np.ravel(index_im)),im.size()[0],im.size()[1])


    if (color == - 1):
        out= np.copy(im)

        max1,w2cM= max(w2c,[],2)

        out2= np.reshape(w2cM(np.ravel(index_im)),im.size()[0],im.size()[1])

        for jj in range(1, im.size()[0]+1):
            for ii in range(1, im.size()[1]+1):
                #pass
                out[jj,ii,:]= np.dot(np.transpose(color_values[out2[jj,ii]]),255)
#

    if (color == - 2):
        out= np.reshape(w2c[index_im,:],im.size()[0], im.size()[1],w2c.size()[1])
