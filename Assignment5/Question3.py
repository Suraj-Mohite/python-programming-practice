"""
Write a program that asks the user for a number n and print whether the number is a prime number or not.
"""
#Time Complexity is O(N/2) of this function   
def Check_Prime(No):
    if No<0:
        No=-No
    if No==0 or No==1:
        return False
    if No==2 :
        return True
    item=1
    while(item<=No//2):
        item+=1
        if No % item==0:
           break
    if item>No//2:
        return True
    else :
        return False


No=int(input("Enter the number.\n"))

if Check_Prime(No)==True:
    print("Prime Number")
else:
    print("NOT Prime Number")


