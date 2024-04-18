import sys
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
def typeAsolve(a,c,d,r0,r1,r2,r3,r4,r5,r6,flag):
    regval={"000":str(r0),
            '001':str(r1),
            '010':str(r2),
            '011':str(r3),
            '100':str(r4),
            '101':str(r5),
            '110':str(r6),
            '111':str(flag)}
    
    valueset=[r0,r1,r2,r3,r4,r5,r6,flag]
    if a=="add":
        result=int(regval[c])+int(regval[d])
    if a=="sub":
        result=int(regval[c])-int(regval[d])
    if a=="mul":
        result=int(regval[c])*int(regval[d])
    if a=="xor":
        result=int(regval[c])^int(regval[d])
    if a=='or':
        result=int(regval[c])| int(regval[d])
    if a=='and':
        result=int(regval[c])&int(regval[d])


    return result

def typeBsolve(funcname,register,value,r0,r1,r2,r3,r4,r5,r6,flag):
    retval=0
    if funcname=="mov":
        retval=bintodec(value)
    elif funcname=='rs':
        if register=='000':
            retval=int(ro)>>bintodec(value)
        if register=='001':
            retval=int(r1)>>bintodec(value)
        if register=='010':
            retval=int(r2)>>bintodec(value)
        if register=='011':
            retval=int(r3)>>bintodec(value)
        if register=='100':
            retval=int(r4)>>bintodec(value)
        if register=='110':
            retval=int(r5)>>bintodec(value)
        if register=='111':
            retval=int(r6)>>bintodec(value)
    elif funcname=='ls':
        if register=='000':
            retval=int(ro)<<bintodec(value)
        if register=='001':
            retval=int(r1)<<bintodec(value)
        if register=='010':
            retval=int(r2)<<bintodec(value)
        if register=='011':
            retval=int(r3)<<bintodec(value)
        if register=='100':
            retval=int(r4)<<bintodec(value)
        if register=='110':
            retval=int(r5)<<bintodec(value)
        if register=='111':
            retval=int(r6)<<bintodec(value)

    return retval
def typeCsolve(a,b,c,r0,r1,r2,r3,r4,r5,r6,flag):
    if a=='mov':
        if b=='000':
            result=r0
        elif b=='010':
            result=r2
        elif b=='011':
            result=r3
        elif b=='100':
            result=r4
        elif b=='101':
            result=r5
        elif b=='110':
            result=r6
        reslist=[result]
    regval={"000":str(r0),
            '001':str(r1),
            '010':str(r2),
            '011':str(r3),
            '100':str(r4),
            '101':str(r5),
            '110':str(r6)}
    if a=='div':
        quo=int(regval[b])//int(regval[c])
        rem=int(regval[b])%int(regval[c])
        reslist=[quo,rem]
    if a=='not':
        value=int(regval[b])
        if val==1:
            result=0
        else:
            result=abs(~int(regval[b]))
        reslist=[result]
    if a=='cmp':
        if int(regval[b])<int(regval[c]):
            result=4
        elif int(regval[b])==int(regval[c]):
            result=1
        elif int(regval[b])>int(regval[c]):
            result=2
        reslist=[result]
    return reslist
        
            
def taking_input():
    
    filecode=[]
    filecode=sys.stdin.readlines()
    filecode=[x.strip() for x in filecode]
    
    return filecode
def dataset():
    datalist=[]
    A=['add','sub','mul','xor','or','and']
    typeAdict={'10000':'add',
               '10001':'sub',
               '10110':'mul',
               '11010':'xor',
               '11011':'or',
               '11100':'and',}
    B=['mov','ls','rs']
    typeBdict={'10010':'mov',
           '11001':'ls',
           '11000':'rs'}
    C=['mov','div','not','cmp']
    typeCdict={'10011':'mov',
           '10111':'div',
           '11101':'not',
           '11110':'cmp'}
    D=['ld','st']
    typeDdict={'10100':'ld',
           '10101':'st'}
    E=['jmp','jlt','jgt','je']
    typeEdict={'11111':'jmp',
               '01100':'jlt',
               '01101':'jgt',
               '01111':'je'}
    maindict={'10000':'add',
               '10001':'sub',
               '10110':'mul',
               '11010':'xor',
               '11011':'or',
               '11100':'and',
               '10010':'mov',
               '11001':'ls',
               '11000':'rs',
               '10011':'mov',
               '10111':'div',
               '11101':'not',
               '11110':'cmp',
               '10100':'ld',
               '10101':'st',
               '11111':'jmp',
               '01100':'jlt',
               '01101':'jgt',
               '01111':'je',
               '01010':'hlt'}
    datalist=[A,typeAdict,B,typeBdict,C,typeCdict,D,typeDdict,E,typeEdict,maindict]
    return datalist
    

def main():
    
    valuelist=dataset()
    typeA=valuelist[0]
    typeAdict=valuelist[1]
    typeB=valuelist[2]
    typeBdict=valuelist[3]
    typeC=valuelist[4]
    typeCdict=valuelist[5]
    typeD=valuelist[6]
    typeDdict=valuelist[7]
    typeE=valuelist[8]
    typeEdict=valuelist[9]
    opcodedict=valuelist[10]
    
    reglist=[]#it will store the state of registers after evey instruction count
    pogocounter=0#programme counter
    
    r0=0
    r1=0
    r2=0
    r3=0
    r4=0#INITIALLY ALL REGISTERS ARE SET TO ZERO
    r5=0
    r6=0
    flag=0
    instruction_set=list(taking_input())
    instlen=len(instruction_set)#length of the instructions
    j=0
    remlen=256-instlen
    dumplist=[]
    for i in range(remlen):
        dumplist.append('0'*16)
    temp=0    
    while j<=instlen:
        i=instruction_set[j]
        opcodeint=i[:5]
        strval=str(opcodedict[opcodeint])
        if strval in typeA:
            resval=typeAsolve(strval,i[7:10],i[10:13],r0,r1,r2,r3,r4,r5,r6,flag)#ro,r1,r2,r3,r4,r5,r6,flag represents the current value of the registers
            if i[13:]=='000':  #i[7:10]represent the register in which addition in going on   # with the instructions soon it will get updated
                r0=int(resval)
            elif i[13:]=='001':
                r1=int(resval)
            elif i[13:]=='010':
                r2=int(resval)
            elif i[13:]=='011':
                r3=int(resval)
            elif i[13:]=='100':
                r4=int(resval)
            elif i[13:]=='101':
                r5=int(resval)
            elif i[13:]=='110':
                r6=int(resval)
            pogocounter=j
            reglist.append([pogocounter,r0,r1,r2,r3,r4,r5,r6,flag])
        if strval in typeB:
            if i[:5] in ['10010','11001','11000']:
                resval=typeBsolve(strval,i[5:8],i[8:],r0,r1,r2,r3,r4,r5,r6,flag)
                if i[5:8]=='000':  #i[7:10]represent the register in which addition in going on   # with the instructions soon it will get updated
                    r0=int(resval)
                elif i[5:8]=='001':
                    r1=int(resval)
                elif i[5:8]=='010':
                    r2=int(resval)
                elif i[5:8]=='011':
                    r3=int(resval)
                elif i[5:8]=='100':
                    r4=int(resval)
                elif i[5:8]=='101':
                    r5=int(resval)
                elif i[5:8]=='110':
                    r6=int(resval)
                pogocounter=j
                reglist.append([pogocounter,r0,r1,r2,r3,r4,r5,r6,flag])
        if strval in typeC:
            if i[:5] in ['10011','10111','11101','11110']:
                resval=typeCsolve(strval,i[10:13],i[13:],r0,r1,r2,r3,r4,r5,r6,flag)
                if strval=='mov':
                    if i[13:]=='000': 
                        r0=int(resval[0])
                    elif i[13:]=='001':
                        r1=int(resval[0])
                    elif i[13:]=='010':
                        r2=int(resval[0])
                    elif i[13:]=='011':
                        r3=int(resval[0])
                    elif i[13:]=='100':
                        r4=int(resval[0])
                    elif i[13:]=='101':
                        r5=int(resval[0])
                    elif i[13:]=='110':
                        r6=int(resval[0])
                elif strval=='div':
                    ro=resval[0]
                    r1=resval[1]
                elif strval=='not':
                    if i[13:]=='000': 
                        r0=int(resval[0])
                    elif i[13:]=='001':
                        r1=int(resval[0])
                    elif i[13:]=='010':
                        r2=int(resval[0])
                    elif i[13:]=='011':
                        r3=int(resval[0])
                    elif i[13:]=='100':
                        r4=int(resval[0])
                    elif i[13:]=='101':
                        r5=int(resval[0])
                    elif i[13:]=='110':
                        r6=int(resval[0])
                elif strval=='cmp':
                    flag=resval[0]
                pogocounter=j
                reglist.append([pogocounter,r0,r1,r2,r3,r4,r5,r6,flag])
        if strval in typeD:
            pogocounter=j
            reglist.append([pogocounter,r0,r1,r2,r3,r4,r5,r6,flag])
            if strval=='ld':
                remindex=bintodec(str(i[8:]))-instlen
                if i[5:8]=='000':
                    r0=int(dumplist[remindex])
                elif i[5:8]=='001':
                    r1=int(dumplist[remindex])
                elif i[5:8]=='010':
                    r2=int(dumplist[remindex])
                elif i[5:8]=='011':
                    r3=int(dumplist[remindex])
                elif i[5:8]=='100':
                    r4=int(dumplist[remindex])
                elif i[5:8]=='101':
                    r5=int(dumplist[remindex])
                elif i[5:8]=='110':
                    r6=int(dumplist[remindex])
            if strval=='st':
                remindex=bintodec(str(i[8:]))-instlen
                if i[5:8]=='000':
                    dumplist[remindex]=r0
                if i[5:8]=='001':
                    dumplist[remindex]=r1
                if i[5:8]=='010':
                    dumplist[remindex]=r2
                if i[5:8]=='011':
                    dumplist[remindex]=r3
                if i[5:8]=='100':
                    dumplist[remindex]=r4
                if i[5:8]=='101':
                    dumplist[remindex]=r5
                if i[5:8]=='110':
                    dumplist[remindex]=r6
        if strval in typeE:
            pogocounter=j
            if strval=='jmp':
                j=bintodec(str(i[8:]))-1
            elif strval=='jlt':
                if flag==4:
                    j=bintodec(str(i[8:]))-1
            elif strval=='jgt':
                if flag==2:
                    j=bintodec(str(i[8:]))-1
            elif strval=='je':
                if flag=='1':
                    j=bintodec(str(i[8:]))-1
            flag=0
            reglist.append([pogocounter,r0,r1,r2,r3,r4,r5,r6,flag])

            
            
                               
            
                    
        if strval=='hlt':
            pogocounter=j
            reglist.append([pogocounter,r0,r1,r2,r3,r4,r5,r6,flag])
            break
        j+=1
        temp+=1
    for i in range(len(reglist)):
        for j in range(len(reglist[i])):
            if j==0:
                temp=reglist[i][j]
                reglist[i][j]=biteightconverter(temp)
            else:
                temp=reglist[i][j]
                reglist[i][j]=bitsixteenconverter(temp)
    biglist=[]
    
    for i in reglist:
        mainstr=""
        for j in i:
            mainstr+=j+" "
        biglist.append(mainstr)
            
        
        
        




    for i in instruction_set:
        biglist.append(i)
        
    for i in dumplist:
        if i!='0000000000000000':
            i=bitsixteenconverter(i)
        else:
            i=i
        biglist.append(i)
    for i in biglist:
        sys.stdout.write(i)
        sys.stdout.write('\n')

    
     
                    
                
                
main()            
                
                
                    
            
            
    
            
            
            
            
        
    
