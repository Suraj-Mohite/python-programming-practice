def Pattern(row):
    if row%2==0:
        print("ERROR:Please Enter odd number")
        return
    n=(row//2)+1
    for i in range(1,row+1):
        for j in range(1,row+1):
            if i<=n and j==(n-i)+1 or j==(n+i)-1:
                print("*",end=" ")
            elif i>n and j==(i-n)+1 or j==(row+1)-((i-n)+1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

Pattern(17)

