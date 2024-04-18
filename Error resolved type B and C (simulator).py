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
