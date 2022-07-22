for A in range(1,1000): #1
    B=bin(A)[2::] #2
    B=B+B[-1]+B[-1] #3
    summa=B.count("1") #4
    summa=str(summa%2) #5
    B=B+summa #6
    B=int(B,2) #7
    if B%41==0: #8
        print(A) #9
        break #10