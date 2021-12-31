#find smallest and second smallest number without using inbuilt function

def secondSmallest(arr):
    min=10**9
    for i in arr:
        if i<min:
            min=i
    print(min)

    secondSmallestnum=10**9
    for i in arr:
        if i>min and i<secondSmallestnum:
            secondSmallestnum=i
    print(secondSmallestnum)

def secondmin(arr):
    arr.sort()
    print(arr[0])
    print(arr[1])

# secondSmallest([2,7,8,1,1,1,1,5,6,4,9,88,45,6,3,77])
# secondSmallest([2,3])

secondmin([2,7,8,1,5,6,4,9,88,45,6,3,77])

# find second min even if input array contains duplicate elements igone duplicate element and find second min

def secmin(arr):
    arr=list(set(arr))
    arr.sort()
    print(arr)
    print(arr[0])
    print(arr[1])

secmin([22,2,2,2,7,8,1,1,1,1,5,6,4,9,88,45,6,3,77])
