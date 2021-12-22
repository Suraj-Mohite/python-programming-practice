#count number of elements of given sorted array

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

def Count_Elements(arr,element):
    First=First_Occurrance(arr,element)
    Last=Last_Occurrance(arr,element)

    if First>=0:
        return (Last-First)+1
    else:  #if element is not present then return 0
        return 0

print(Count_Elements([1,5,6,7,10,10,10,10,10,10,11,11,12,15],7))

