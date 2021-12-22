#floor is greatesr number smaller than the number whose floor has to be calculated

def floor(arr,no):
    Start=0
    End=len(arr)-1
    floor_no=0

    while Start<=End:
        mid=Start+(End-Start)//2

        if arr[mid]==no:
            floor_no=arr[mid]
            break
        if arr[mid]<no:
            floor_no=arr[mid]
            Start=mid+1
        elif arr[mid]>no:
            End=mid-1
    return floor_no

print(floor([-1,2,3,4,5,7,8,9,45],0))
