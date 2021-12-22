def searchInTwoDSorted(arr,no):
    i=len(arr)-1
    j=0
    while(True):
        if(arr[i][j])==no:
            break
        if(arr[i][j]<no):
            j+=1
        elif(arr[i][j]>no):
            i-=1
        if i==-1 or j==len(arr[0]):
            break
    if i==-1 or j==len(arr[0]):
        return -1
    return (i,j)

print(searchInTwoDSorted([[1,2,3,4],
                         [5,6,7,8],
                         [9,10,11,12],
                         [13,14,15,16]],1))