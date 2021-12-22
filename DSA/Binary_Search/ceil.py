def ceil(arr,no):
    Start=0
    End=len(arr)-1
    ceil_no=0

    while Start<=End:
        mid=Start+(End-Start)//2

        if arr[mid]==no:
            ceil_no=arr[mid]
            break
        if arr[mid]>no:
            ceil_no=arr[mid]
            End=mid-1
        elif arr[mid<no]:
            Start=mid+1
    return ceil_no

print(ceil([-1,2,3,4,5,7,8,9,45],10))



"""
def Stock_Spanx(arr):
    List1=[]       #[5,16,11,8,8,9,8,6,3,7,15,15,4,2,6,7]
    stack=[]

    for i in range(len(arr)):
        if len(stack)==0:
            List1.append(-1)
           # List1[i]=i-List1[i]
        elif len(stack)>0 and stack[-1][0]>arr[i]:
            List1.append(stack[-1][1])
            #List1[i]=i-List1[i]
        elif len(stack)>0 and stack[-1][0]<=arr[i]:
            while len(stack)!=0 and stack[-1][0]<=arr[i]:
                stack.pop()
            if len(stack)==0:
                List1.append(-1)
               # List1[i]=i-List1[i]
            elif len(stack)>0 and stack[-1][0]>arr[i]:
                List1.append(stack[-1][1])
               # List1[i]=i-List1[i]

        stack.append([arr[i],i])
    return List1
"""