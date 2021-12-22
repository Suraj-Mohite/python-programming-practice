import random

def One_missing_Number(List1):
    for i in range(len(List1)+1):
        miss=None
        if i not in List1:
            miss=i
            break
    return miss


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

print("Missing number is :",One_missing_Number(List1))

Random_item=random.choice(List1)
List1.remove(Random_item)

Random_item=random.choice(List1)
List1.remove(Random_item)
print("Actual list :",list2)
print("After deleting items :",List1)
print("Missing number are :",Three_missing_Number(List1))