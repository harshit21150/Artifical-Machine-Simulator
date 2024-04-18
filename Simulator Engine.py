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
