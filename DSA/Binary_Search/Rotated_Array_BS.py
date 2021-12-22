def Rotated_Array_Search(arr,key):
    Start=0
    End=len(arr)-1
    index=-1
    c=0
    while Start<=End:
        mid=Start+(End-Start)//2

        if(arr[mid]==key):
            index=mid
            break
        if(arr[Start]==key):
            index=Start
            break
        if(arr[End]==key):
            index=End
            break
                
        if arr[Start]<arr[mid]:
            if key<arr[mid] and key>arr[Start]:
                End=mid-1
            else:
                Start=mid+1

        if arr[End]>arr[mid]:
            if key>arr[mid]and key<arr[End]:
                Start=mid+1
            else:
                End=mid-1
    return index

print(Rotated_Array_Search([9,10,12,22,33,55,66,6,8],8))