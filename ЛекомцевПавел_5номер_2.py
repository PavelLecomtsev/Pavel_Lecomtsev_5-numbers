minW=10**100 #1
for Q in range(10001,100000): #2
    m0=[] #3
    m1=[]
    for i in str(Q): #4
        if i=="0":
            m0.append(int(i))
        else:
            m1.append(int(i))
    m1.sort() #5
    if len(m1)==1: #6
        maxch=int(str(m1[0])+"0")
    else: 
        maxch=int(str(m1[-1])+str(m1[-2]))
    if len(m0)==0: #7
        minch=int(str(m1[0])+str(m1[1]))
    else:
        minch=int(str(m1[0])+"0")
    proizv=(maxch*minch)**2 #8
    proizv=str(proizv-Q) 
    proizv=proizv.replace("0","4") 
    W=int(proizv[::-1]) #9
    if W<minW: #10
        minW=W
print(minW)