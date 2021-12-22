#Accept N number and target from User and return its Last occurance (Last index number)

def Last_Occurance(List1,Target):
    
    i=len(List1)-1
    while(i>=0):
        if List1[i]==Target:
            break
        i-=1
    if i<0:
        return -1
    else:
        return i

No=int(input("Enter the number of elements you want to enter into the List."))
List1=[]
print(f"Enter the {No} elements")
for i in range(No):
    element=int(input())
    List1.append(element)

Target=int(input("Enter the target\t"))

print(Last_Occurance(List1,Target))