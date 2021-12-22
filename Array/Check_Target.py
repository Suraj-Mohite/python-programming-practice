#Accept N number and Target From User and check whether that Target is present in it or not

def Check_Target(List1,Target):
    if List1==[]:
        return -1

    end=len(List1)-1
    i=0
    while(i<=end):
        if List1[i]==Target or List1[end]==Target:
            break
        i+=1
        end-=1
    if i>end:
        return False
    else:
        return True


No=int(input("Enter the number of elements you want to enter into the List."))
List1=[]
print(f"Enter the {No} elements")
for i in range(No):
    element=int(input())
    List1.append(element)

Target=int(input("Enter the target\t"))

print(Check_Target(List1,Target))