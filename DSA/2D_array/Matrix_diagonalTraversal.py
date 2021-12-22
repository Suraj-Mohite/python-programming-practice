def diagonalTraverse(arr):
    row=len(arr)
    col=len(arr[0])

    for i in range(row-1,0,-1):
        for j in range(i,row):
            print(arr[j][j-i])
    
    for i in range(row):
        for j in range(i,col):
            print(arr[j-i][j])

diagonalTraverse([[10,20,30,40],
                 [11,22,33,44],
                 [4,5,9,8],
                 [22,4,5,7]])
