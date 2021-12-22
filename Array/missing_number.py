import random

#APPROACH 1

def One_missing_Number(List1):
    for i in range(len(List1)+1):
        miss=None
        if i not in List1:
            miss=i
            break
    return miss

#APPROACH 2

def One_missing_NumberX(List1):
    N=len(List1)
    Sum_Temp=N*(N+1)//2
    Sum=0
    for i in List1:
        Sum=Sum+i
    return Sum_Temp-Sum


def Three_missing_Number(List2):
    #List2=list(set(List2))
    List=[]
    for i in range(len(List2)+3):
        if i not in List2 :
            List.append(i)
    return List



List1=list(range(0,6))
list2=list(range(0,6))

Random_item=random.choice(List1)
List1.remove(Random_item)

print("\nMissing number is (Approach 1):",One_missing_Number(List1))
print("Missing number is (Approach 2) :",One_missing_NumberX(List1))

Random_item=random.choice(List1)
List1.remove(Random_item)

Random_item=random.choice(List1)
List1.remove(Random_item)
print("Actual list :",list2)
print("After deleting items :",List1)
print("Missing number are :",Three_missing_Number(List1),end="\n\n")