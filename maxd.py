# Generated with SMOP  0.41
from libsmop import *
# maxd.m

    
@function
def maxd(detections=None,*args,**kwargs):
    varargin = maxd.varargin
    nargin = maxd.nargin

    ## return the maximum of detections per frame
    N_frame=length(detections)
# maxd.m:3
    pnum=0
# maxd.m:4
    for i in arange(1,N_frame).reshape(-1):
        l=detections[i]
# maxd.m:6
        pnum=max(pnum,size(l,1))
# maxd.m:7
    
    return pnum
    
if __name__ == '__main__':
    pass
    