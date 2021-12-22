def display(newArr):
    for i in range(len(newArr)):
        for j in range(len(newArr[i])):
            print(newArr[i][j],end=" ")
        print()
    print()

def diagonalSort(arr):
    row=len(arr)
    col=len(arr[0])

    display(arr)
    for i in range(row-1,0,-1):
        newArray=[]
        for j in range(i,row):
            newArray.append(arr[j][j-i])
        newArray.sort()
        k=0
        for j in range(i,row):
            arr[j][j-i]=newArray[k]
            k+=1
    
    for i in range(row):
        newArray=[]
        for j in range(i,col):
            newArray.append(arr[j-i][j])
        newArray.sort()
        k=0
        for j in range(i,col):
            arr[j-i][j]=newArray[k]
            k+=1

    display(arr)

diagonalSort([[10,20,30,40],
                 [11,22,33,44],
                 [4,5,9,8],
                 [22,4,5,7]])
diagonalSort([[10,6,7,8,9],[11,22,41,2,3],[3,3,2,9,7],[7,8,9,4,5],[9,8,7,3,2]])