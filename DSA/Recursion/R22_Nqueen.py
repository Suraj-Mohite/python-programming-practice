def isQueenSafe(arr,row,col):
    size=len(arr[0])
    i=row
    j=col
    if row-1>=0 and col-1>=0:
        while(i>=0 and j>=0):
            if(arr[i-1][j-1]==1):
                return False
            i-=1
            j-=1
    i=row
    j=col
    if row-1>=0:
        while(i>=0):
            if(arr[i-1][j]==1):
                return False
            i-=1
    i=row
    j=col
    if (row-1>=0 and col+1<size):
        while(i-1>=0 and j+1<size):
            if(arr[i-1][j+1]==1):
                return False
            i-=1
            j+=1
    return True


def nQueen(arr,row):
    if row==len(arr):
        for i in arr:
            print(i)
        print()
        return
    for col in range(len(arr[0])):
        if (isQueenSafe(arr,row,col)):
            arr[row][col]=1
            nQueen(arr,row+1)
            arr[row][col]=0
        

#NQueen2 count the number of possibilities where N number of queens can fit is matrix
def isQueenSafe2(arr,row,col):
    size=len(arr[0])
    i=row
    j=col
    if row-1>=0 and col-1>=0:
        while(i>=0 and j>=0):
            if(arr[i-1][j-1]==1):
                return False
            i-=1
            j-=1
    i=row
    j=col
    if row-1>=0:
        while(i>=0):
            if(arr[i-1][j]==1):
                return False
            i-=1
    i=row
    j=col
    if (row-1>=0 and col+1<size):
        while(i-1>=0 and j+1<size):
            if(arr[i-1][j+1]==1):
                return False
            i-=1
            j+=1
    return True


def nQueen2(arr,row):
    if row==len(arr):
        return 1
    cnt=0
    for col in range(len(arr[0])):
        if (isQueenSafe2(arr,row,col)):
            arr[row][col]=1
            cnt+=nQueen2(arr,row+1)
            arr[row][col]=0    
    return cnt

arr=[[0]*5 for i in range(5)]
nQueen(arr,0)
print()
print(nQueen2(arr,0))
# print(isQueenSafe([[1,0,0,0],
#                    [0,0,0,0],
#                    [0,0,0,0],
#                    [0,0,0,0]],1,2))