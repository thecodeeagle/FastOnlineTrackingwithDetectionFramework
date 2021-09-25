# Generated with SMOP  0.41
from libsmop import *
# .\ndet_tran.m

    
@function
def ndet_tran(detections=None,num=None,*args,**kwargs):
    varargin = ndet_tran.varargin
    nargin = ndet_tran.nargin

    ## divide the detection matrix into cells according to the frame number
    global params
    for flag in arange(1,num).reshape(-1):
        det[flag]=detections(detections(arange(),1) == flag,arange())
# .\ndet_tran.m:5
        det[flag][arange(),arange(1,2)]=[]
# .\ndet_tran.m:6
        # line below
        det[flag][arange(),arange(3,4)]=det[flag](arange(),arange(1,2)) + det[flag](arange(),arange(3,4))
# .\ndet_tran.m:10
        det[flag][arange(),arange(1,4)]=floor(det[flag](arange(),arange(1,4)))
# .\ndet_tran.m:11
        det[flag][arange(),arange(6,end())]=[]
# .\ndet_tran.m:12
    
    detections=copy(det)
# .\ndet_tran.m:14
    return detections
    
if __name__ == '__main__':
    pass
    