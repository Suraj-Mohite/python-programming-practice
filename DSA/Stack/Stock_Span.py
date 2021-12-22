def Stock_Span(arr):
    stack=[]
    vector=[]
    cnt=1
    temp=0

    for i in arr:
        if len(stack)==0:
            vector.append(1)
        elif stack[-1]>i:
            vector.append(1)
        elif stack[-1]<=i:
            j=-1
            while j>=-len(stack) and stack[j]<=i:
                cnt+=1
                j-=1

            vector.append(cnt)
        cnt=1    
        stack.append(i)
    return vector


#APPROACH 2
def Stock_Spanx(arr):
    List1=list(range(len(arr)))       #[5,16,11,8,8,9,8,6,3,7,15,15,4,2,6,7]
    stack=[]  #this stack will contain index of gretest near element

    for i in range(len(arr)):
        if len(stack)==0:
            List1[i]=-1
            List1[i]=i-List1[i]
        elif arr[stack[-1]]>arr[i]:
            List1[i]=stack[-1]
            List1[i]=i-List1[i]
        elif arr[stack[-1]]<=arr[i]:
            while len(stack)!=0 and arr[stack[-1]]<=arr[i]:
                stack.pop()
            if len(stack)==0:
                List1[i]=-1
                List1[i]=i-List1[i]
            elif arr[stack[-1]]>arr[i]:
                List1[i]=stack[-1]
                List1[i]=i-List1[i]

        stack.append(i)
    return List1


"""def Stock_Spanxx(arr):
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
            elif stack[-1][0]>arr[i]:
                List1.append(stack[-1][1])
               # List1[i]=i-List1[i]

        stack.append([arr[i],i])
    return List1"""

print(Stock_Span([5,16,11,8,8,9,8,6,3,7,15,15,4,2,6,7]))
print(Stock_Spanx([5,16,11,8,8,9,8,6,3,7,15,15,4,2,6,7]))
#print(Stock_Spanxx([5,16,11,8,8,9,8,6,3,7,15,15,4,2,6,7]))
"""print(Stock_Span([1,10,1,1,2,2,2,2,3,3,3,3]))
print(Stock_Spanx([1,10,1,1,2,2,2,2,3,3,3,3]))"""

            


