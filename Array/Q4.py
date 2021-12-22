"""
Function Name    : fun
Input_Parameters : integer
return type      : -
Description      : This Function accepts one integer value and print the pattern.
Date             : 17/04/2021
Team             : Team-Extreme
Author Name      : 
Team Lead        : Suraj Mohite

"""
def fun(n):
    if n<=0:
        print("ERROR:Invalid Input")
        return

    for i in range(1,n+1):
        # It is used for number of spaces
        for j in range((n+1)-i):
            print(end=" ")
        # It is used for printing star
        for k in range(2*i-1):
            print("*",end="")
        print()

#Taste cases

n=0
fun(n)
n=6
fun(n)
n=-3
fun(n)
n=5
fun(n)

