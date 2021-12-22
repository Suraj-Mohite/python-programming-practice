#rotate matrix by 90,180,270 clockwise
#rotate matrix by 90,180,270 Anti-clockwise

def display(newArr):
    for i in range(len(newArr)):
        for j in range(len(newArr[i])):
            print(newArr[i][j],end=" ")
        print()


def transverseMatrix(arr):
    newArr=[[0]*len(arr) for i in range(len(arr[0]))]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            newArr[j][i]=arr[i][j]
    
    return newArr

def rowSwap(arr):
    for i in range(len(arr)):
        start=0
        end=len(arr[0])-1
        while(start<end):
            arr[i][start],arr[i][end]=arr[i][end],arr[i][start]
            start+=1
            end-=1
    return arr

def colSwap(arr):
    for i in range(len(arr[0])):
        start=0
        end=len(arr)-1

        while(start<end):
            arr[start][i],arr[end][i]=arr[end][i],arr[start][i]
            start+=1
            end-=1
    return arr

def rotateMatrix90Clockwise(arr):
    arr=transverseMatrix(arr)
    return rowSwap(arr)

def rotateMatrix90AntiClockwise(arr):
    arr=transverseMatrix(arr)
    return colSwap(arr)

def rotateMatrix180Clockwise(arr):
    arr=transverseMatrix(arr)
    arr=rowSwap(arr)
    arr=transverseMatrix(arr)
    return rowSwap(arr)

def rotateMatrix180AntiClockwise(arr):
    arr=transverseMatrix(arr)
    arr=colSwap(arr)
    arr=transverseMatrix(arr)
    return colSwap(arr)

def rotateMatrix270Clockwise(arr):
    arr=transverseMatrix(arr)
    arr=rowSwap(arr)
    arr=transverseMatrix(arr)
    arr=rowSwap(arr)
    arr=transverseMatrix(arr)
    return rowSwap(arr)

def rotateMatrix270AntiClockwiseX(arr):
    arr=transverseMatrix(arr)
    arr=colSwap(arr)
    arr=transverseMatrix(arr)
    arr=colSwap(arr)
    arr=transverseMatrix(arr)
    return colSwap(arr)

def rotateMatrix270ClockwiseX(arr):
    return rotateMatrix90AntiClockwise(arr)

def rotateMatrix270AntiClockwise(arr):
    return rotateMatrix90Clockwise(arr)


arr=[[1,2,3,4,5],[4,5,9,8,7]]
display(arr)
ans=rotateMatrix90Clockwise(arr)
print("result after 90 degree rotation  clockwise")
display(ans)

ans=rotateMatrix180Clockwise(arr)
print("result after 180 degree rotation clockwise")
display(ans)

ans=rotateMatrix270Clockwise(arr)
print("result after 270 degree rotation clockwise")
display(ans)

ans=rotateMatrix270ClockwiseX(arr)
print("result after 270 degree rotation clockwise  $$$.....")
display(ans)

ans=rotateMatrix90AntiClockwise(arr)
print("result after 90 degree rotation Anti-clockwise")
display(ans)

ans=rotateMatrix180AntiClockwise(arr)
print("result after 180 degree rotation Anti-clockwise")
display(ans)

ans=rotateMatrix270AntiClockwise(arr)
print("result after 270 degree rotation Anti-clockwise")
display(ans)

ans=rotateMatrix270AntiClockwiseX(arr)
print("result after 270 degree rotation Anti-clockwise $$$$.....")
display(ans)