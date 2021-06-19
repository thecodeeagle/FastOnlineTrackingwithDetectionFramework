
def get_context(im=None,pos=None,sz=None,window=None,*args,**kwargs):


    #get and process the context region
    xs=floor(pos(2) + (arange(1,sz(2))) - (sz(2) / 2))

    ys=floor(pos(1) + (arange(1,sz(1))) - (sz(1) / 2))

    #the borders
    xs[xs < 1]=1
    ys[ys < 1]=1

    xs[xs > size(im,2)]=size(im,2)
    ys[ys > size(im,1)]=size(im,1)


    out=im(ys,xs,arange())
    out=double(out)
    out=(out - mean(ravel(out)))

    out=multiply(window,out)


    return out

if __name__ == '__main__':
    get_context()
