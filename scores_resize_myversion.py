# Generated with SMOP  0.41
from libsmop import *
# scores_resize_myversion.m

    
@function
def scores_resize_myversion(objects=None,*args,**kwargs):
    varargin = scores_resize_myversion.varargin
    nargin = scores_resize_myversion.nargin

    ## change score to the same format as object
    global scores
    for i in arange(1,size(scores,3)).reshape(-1):
        max=size(objects[i],1) + 1
# scores_resize_myversion.m:5
        scores[1,arange(max,size(scores,2)),i]=0
# scores_resize_myversion.m:6
    
    return
    
if __name__ == '__main__':
    pass
    