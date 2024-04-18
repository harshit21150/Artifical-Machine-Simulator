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
        print(i)
