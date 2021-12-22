#find maximum area of given binary matrix

def Zero(size):
    List1=[]
    for i in range (size):
        List1.append(0)
    return List1

def left_near_small(arr):
    List1=list(range(len(arr)))       
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
    #print(List1)
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
    #print(list2)
    return list2

def histo(arr):
    #print(arr)
    left=left_near_small(arr)
    right=right_near_small(arr)
    max1=0
    for i in range(len(arr)):
        area=(left[i]+right[i])*arr[i]
        if area>max1:
            max1=area
    return max1


def Max_Area(arr):

    List1=Zero(len(arr[0])) #to create list with all elements 0
    
    max1=0
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==0:
                List1[j]*=0
            else:
                List1[j]+=1
        area=histo(List1)
        if area>max1:
            max1=area
    return max1

row=int(input("Enter the number of the row : "))
col=int(input("Enter the number of the column : "))
list1=[]
for i in range(row):
    l=[]
    for j in range(col):
        print(f"[{i}][{j}]")
        ele=int(input())
        l.append(ele)
    list1.append(l)
print()
for i in list1:
    for j in i:
        print(j,end=" ")
    print()


print("\nMax rectangle area of given binary matrix is ",Max_Area(list1))


