#Find Duplicate element in an array

def Duplicate(arr):
    arr1=arr
    arr=list(set(arr))

    for i in arr:
        arr1.remove(i)
    return arr1


print(Duplicate([4,3,2,7,8,2,3,1]))
        