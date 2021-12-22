#Accept the array from user and print all the subset of that array

def printSubSet(arr,ind,ans,size):
    if ind==size:
        print(ans)
        return
    ans.append(arr[ind])
    printSubSet(arr,ind+1,ans,size)
    ans.pop()
    printSubSet(arr,ind+1,ans,size)

def countSubSet(arr,ind,size):
    if ind==size:
        return 1
    l=countSubSet(arr,ind+1,size)
    r=countSubSet(arr,ind+1,size)
    return l+r

def getSubSet(arr):
    if len(arr)==0:
        return [[]]
    
    ans=getSubSet(arr[1:])
    res=[]
    for i in ans:
        res.append(i)
        res.append([arr[0]]+i)
    
    return res

def getSubSet2(arr):
    if len(arr)==0:
        return [[]]
    
    ans=getSubSet2(arr[1:])
    res=[]
    for i in ans:
        res.append(i)
        res.append([arr[0]]+i)
    
    return list(set(res))



arr=[0]
# print(getSubSet2(arr))
print(countSubSet(arr,0,len(arr)))
printSubSet(arr,0,[],len(arr))