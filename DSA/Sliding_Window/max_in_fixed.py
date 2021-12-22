"""def First_Negative(arr,k):
    i=0
    j=1
    list1=[] #this list contain the index of negative elements
    vector=[]
    max1=arr[0]
    list1.append(0)

    while j<len(arr):
        if arr[j]>max1:
            max1=arr[j]
            list1.pop()
            list1.append(j)    
        if j-i+1<k:
            j+=1
        elif j-i+1==k:
            if i<=list1[0]:
                vector.append(arr[list1[0]])
            else:
                list1.remove(list1[0])
                vector.append(arr[list1[0]])
            i+=1
            j+=1
    return vector

print(First_Negative([9,6,-9,6,5,8,5,4,6,9,7,8,5],3))"""