def printPat(n):
    i=n
    while i>=1:
        icnt=1
        j=n
        while j>=1:
            if icnt<=i:
                print(j,end=" "),
                icnt+=1
            else:
                j-=1
                icnt=1
        print("$",end=""),
        i-=1
printPat(1)