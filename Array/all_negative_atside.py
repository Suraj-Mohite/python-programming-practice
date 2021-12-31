#write a function which will move all negative elements at one side

def Move_negative(arr):
    i=0
    j=1
    while j<len(arr):
        if arr[i]<0:
            i+=1
            j+=1
        elif arr[j]>=0:
            j+=1
        elif arr[j]<0:
            arr[i],arr[j]=arr[j],arr[i]
        
    return arr

def Move_negative1(arr):
    i=0
    j=0
    while j<len(arr):
        if i!=j and arr[j]<0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1
    return arr

print(Move_negative([1,-8,-9,7,-6,-8,-7,5,-5]))
print(Move_negative1([1,-8,-9,7,-6,-8,-7,5,-5]))
print(Move_negative([]))
print(Move_negative1([]))

