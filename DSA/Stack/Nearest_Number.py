#create 4 functions 
# 1. will return array of nearest largest/Greatest number from right
# 2. will return array of nearest Smallest number from right
# 3. will return array of nearest largest/Greatest number from left
# 4. will return array of nearest Smallest number from left

#if there is no nearset number then return -1
#eg [1,2,5,45,16,12,7,9]
#output: 
#nearest largest/Greatest number from right [2,5,45,-1,-1,-1,9,-1]
#nearest Smallest number from right [-1,-1,-1,16,12,7,-1,-1]
#nearest largest/Greatest number from left [-1,-1,-1,-1,45,16,12,12]
#nearest Smallest number from left [-1,1,2,5,5,5,5,7]

def Nearest_Smallest_From_Left(arr):
    stack=[]
    vector=list(range(len(arr)))

    for i in range(len(arr)):              
        if len(stack)==0:
            vector[i]=-1
        elif stack[-1]<arr[i]:
            vector[i]=stack[-1]
        elif stack[-1]>=arr[i]:
            while(len(stack)!=0 and stack[-1]>=arr[i]):
                stack.pop()
            if len(stack)==0:
                vector[i]=-1
            elif stack[-1]<arr[i]:
                vector[i]=stack[-1]

        stack.append(arr[i])
    
    return vector
        
def Nearest_Largest_From_Right(arr):
    stack=[]             #[5,16,15,4,2,6,1,1,1,9,8,6,3,7,15]
    vector=[]

    for i in arr[::-1]:
        if len(stack)==0:
            vector.append(-1)
        elif stack[-1]>i:
            vector.append(stack[-1])
        elif stack[-1]<=i:
            while (len(stack)!=0 and stack[-1]<=i):
                stack.pop()
            if len(stack)==0:
                vector.append(-1)
            elif stack[-1]>i:
                vector.append(stack[-1])
        stack.append(i)
    return vector[::-1]

def Nearest_Smallest_From_Right(arr):
    stack=[]
    vector=[]
    for i in arr[::-1]:
        if len(stack)==0:
            vector.append(-1)
        elif stack[-1]<i:
            vector.append(stack[-1])
        elif stack[-1]>=i:
            while len(stack)!=0 and stack[-1]>=i:
                stack.pop()
            if len(stack)==0:
                vector.append(-1)
            else:
                vector.append(stack[-1])
        stack.append(i)
    
    return vector[::-1]

def Nearest_Largest_From_left(arr):
    stack=[]
    vector=[]
     
    for i in arr:
        if len(stack)==0:
            vector.append(-1)
        elif stack[-1]>i:
            vector.append(stack[-1])
        elif stack[-1]<=i:
            while len(stack)!=0 and stack[-1]<=i:
                stack.pop()
            if len(stack)==0:
                vector.append(-1)
            elif stack[-1]>i:
                vector.append(stack[-1])
        stack.append(i)
    return vector


print("\nnearest largest/Greatest number from right :",Nearest_Largest_From_Right([5,16,15,4,2,6,1,1,1,9,8,6,3,7,15]))
print("\nnearest Smallest number from Right :",Nearest_Smallest_From_Right([5,16,15,4,2,6,1,1,1,9,8,6,3,7,15]))
print("\nnearest largest/Greatest number from left :",Nearest_Largest_From_left([5,16,15,4,2,6,1,1,1,9,8,6,3,7,15]))
print("\nNearest Smallest number from left :",Nearest_Smallest_From_Left([5,16,15,4,2,6,1,1,1,9,8,6,3,7,15]))