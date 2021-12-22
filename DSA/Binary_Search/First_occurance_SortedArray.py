def First_Occurrance(arr,key):
    Start=0
    End=len(arr)-1
    index=-1

    while(Start<=End):
        mid=Start+(End-Start)//2

        if arr[Start]==key:
            index=Start
            break
        if arr[mid]==key and arr[mid-1]!=key:
            index=mid
            break
        if arr[mid]<key:
            Start=mid+1
        else:
            End=mid-1
    return index

print(First_Occurrance([1,5,6,7,10,10,10,10,10,10,11,11,12,15],11))
