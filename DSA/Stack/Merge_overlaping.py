def Merge_overlaping(arr):
    arr.sort()
    stack=[]
    stack.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i][0]<=stack[-1][1]:
            if arr[i][1]>stack[-1][1]:
                stack[-1][1]=arr[i][1]
        else:
            stack.append(arr[i])
    return stack

print(Merge_overlaping([[22,28],[1,8],[25,27],[14,19],[27,30],[5,12]]))
print(Merge_overlaping([[22,28],[151,100],[25,227],[114,19],[27,302],[5,12]]))