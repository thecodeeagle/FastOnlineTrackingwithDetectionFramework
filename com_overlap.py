# Generated with SMOP  0.41
from libsmop import *
# com_overlap.m

    
@function
def com_overlap(pos1=None,pos2=None,sz1=None,sz2=None,*args,**kwargs):
    varargin = com_overlap.varargin
    nargin = com_overlap.nargin

    h11=pos1 - dot(1 / 2,sz1)
# com_overlap.m:2
    h12=pos2 + dot(1 / 2,sz1)
# com_overlap.m:3
    h21=pos2 - dot(1 / 2,sz2)
# com_overlap.m:4
    h22=pos2 + dot(1 / 2,sz2)
# com_overlap.m:5
    h1=cat(2,h11,h12)
# com_overlap.m:6
    h2=cat(2,h21,h22)
# com_overlap.m:7
    H=compute_overlap(h1,h2)
# com_overlap.m:8
    return H
    
if __name__ == '__main__':
    pass
    