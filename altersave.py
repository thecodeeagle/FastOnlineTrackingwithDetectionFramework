
import numpy as np
def altersave(now_im=None,frame=2,pre_im=None,pre_pos=None,pre_sz=None,t1=None,label=None,virflag=4,non_compressed_features=None,compressed_features=None,w2c=None,*args,**kwargs):

    alternative= np.zeros(8);
    alternative[0:2]=pre_pos
    alternative[2:4]=pre_sz
    alternative[4]=frame - 1
    alternative[5]=t1
    alternative[6]=label
    alternative[7]=virflag + 1
    return alternative

if __name__ == '__main__':
    altersave()
