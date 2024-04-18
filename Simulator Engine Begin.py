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
