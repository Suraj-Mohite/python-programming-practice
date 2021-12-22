def Last_Occurrance(arr,key):
    Start=0
    End=len(arr)-1
    index=-1

    while(Start<=End):
        mid=Start+(End-Start)//2

        if arr[End]==key:
            index=End
            break
        if arr[mid]==key and arr[mid+1]!=key:
            index=mid
            break
        if arr[mid]>key:
            End=mid-1
        else:               #if arr[mid]<key or arr[mid+1]==key
            Start=Start+1
    return index

print(Last_Occurrance([1,5,6,7,10,10,10,10,10,10,11,11,12,15],7))