alp="01234567" #1
P=-1
for X1 in range(1,8): #2
    for X2 in alp:
        ch1=str(X1)+X2 #3
        for Y1 in range(1,8):
            for Y2 in alp:
                ch2=str(Y1)+Y2 #4
                nov1=int(ch1[0])+int(ch2[0]) #5
                nov2=int(ch1[1])+int(ch2[1])
                if nov1>=nov2: #6
                    vozrast=int(str(nov1)+str(nov2))
                else:
                    vozrast=int(str(nov2)+str(nov1))
                vozrast=bin(vozrast)[3::] #7
                vozrast=vozrast.replace("1","е") #8
                vozrast=vozrast.replace("0","н")
                vozrast=vozrast.replace("е","0")
                vozrast=vozrast.replace("н","1")
                vozrast="1"+vozrast #9
                vozrast=int(vozrast,2) #10
                if vozrast>P: #11
                    P=vozrast
print(P)