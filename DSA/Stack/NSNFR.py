#find nearest grestest number from right

def NSNFR(arr):
    stack=[0]
    for i in range(1,len(arr)):
        if arr[i]>=arr[stack[-1]]:
            stack.append(i)
        else:
            while len(stack)!=0 and  arr[i]<arr[stack[-1]]:
                arr[stack[-1]]=arr[i]
                stack.pop()
            stack.append(i)
    else:
        while len(stack)!=0:
            arr[stack[-1]]=-1
            stack.pop()
    return arr

print(NSNFR([5,16,15,4,2,6,1,1,1,9,8,6,3,7,15]))
print(NSNFR([6,5,4,3,2,1]))
print(NSNFR([1,2,3,4,5,6]))
        