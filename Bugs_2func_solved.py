def typed(a,b,memx,linenum):
    dataset=ISA()
    funclist=dataset[0]
    funcopcode=dataset[1]
    reglist=dataset[2]
    regcode=dataset[3]
    resstring=""
    if a  not in funclist:
        resstring=" ERROR:INVALID FUNCTION IMPLEMENTED IN LINE "+str(linenum)
    else:
        resstring+=str(funcopcode[a])
        if b in reglist:
            resstring+=str(regcode[b])
            resstring+=bitmemconverter(memx)
        else:
            resstring=" ERROR:INVALID REGISTER IMPLEMENTED IN LINE "+str(linenum)
    

    return resstring

def typee(a,memx,linenum):
    dataset=ISA()
    funclist=dataset[0]
    funcopcode=dataset[1]
    reglist=dataset[2]
    regcode=dataset[3]
    resstring=""
    if a  not in funclist:
        resstring=" ERROR:INVALID FUNCTION IMPLEMENTED IN LINE "+str(linenum)
    else:
        resstring+=str(funcopcode[a])
        resstring+="000"
        resstring+=bitmemconverter(memx)

    return resstring
