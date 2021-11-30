
def single_tracker(title=None,*args,**kwargs):
    varargin = single_tracker.varargin
    nargin = single_tracker.nargin


    param_set
    ## change this directory to your own MOT2015 data path
    DataDir='Data'

    ## load image
    im_dir=fullfile(DataDir,title,'img1')
    images=dir(fullfile(im_dir,'*.jpg'))
    framenum=numel(images)
    ## load detection

    det_dir=fullfile(DataDir,title,'det')
    det_array=load(fullfile(det_dir,'det.txt'))
    detections=ndet_tran(det_array,framenum)
    pnum=maxd(detections)
    ## Object matching
    objects=info_get(detections)
    labels,flag,scores,resulttmp,results,virscore,virobjects,virresults=blockmatch(detections,objects,framenum,im_dir,images,params,pnum,nargout=8)
    scores_resize_myversion(objects)
    trackRes=cr_tr(objects,framenum,flag)
    ## visualization
    framevisual(objects,framenum,im_dir,images)
    ## save results
    outDir='./out_res/test/'
    if logical_not(exist(outDir,'file')):
        mkdir(outDir)

    saveas_txt(outDir,title,trackRes)
    return

if __name__ == '__main__':
    pass
