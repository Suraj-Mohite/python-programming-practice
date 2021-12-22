#write a python function that take number as parameter and check whether prime or not

def Check_Prime(No):
    if No<0:
        No=-No
    if No==0 or No==1:
        return False
    if No==2 or No==3:
        return True
    cnt=0
    item=1
    middle_last=No//2
    while(item<=No//4):
        cnt+=1
        item+=1
        if No % item==0:
           break
        if No%middle_last==0:
            break
        middle_last-=1
    print(cnt)
    if item>No//4:
        return True
    else :
        return False

        
def Check_Primex(No):
    if No<0:
        No=-No
    if No==0 or No==1 or No==4:
        return False
    if No==2 or No==3:
        return True
    cnt=0
    item=1
    middle_last=No//2
    while(item<=No//4):
        cnt+=1
        item+=1
        if No % item==0:
           break
        if No%middle_last==0:
            break
        middle_last-=1
    print(cnt)
    if item>No//4:
        return True
    else :
        return False

No=int(input("Enter the number.\n"))
print(Check_Prime(No))
print(Check_Primex(No))