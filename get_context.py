# Generated with SMOP  0.41
from libsmop import *
# .\get_context.m

    
@function
def get_context(im=None,pos=None,sz=None,window=None,*args,**kwargs):
    varargin = get_context.varargin
    nargin = get_context.nargin

    #get and process the context region
    xs=floor(pos(2) + (arange(1,sz(2))) - (sz(2) / 2))
# .\get_context.m:3
    ys=floor(pos(1) + (arange(1,sz(1))) - (sz(1) / 2))
# .\get_context.m:4
    
    #the borders
    xs[xs < 1]=1
# .\get_context.m:8
    ys[ys < 1]=1
# .\get_context.m:9
    xs[xs > size(im,2)]=size(im,2)
# .\get_context.m:10
    ys[ys > size(im,1)]=size(im,1)
# .\get_context.m:11
    
    out=im(ys,xs,arange())
# .\get_context.m:13
    
    out=double(out)
# .\get_context.m:15
    out=(out - mean(ravel(out)))
# .\get_context.m:16
    
    out=multiply(window,out)
# .\get_context.m:17
    
    return out
    
if __name__ == '__main__':
    pass
    