def bitmemconverter(memx):
    n=memx
    l=[]
    i=0
    n=int(n)
    while n!=0:
        binary_value=n%2
        l.append(binary_value)
        n=n//2
        t=l[::-1]
    t1=""
    for i in t:
        t1+=str(i)
    memxlen=len(t1)
    zerocount=8-int(memxlen)
    zero="0"*zerocount
    truestring=zero+t1
    return truestring
    
def codelen4(a,b,c,d,linenum):
    dataset=ISA()
    validfunclist=['add',
                   'sub',
                   'mul',
                   'xor',
                   'or',
                   'and']
    funcopcode=dataset[1]
    reglist=dataset[2]
    regcode=dataset[3]
    resstring=""
    if a not in validfunclist:
        resstring="ERROR:"+"IN LINE"+str(linenum)+"IMPLEMENTED FUNCTION NOT COMPATIBLE FOR 3 REGISTERS"
        
    else:
        resstring+=str(funcopcode[a])
        resstring+="00"
        subreglist=[b,c,d]
        check=all(x in reglist for x in subreglist)
        if check==False:
            resstring="ERROR: IN LINE "+str(linenum)+"INVALID REGISTER TYPE"
        else:
            regop1=str(regcode[b])
            
            regop2=str(regcode[c])
            regop3=str(regcode[d])
            regnew=regop1+regop2+regop3
            resstring+=regnew
    return resstring
def codelen1(a,linenum):
    dataset=ISA()
    funclist=dataset[0]
    funcopcode=dataset[1]
    reglist=dataset[2]
    regcode=dataset[3]
    resstring=""
    if a not in funclist:
        resstring="improper function implemented in line "+str(linenum)
    else:
        resstring+=str(funcopcode[a])+str("0"*11)
    return resstring
def typeb(a,b,c,linenum):
    dataset=ISA()
    funclist=dataset[0]
    funcopcode=dataset[1]
    reglist=dataset[2]
    regcode=dataset[3]
    resstring=""
    if a not in funclist:
        resstring="INVALID FUNCTION IMPLEMENTED"
    else:
        if (c[1:]).isdigit():
                if int(c[1:])<255 and int(c[1:])>0:
                    resstring+=str(funcopcode[a])
                    if b not in reglist:
                        resstring="ERROR: INVALID REGISTER USAGE IN LINE" +str(linenum)
                    else:
                        resstring+=str(regcode[b])
                        resstring+=bitmemconverter(int(c[1:]))
                        
                        
                else:
                    resstring="ERROR: immediate value not in specfied range in line " +str(linenum)
        else:
            resstring="ERROR: improper immediate value entered by the user in line "+str(linenum)
    return resstring
def typec(a,b,c,linenum):
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
        resstring+="00000"
        if b in reglist and c in reglist:
            resstring+=str(regcode[b])+str(regcode[c])
        else:
            resstring=" ERROR:INVALID REGISTER IMPLEMENTED IN LINE "+str(linenum)
    return resstring
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
    
    
            

            
        
    

        
    
        
            
    
def ISA():
    #creating storage place for ISA values
    instruct=["add",
             "sub",
             "mov",
             "movreg",
             "ld",
             "st",
             "mul",
             "div",
             "rs",
             "ls",
             "xor",
             "or",
             "and",
             "not",
             "not",
             "cmp",
             "jmp",
             "jli",
             "jgt",
             "je",
             "hlt"]
    instructopcode={"add":'10000',
                    "sub":'10001',
                    "mov":'10010',
                    "movreg":'10011',
                    "ld":'101000',
                    "st":'10101',
                    "mul":'10110',
                    "div":'10111',
                    "rs":'11000',
                    "ls":'11001',
                    "xor":'11010',
                    "or":'11011',
                    "and":'11100',
                    "not":'11101',
                    "cmp":'11110',
                    "jmp":'11111',
                    "jlt":'01100',
                    "jgt":'01101',
                    "je":'01111',
                    "hlt":'01010'}
    reg=["R1",
         "R2",
         "R3",
         "R4",
         "R5",
         "R6",
         "FLAGS",
         "R0"]
    regopcode={"R0":'000',
               "R1":'001',
               "R2":'010',
               "R3":'011',
               "R4":'100',
               "R5":'101',
               "R6":'110',
               "FLAGS":'111'}
    tot_isa=[instruct,instructopcode,reg,regopcode]
    return tot_isa
def taking_input():
    import sys
    filecode=sys.stdin.readlines()
    statements=[]
    for i in filecode:
        if i!="hlt":
            stm1=i[:-1].split(" ")
        else:
            stm1=[i]
        
        statements.append(stm1)
    return (statements)
def conversion():
    import sys
    dataset=ISA()
    funclist=dataset[0]
    funcopcode=dataset[1]
    reglist=dataset[2]
    regcode=dataset[3]
    code=taking_input()
    varpcdict={}
    varlist=[]
    varpc=0
    for i in range(len(code)):
        resstring=""
        if code[i][0]=='var':
            if len(code[i])==2:
                varlist.append(code[i][1])
        else:
            varend=i
            break
    totvar=len(varlist)
    addvar=1
    for i in varlist:
        varpcdict[i]=len(code)-totvar+addvar-1
        addvar+=1
    
    
        
    
#########################################
    labelpc={}
    labelresult={}
    for i in range(0,len(code)):
        spacecheck="".join(code[i])
        if len(spacecheck)==0:
            resstring="ERROR: EMPTY LINE"
        elif ":"==code[i][0][-1]:
            labelpc[code[i][0]]=i
            sublist=code[i]
            sublen=len(code[i])
            if sublen>5:
                labresstring="ERROR: INVALID OPERATION IN GIVEN :"+str(code[i][0])+"in line "+str(i)
                labelresult[code[i][0]]=resstring
            elif sublen==5:
                labelresstring=codelen4(code[i][1],code[i][2],code[i][3],code[i][4],i)
                labelresult[code[i][0]]=labelresstring
            elif sublen==4:
                if code[i][3][0]=="$" and (code[i][3][1:]).isdigit():
                    intval=int(code[i][3][1:])
                    resstring=typeb(code[i][1],code[i][2],code[i][3],i)
                    labelresult[code[i][0]]=resstring
                elif code[i][3] in reglist:
                    resstring=typec(code[i][1],code[i][2],code[i][3],i)
                    labelresult[code[i][0]]=resstring
                else:
                    resstring="ERROR: NOT A VALID REGISTER TYPE/OR A IMMEDIATE VALUE IN LINE" +str(i)+"FOR LABEL"
                    labelresult[code[i][0]]=resstring
    '''print(labelpc)
    print(labelresult)
    print(varlist)
    print(varpc)
    print(varpcdict)'''
    finalresult=[]
################################################
    
    for i in range(len(varlist),len(code)):
        codelen=len(code[i])
        spacecheck2="".join(code[i])
        if len(spacecheck2)==0:
            resstring="ERROR: EMPTY LINE"
        elif codelen==5 and code[i][0][-1]==":":
            resstring=labelresult[code[i][0]]
        elif codelen==5 and code[i][0][-1]!=":":
            resstring="ERROR: INVALID INSTRUCTION IN LINE "+str(i+1)
        elif codelen==4 and code[i][0][-1]==":":
            resstring=labelresult[code[i][0]]
        elif codelen==4 and code[i][0][-1]!=":":
            resstring=codelen4(code[i][0],code[i][1],code[i][2],code[i][3],i+1)
        elif codelen==3 and code[i][0][-1]==":":
            resstring=labelresult[code[i][0]]
        elif codelen==3 and code[i][0][-1]!=":":
            if code[i][2] in varlist:
                resstring=typed(code[i][0],code[i][1],int(varpcdict[code[i][2]]),i+1)
            elif code[i][2] in reglist:
                resstring=typec(code[i][0],code[i][1],code[i][2],i+1)
            elif code[i][2][1:].isdigit():
                resstring=typeb(code[i][0],code[i][1],code[i][2],i+1)
            else:
                resstring="ERROR: INVALID INSTRUCTION IMPLIED IN LINE "+str(i+1)
        elif codelen==2:
            if code[i][0]=="var":
                resstring="ERROR: IMPROPER VARIABLE ALLOACTION IN LINE " +str(i+1)
            elif code[i][0] in ["je","jgt","jmp","jlt"]:
                if code[i][1] in list(labelresult.keys()):
                    resstring=typee(code[i][0],labelresult[code[i][1]],i+1)
                else:
                    resstring="ERROR: UNDEFINED LABEL GIVEN TO THE INSTRUCTION"
            else:
                resstring="ERROR: IMPROPER SYNATX/INSTRUCTION IN LINE "+str(i+1)
        elif codelen==1:
            if code[i][0]=="hlt":
                if i+1==len(code):
                    resstring=codelen1(code[i][0],i+1)
                else:
                    resstring="ERROR: hlt USED IN BETWEEN THE PROGRAMME IN LINE "+str(i+1)
            else:
                resstring="ERROR: INVALID INSTRUCTION IN LINE "+str(i+1)
        finalresult.append(resstring)

        ##########################
    for i in finalresult:
        sys.stdout.writelines(i+ "\n")
   

         
conversion()

    
