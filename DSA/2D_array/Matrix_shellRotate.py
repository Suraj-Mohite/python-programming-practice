def rotateArray(arr,rot):
    if rot<0:
        rot=rot%len(arr)
        rot=len(arr)+rot
    if rot>=len(arr):
        rot=rot%len(arr)
    for i in range(rot):
        temp=arr[-1]
        for j in range(len(arr)-2,-1,-1):
            arr[j+1]=arr[j]
        arr[0]=temp
    return arr
def swapArray(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    
    return arr

#print(swapArray([10,20,30,40,50,60],3,5))
def rotateArrayX(arr,rot):
    if rot<0:
        rot=rot%len(arr)
        rot=len(arr)+rot
    if rot>=len(arr):
        rot=rot%len(arr)
    arr=swapArray(arr,0,len(arr)-rot-1)
    arr=swapArray(arr,len(arr)-rot,len(arr)-1)
    arr=swapArray(arr,0,len(arr)-1)
    return arr

def getShell(arr,shell):
    newArr=[]
    iMin=shell-1
    jMin=shell-1

    iMax=len(arr)-shell
    jMax=len(arr[0])-shell

    for i in range(iMin,iMax+1):
        newArr.append(arr[i][jMin])
    else:
        jMin+=1

    for j in range(jMin,jMax+1):
        newArr.append(arr[iMax][j])
    else:
        iMax-=1
    for i in range(iMax,iMin-1,-1):
        newArr.append(arr[i][jMax])
    else:
        jMax-=1
    
    for j in range(jMax,jMin-1,-1):
        newArr.append(arr[iMin][j])

    return(newArr)

def shellRotate(arr,shell,rot):
    if rot==0:
        return arr
    
    narr=getShell(arr,shell)
    narr=rotateArrayX(narr,rot)
    
    iMin=shell-1
    jMin=shell-1

    iMax=len(arr)-shell
    jMax=len(arr[0])-shell
    k=0
    for i in range(iMin,iMax+1):
        arr[i][jMin]=narr[k]
        k+=1
    else:
        jMin+=1

    for j in range(jMin,jMax+1):
        arr[iMax][j]=narr[k]
        k+=1
    else:
        iMax-=1

    for i in range(iMax,iMin-1,-1):
        arr[i][jMax]=narr[k]
        k+=1
    else:
        jMax-=1
    
    for j in range(jMax,jMin-1,-1):
        arr[iMin][j]=narr[k]
        k+=1

    return(arr)


# getShell([[11,12,13],
#           [21,22,23],
#           [31,32,33],
#           [41,42,43],
#           [51,52,53]],2)

#shellRotatex([[11,12,13],[21,22,23],[31,32,33],[41,42,43],[51,52,56]],2,0)

print(shellRotate([[11,12,13,14,15],
                   [21,22,23,24,26],
                   [31,32,33,34,35],
                   [41,42,43,44,45]],2,1))

                #    [[11, 12, 13, 14, 15], 
                #    [21, 34, 44, 43, 26], 
                #    [31, 24, 33, 42, 35], 
                #    [41, 23, 22, 32, 45], 
                #    [51, 52, 53, 54, 55]]