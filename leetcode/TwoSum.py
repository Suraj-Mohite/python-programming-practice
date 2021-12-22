'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Input: nums = [], target = 6
Output: [0,1]
Input: nums = [3,3], target = 7
Output: []

'''
#APPROACH 1

def Two_Sum(List1,Target):
    
    List_Temp=[]
    for i in range(len(List1)-1):
        for j in range(i+1,len(List1)):
            if(List1[i]+List1[j]==Target):
                List_Temp.append(i)
                List_Temp.append(j)
                break
    
    return List_Temp


#APPROACH 2

def Two_Sum2(List1,Target):
    check={}
    temp=0
    temp2=0
    for i in range(len(List1)):
        temp=Target-List1[i]
        if List1[i] not in check:
            check[temp]=i
        else:
            temp=check[List1[i]]
            temp2=i
            break
    print(check)
    return[temp,temp2]

No=int(input("Enter Number of element in List. \n"))
List1=[]
for i in range(No):
    print("Enter the element at position ",i)
    element=int(input())
    List1.append(element)

print(List1)
Target=int(input("Enter the Target : "))

print(Two_Sum2(List1,Target))