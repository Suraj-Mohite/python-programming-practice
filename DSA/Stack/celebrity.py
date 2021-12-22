#Celebrity Problem

def Celebrity(arr):
    result=-1
    stack=list(range(len(arr)))
    while len(stack)!=1:
        no1=stack[-1]
        stack.pop()
        no2=stack[-1]
        stack.pop()
        if arr[no1][no2]==1:
            stack.append(no2)
        else:
            stack.append(no1)
    for i in range(len(arr)):
        if arr[stack[-1]][i]==1:
            break
    else:
        result=stack[-1]

    return result


print(Celebrity([[0,0,0,0,0],[0,1,1,1,1],[1,0,0,1,0],[1,0,0,1,0],[0,1,0,1,0]]))