#find how many time the sorted array is rotated (anticlockwise).
#[9,10,12,2,3,5,6,7,8] output=3 
#[12,2,3,5,6,7,8,9,10] output=1 

def Rotated_Array_cnt(arr):
    Start=0
    End=len(arr)-1
    rotation=0
    if arr[Start]<arr[End]:
        return rotation
    while Start<=End:
        mid=Start+(End-Start)//2

        if (Start==End):
            rotation=mid
            break

        if(arr[mid-1]>arr[mid] and arr[mid+1]>arr[mid]):
            rotation=mid
            break

        if arr[Start]>arr[mid]:
            End=mid-1
        elif arr[End]<arr[mid]:
            Start=mid+1
    return rotation

print(Rotated_Array_cnt([9,10,12,22,33,55,66,77,8]))
        

