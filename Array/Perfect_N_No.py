#Accept N number from user and display all the perfect number from that N numbers

def Check_Perfect(No):
    if No<0:
        return None

    if No==0 or No==1:
        return False

    iSum=0
    for i in range(1,(No//2)+1):
        if No%i==0:
            iSum+=i
    
    if iSum==No:
        return True
    else:
        return False

def Display_Perfect(List):
    if List==[]:
        return None
    Temp_List=[]

    List=list(set(List)) #if input contain duplicate perfect number then it will return once due to set
    for i in List:
        if(Check_Perfect(i)==True):
            Temp_List.append(i)
    return Temp_List


No=int(input("Enter the number of elements you want to enter into the List."))
List1=[]
print(f"Enter the {No} elements")
for i in range(No):
    element=int(input())
    List1.append(element)
print(Display_Perfect(List1))
