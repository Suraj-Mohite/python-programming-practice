#Assumption length of Arr2>Arr1

def TwoArraySub(arr1,arr2):
    if len(arr1)>len(arr2):
        arr1,arr2=arr2,arr1

    quo=0
    for i in range(-1,-(len(arr1)+1),-1):
        if arr2[i]<(arr1[i]+quo):
            arr2[i]=(arr2[i]+10)-(arr1[i]+quo)
            quo=1
        else:
            arr2[i]=arr2[i]-(arr1[i]+quo)
            quo=0
    else:
        if quo!=0:
            i-=1
            arr2[i]=arr2[i]-quo

    return arr2

print(TwoArraySub([2,3,5,6,7,4,9,1,1,1,1,1,1,1,1],[1,1,1,1,9,6,2,2,3,1,1]))