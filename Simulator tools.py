def biteightconverter(n):
    n1=str(dectobinconverter(n))
    numlen=len(n1)
    remlen=8-numlen
    remnum=remlen*'0'+n1
    return remnum

def bitsixteenconverter(n):
    n1=str(dectobinconverter(n))
    numlen=len(n1)
    remlen=16-numlen
    remnum=remlen*'0'+n1
    return remnum
                   
    
def dectobinconverter(n):
    l=[]
    i=0
    t=''
    n=int(n)
    while n!=0:
        binary_value=n%2
        l.append(binary_value)
        n=n//2
        t=l[::-1]
    t1=""
    for i in t:
        t1+=str(i)
    return t1
    
def bintodec(n):
    z=list(str(n))
    z_main=z[::-1]
    z1=0
    binset={'1','0'}
    checkbin=set(n)
    if checkbin=={'0'} or checkbin=={'1'} or checkbin==binset:
        for i in range(len(z_main)):
            z1+=int(z_main[i])*2**i
        return z1
