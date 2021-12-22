def Nearly_sort(arr,key):
    Start=0
    End=len(arr)-1
    index=-1

    while Start<=End:
        mid=Start+(End-Start)//2
        
        if arr[Start]==key:
            index=Start
            break
        if arr[End]==key:
            index=End
            break
        if arr[mid]==key:
            index=mid
            break
        if arr[mid-1]==key:
            index=mid-1
            break
        if arr[mid+1]==key:
            index=mid+1
            break
        if arr[mid]>key:
            End=mid-2
        elif arr[mid]<key:
            Start=mid+2
    return index

print(Nearly_sort([11,2],2))
print(Nearly_sort([1,2,3,4,6,9,8,10,11,12,16],4))
