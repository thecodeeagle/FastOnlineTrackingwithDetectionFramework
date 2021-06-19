import numpy as np
def com_overlap(pos1=5,pos2=5,sz1=5,sz2=5,*args,**kwargs):

    h11=pos1 - sz1/2
    h12=pos2 + sz1/2
    h21=pos2 - sz2/2
    h22=pos2 + sz2/2
    h1= [2,h11, h22]
    h2= [2,h21, h22]
#    H=compute_overlap(h1,h2)

#    return H

if __name__ == '__main__':
     com_overlap()
