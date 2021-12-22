def SpanArray(arr):
    max1=arr[0]
    min1=arr[0]

    for i in arr:
        if i>max1:
            max1=i
        if i<min1:
            min1=i
    return max1-min1

print(SpanArray([10,20,30,5,6,4,1]))
print(SpanArray([1,1,1,1,1,1]))
#print(SpanArray([-1,1,16,1,-11,1]))
#print(SpanArray([-2,-5,-9,-8,-4,-7]))
