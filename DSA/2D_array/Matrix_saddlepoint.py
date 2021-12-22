#saddle point is the point who is smallest in its rpw and largest in its column there could be only 1 or 0 saddle point . 2 saddle points in any 2D array is not possible
def findSaddlePoint(arr):
    result="no saddle"
    for i in range(len(arr)):
        minIndex=0
        for j in range(1,len(arr[i])):
            if arr[i][j]<arr[i][minIndex]:
                minIndex=j
        
        for k in range(len(arr)):
            if arr[k][minIndex]>arr[i][minIndex]:
                break
        else:
            result=arr[i][minIndex]
            break
    
    return result

print(findSaddlePoint([[-2,0,0,5,3],
                       [4,2,1,3,2],
                       [-4,-3,0,-2,6],
                       [5,3,-4,2,-6]]))
                       
print(findSaddlePoint([[-2,0,0,5,3],[4,2,-5,3,2],[-4,-3,0,-2,6],[5,3,-4,2,-6]]))
