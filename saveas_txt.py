# Generated with SMOP  0.41
from libsmop import *
# saveas_txt.m

    
@function
def saveas_txt(outDir=None,sequence_name=None,trackRes=None,*args,**kwargs):
    varargin = saveas_txt.varargin
    nargin = saveas_txt.nargin

    # transfer the result to adapt the devkit in MOT2015 https://motchallenge.net
    
    N,D=size(trackRes,nargout=2)
# saveas_txt.m:4
    T_res=- ones(N,10)
# saveas_txt.m:5
    T_res[arange(),arange(1,6)]=trackRes(arange(),arange(1,6))
# saveas_txt.m:6
    
    # T_res(:,5) = trackRes(:,5)-trackRes(:,3); # width
# T_res(:,6) = trackRes(:,6)-trackRes(:,4); # height
    T_res=sortrows(T_res)
# saveas_txt.m:9
    dlmwrite(concat([outDir,sequence_name,'.txt']),T_res,',')
    return
    
if __name__ == '__main__':
    pass
    