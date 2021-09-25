# Generated with SMOP  0.41
from libsmop import *
# framevisual.m

    
@function
def framevisual(objects=None,framenum=None,im_directory=None,images=None,*args,**kwargs):
    varargin = framevisual.varargin
    nargin = framevisual.nargin

    global scores
    for frame in arange(1,min(framenum,numel(objects))).reshape(-1):
        info=objects[frame]
# framevisual.m:4
        m,n=size(info,nargout=2)
# framevisual.m:5
        now_im=imread(fullfile(im_directory,images(frame,1).name))
# framevisual.m:6
        now_pos=zeros(m,2)
# framevisual.m:7
        now_sz=zeros(m,2)
# framevisual.m:8
        for i in arange(1,m).reshape(-1):
            now_pos[i,arange()]=floor(concat([info(i,1),info(i,2)]))
# framevisual.m:10
            now_sz[i,arange()]=floor(concat([info(i,3),info(i,4)]))
# framevisual.m:11
        imshow(now_im)
        hold('on')
        for i in arange(1,m).reshape(-1):
            if scores(1,i,frame) != 0:
                rect_position=concat([now_pos(i,arange()) - now_sz(i,arange()) / 2,now_sz(i,arange())])
# framevisual.m:17
                rectangle('Position',rect_position,'EdgeColor','r','LineWidth',1.5)
                fx=now_pos(i,1)
# framevisual.m:19
                fy=now_pos(i,2) - now_sz(i,2) / 2 - 10
# framevisual.m:20
                text_handle=text(fx,fy,int2str(scores(1,i,frame)))
# framevisual.m:21
                set(text_handle,'color',concat([1,0,0]))
        drawnow
        hold('off')
    