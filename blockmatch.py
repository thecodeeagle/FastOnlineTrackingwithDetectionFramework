
import numpy as np
import math


def blockmatch(detections=None,objects=None,framenum=None,im_directory=None,images=None,params=None,pnum=5,*args,**kwargs):

    object_pnum= np.dot(math.ceil((pnum + 6) / 5),5)
    scores= np.zeros((object_pnum,object_pnum,np.size(images)))
    results= np.zeros((1,object_pnum,np.size(images)))
    resulttmp= np.zeros((1,object_pnum,np.size(images)))
    virobjects= np.array([])
    virresults= np.array(framenum)
    virscore= np.array(framenum)
    labels= np.zeros(1,object_pnum,framenum)
    flag=1
    virflag=0
    non_compressed_features= np.array(['gray'])
    compressed_features= np.array(['cn'])
    #temp= load('w2crs.mat')
    w2c=w2crs
    for frame in arange(1,min(framenum,np.size(objects))).reshape(-1):
        ## visualize process
        clc
        fprintf('Processing %.1f%%\n',dot(frame,100) / min(framenum,np.size(objects)))
        infor=objects[frame]

        m=size(infor,1)

        if frame == 1:
            pre_m=copy(m)

            for i in arange(1,m).reshape(-1):
                scores[i,i,frame]=1

                results[1,i,frame]=i

                labels[1,i,frame]=flag

                flag=flag + 1

        else:
            # save previous information
            pre_im=copy(now_im)

            pre_pos=copy(now_pos)

            pre_sz=copy(now_sz)

        ## add virtual objects
        vm=size(virobjects,1)

        if vm:
            fr=frame - virobjects(arange(),5)

            outd=find(fr > 5)

            virobjects[outd,arange()]=[]

        vm=size(virobjects,1)

        now_im=imread(fullfile(im_directory,images(frame,1).name))

        now_pos=zeros(m,2)

        now_sz=zeros(m,2)

        for i in arange(1,m).reshape(-1):
            now_pos[i,arange()]=floor(concat([infor(i,1),infor(i,2)]))

            now_sz[i,arange()]=floor(concat([infor(i,3),infor(i,4)]))

        ## model transformation and matching
        if frame > 1:
            for t1 in arange(1,pre_m).reshape(-1):
                for t2 in arange(1,m).reshape(-1):
                    scores[t1,t2,frame]=patchmatch(pre_im,pre_pos(t1,arange()),pre_sz(t1,arange()),now_im,now_pos(t2,arange()),now_sz(t2,arange()),non_compressed_features,compressed_features,w2c)

                resulttmp(1,t1,frame)
                tm=max(scores(t1,arange(),frame),nargout=2)

                if resulttmp(1,t1,frame) > params.eta1:
                    if logical_not(results(1,tm,frame)):
                        results[1,tm,frame]=t1

                        labels[1,tm,frame]=labels(1,t1,frame - 1)

                    else:
                        tn=results(1,tm,frame)

                        tmp=scores(tn,tm,frame)

                        if resulttmp(1,t1,frame) > tmp:
                            results[1,tm,frame]=t1

                            labels[1,tm,frame]=labels(1,t1,frame - 1)

                ## match virtual objects
                virscore[frame]=zeros(vm,m)

                vtms=zeros(1,vm)

                vtmn=1

                if vm != 0:
                    for t2 in arange(1,m).reshape(-1):
                        if logical_not(results(1,t2,frame)):
                            for ii in arange(1,vm).reshape(-1):
                                frameno=virobjects(ii,5)

                                vir_im=imread(fullfile(im_directory,images(frameno,1).name))

                                virscore[frame][ii,t2]=pmatch(vir_im,virobjects(ii,arange()),now_im,now_pos(t2,arange()),now_sz(t2,arange()),non_compressed_features,compressed_features,w2c)

                        vrt,vtm=max(virscore[frame](arange(),t2),nargout=2)

                        if vrt > params.zeta:
                            if logical_not(find(vtms == vtm)):
                                results[1,t2,frame]=min(max(results(1,arange(),frame) + 1,object_pnum))

                                labels[1,t2,frame]=virobjects(vtm,7)

                                vtms[vtmn]=vtm

                                vtmn=vtmn + 1

                            else:
                                v11=find(labels(1,arange(),frame) == virobjects(vtm,7))

                                if virscore[frame](vtm,t2) > virscore[frame](vtm,v11):
                                    results[1,t2,frame]=min(max(results(1,arange(),frame) + 1,object_pnum))

                                    labels[1,t2,frame]=virobjects(vtm,7)

                                    results[1,v11,frame]=0

                                    labels[1,v11,frame]=0

            ## build virtual objects
            t1n=copy(pre_m)

            pre_m=copy(m)

            for t1 in arange(1,t1n).reshape(-1):
                if max(scores(t1,arange(),frame)) < params.eta2:
                    if labels(1,t1,frame - 1):
                        det,obj,ff=missdetection(now_im,pre_im,pre_pos(t1,arange()),pre_sz(t1,arange()),non_compressed_features,compressed_features,w2c,nargout=3)

                        if ff:
                            objects[frame]=cat(1,objects[frame],obj)

                            detections[frame]=cat(1,detections[frame],det)

                            infor=cat(1,infor,obj)

                            now_pos=cat(1,now_pos,concat([obj(1),obj(2)]))

                            now_sz=cat(1,now_sz,concat([obj(3),obj(4)]))

                            if m >= object_pnum:
                                fprintf('wrong')
                            else:
                                scores[t1,m + 1,frame]=det(5)

                                results[1,m + 1,frame]=t1

                                labels[1,m + 1,frame]=labels(1,t1,frame - 1)

                                m=m + 1

                        else:
                            if labels(1,t1,frame - 1):
                                if isempty(virobjects):
                                    alternative=altersave(now_im,frame,pre_im,pre_pos(t1,arange()),pre_sz(t1,arange()),t1,labels(1,t1,frame - 1),virflag,non_compressed_features,compressed_features,w2c)

                                    virobjects=copy(alternative)

                                    virflag=virflag + 1

                                else:
                                    alternative=altersave(now_im,frame,pre_im,pre_pos(t1,arange()),pre_sz(t1,arange()),t1,labels(1,t1,frame - 1),virflag,non_compressed_features,compressed_features,w2c)

                                    virobjects=cat(1,virobjects,alternative)

                                    virflag=virflag + 1

            ## clear overlap region
            m1=size(objects[frame],1)

            overlap=zeros(m1,m1)

            for tt1 in arange(1,m1).reshape(-1):
                for tt2 in arange(1,m1).reshape(-1):
                    overlap[tt1,tt2]=com_overlap(objects[frame](tt1,arange(1,2)),objects[frame](tt2,arange(1,2)),objects[frame](tt1,arange(3,4)),objects[frame](tt2,arange(3,4)))

            for iii in arange(1,m).reshape(-1):
                if logical_not(results(1,iii,frame)):
                    if max(scores(arange(),iii,frame)) < params.eta2 and detections[frame](iii,5) > params.sigma:
                        labels[1,iii,frame]=flag

                        flag=flag + 1


    flag=flag - 1

    return detections,objects,labels,flag,scores,resulttmp,results,virscore,virobjects,virresults

if __name__ == '__main__':
    blockmatch();
