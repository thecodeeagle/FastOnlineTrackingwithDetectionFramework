# Generated with SMOP  0.41
from libsmop import *
# .\single_tracker.m

    
@function
def single_tracker(title=None,*args,**kwargs):
    varargin = single_tracker.varargin
    nargin = single_tracker.nargin

    ## param settings
    param_set
    ## change this directory to your own MOT2015 data path
    DataDir='Data'
# .\single_tracker.m:5
    ## load image
    im_dir=fullfile(DataDir,title,'img1')
# .\single_tracker.m:7
    images=dir(fullfile(im_dir,'*.jpg'))
# .\single_tracker.m:8
    framenum=numel(images)
# .\single_tracker.m:9
    ## load detection
    
    det_dir=fullfile(DataDir,title,'det')
# .\single_tracker.m:12
    det_array=load(fullfile(det_dir,'det.txt'))
# .\single_tracker.m:13
    detections=ndet_tran(det_array,framenum)
# .\single_tracker.m:14
    pnum=maxd(detections)
# .\single_tracker.m:15
    ## Object matching
    objects=info_get(detections)
# .\single_tracker.m:17
    labels,flag,scores,resulttmp,results,virscore,virobjects,virresults=blockmatch(detections,objects,framenum,im_dir,images,params,pnum,nargout=8)
# .\single_tracker.m:18
    scores_resize_myversion(objects)
    trackRes=cr_tr(objects,framenum,flag)
# .\single_tracker.m:20
    ## visualization
    framevisual(objects,framenum,im_dir,images)
    ## save results
    outDir='./out_res/test/'
# .\single_tracker.m:24
    if logical_not(exist(outDir,'file')):
        mkdir(outDir)
    
    saveas_txt(outDir,title,trackRes)
    return
    
if __name__ == '__main__':
    pass
    