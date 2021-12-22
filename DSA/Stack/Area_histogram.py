#[5,16,11,8,8,9,8,6,3,7,15,15,4,2,6,7]
#Assumption : All Elements of array are positive
def left_near_small(arr):
    List1=list(range(len(arr)))       #[5,16,11,8,8,9,8,6,3,7,15,15,4,2,6,7]
    stack=[]  #this stack will contain index of gretest near element

    for i in range(len(arr)):
        if len(stack)==0:
            List1[i]=-1
            List1[i]=i-List1[i]
        elif arr[stack[-1]]<arr[i]:
            List1[i]=stack[-1]
            List1[i]=i-List1[i]
        elif arr[stack[-1]]>=arr[i]:
            while len(stack)!=0 and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if len(stack)==0:
                List1[i]=-1
                List1[i]=i-List1[i]
            elif arr[stack[-1]]<arr[i]:
                List1[i]=stack[-1]
                List1[i]=i-List1[i]

        stack.append(i)
    print(List1)
    return List1

def right_near_small(arr):
    stack=[]
    list1=list(range(len(arr)))
    list2=list(range(len(arr)))
    for i in list2[::-1]:
        if len(stack)==0:
            list2[i]=len(list1)
            list2[i]=len(list1)-i-1
        elif arr[stack[-1]]<arr[i]:
            list2[i]=stack[-1]
            list2[i]=stack[-1]-i-1
        elif arr[stack[-1]]>=arr[i]:
            while len(stack)!=0 and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if len(stack)==0:
                list2[i]=len(list1)
                list2[i]=len(list1)-i-1
            elif arr[stack[-1]]<arr[i]:
                list2[i]=stack[-1]
                list2[i]=stack[-1]-i-1

        stack.append(i)
    print(list2)
    return list2

def histo(arr):
    left=left_near_small(arr)
    right=right_near_small(arr)
    max1=0
    for i in range(len(arr)):
        area=(left[i]+right[i])*arr[i]
        if area>max1:
            max1=area
    return max1



print([2,1,5,6,2,3])
print(histo([2,1,5,6,2,3]))

print([5,16,11,8,8,9,8,6,3,7,15,15,4,2,6,7])
print(histo([5,16,11,8,8,9,8,6,3,7,15,15,4,2,6,7]))
print(histo([1,1,1,1,1,1,1,1]))
print(histo([1,2,3,4,5,6,7,8,9]))