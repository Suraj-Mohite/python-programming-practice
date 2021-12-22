def ArrayAdd(arr1,arr2):
    if len(arr1)> len(arr2):
        arr1,arr2=arr2,arr1

    for i in range(-1,-(len(arr1)+1),-1):   #arr1<arr2
        arr2[i]=arr1[i]+arr2[i]
    
    return arr2

print(ArrayAdd([1,1,2,3,2,6,9,9],[2,2,2,2,3,3,3,3]))
print(ArrayAdd([1,9],[2,2,2,2,3,3,3,3]))
print(ArrayAdd([1,1,2,3,2,6,9,9],[2,2,3,3,3]))