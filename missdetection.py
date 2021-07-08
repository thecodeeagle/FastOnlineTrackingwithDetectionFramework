import numpy as np
import math

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def missdetection(now_im=[1,2,3,4],pre_im=[1,2,3,4],pre_pos=[1,1,3,4],pre_sz=[1,1,3,4],non_compressed_features=None,compressed_features=None,w2c=None,*args,**kwargs):


    pos= np.array([pre_pos[1],pre_pos[0]])
    target_sz= np.array([pre_sz[1],pre_sz[0]])
    padding=1
    sz= np.dot(target_sz,(1 + padding))

    scale=1
    alapha=2.25

    rs_temp = list(range(1,sz[0]+1))
    cs_temp = list(range(1,sz[1]+1))

    for i in range(len(rs_temp)):
        rs_temp[i] -= math.floor(sz[0]/2)

    for i in range(len(cs_temp)):
        cs_temp[i] -= math.floor(sz[1]/2)

    rs = np.array(rs_temp)
    cs = np.array(cs_temp)
    dist=rs ** 2 + cs ** 2
    conf= np.exp(np.dot(- 0.5 / (alapha),math.sqrt(dist)))
    conf=conf / sum(sum(conf))
    conff=np.fft.fft2(conf)
    hamming_window= np.dot(np.hamming(sz[0]), np.transpose(np.hanning(sz[1])))
    sigma=mean(target_sz)
    window= np.multiply(hamming_window, np.exp(np.dot(- 0.5 / (sigma ** 2),(dist))))
    window=window / sum(sum(window))

    img= np.copy(pre_im)

    if img.shape()[2] > 1:
        im=rgb2gray(img)


    contextprior= get_context(im,pos,sz,window)

    Hstcf=conff / (np.fft.fft2(contextprior) + eps)

    sigma= np.dot(sigma,scale)


    window= np.multiply(hamming_window,np.exp(np.dot(- 0.5 / (sigma ** 2),(dist))))


    window=window / sum(sum(window))


    #load image

    img= np.copy(now_im)

    if img.shape()[2] > 1:
        im=rgb2gray(img)


    contextprior=get_context(im,pos,sz,window)


    response= np.real(np.fft.ifft2(np.multiply(Hstcf,np.fft.fft2(contextprior))))

    # target location is at the maximum response
    if max(np.ravel(response)) > 0.004:
        row,col=  index_2d(response, max(np.ravel(response)))
        newpos= pre_pos - np.array([pre_sz[0],pre_sz[1]]) + np.array([col,row])
        obj= np.array([newpos[0],newpos[1],pre_sz[0],pre_sz[1]])
        det= np.array([newpos[0] - np.dot(1 / 2,pre_sz[0]),newpos[1] - np.dot(1 / 2,pre_sz[1]), newpos[0] + np.dot(1 / 2,pre_sz[1]),newpos[1] + np.dot(1 / 2,pre_sz[1]),0.9])
        ff=1

    else:
        obj=[]
        det=[]
        ff=0

    return det,obj,ff

if __name__ == '__main__':
    missdetection()
