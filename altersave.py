# Generated with SMOP  0.41
from libsmop import *
# altersave.m

    
@function
def altersave(now_im=None,frame=None,pre_im=None,pre_pos=None,pre_sz=None,t1=None,label=None,virflag=None,non_compressed_features=None,compressed_features=None,w2c=None,*args,**kwargs):
    varargin = altersave.varargin
    nargin = altersave.nargin

    alternative=zeros(1,8)
# altersave.m:2
    alternative[1,arange(1,2)]=pre_pos
# altersave.m:3
    alternative[1,arange(3,4)]=pre_sz
# altersave.m:4
    alternative[1,5]=frame - 1
# altersave.m:5
    alternative[1,6]=t1
# altersave.m:6
    alternative[1,7]=label
# altersave.m:7
    alternative[1,8]=virflag + 1
# altersave.m:8
    return alternative
    
if __name__ == '__main__':
    pass
    