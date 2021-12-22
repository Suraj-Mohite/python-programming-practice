#if all numbers right to the number of array are smaller than that number then it is called as leader

def Leader(arr):
    stack=[]
    result=[]
    for i in arr[::-1]:
        if len(stack)==0:
            result.append(i)
        elif stack[-1]<i:
            while len(stack)!=0 and stack[-1]<i:
                stack.pop()
            if len(stack)==0:
                result.append(i)
        stack.append(i)
    return result[::-1]

print(Leader([110,204,52,4,3,6,8,2]))
print(Leader([1,2,3,4,5,6,7]))
            