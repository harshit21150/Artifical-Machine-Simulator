def swap():
    for i in range(0,len(code)):
            spacecheck="".join(code[i])
            if len(spacecheck)==0:
                resstring="ERROR: EMPTY LINE"
            elif ":"==code[i][0][-1]:
                labelpc[code[i][0]]=i
                sublist=code[i]
                sublen=len(code[i])
                if sublen>5:
                    labresstring="ERROR: INVALID OPERATION IN GIVEN :"+str(code[i][0])+"in line"+str(i)
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
