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
