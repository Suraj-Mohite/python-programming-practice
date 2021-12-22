
"""
Function Name    : Question6
Input_Parameters : integer
return type      : -
Description      : This Function accepts one integer value and print the pattern.
Date             : 17/04/2021
Team             : Team-Extreme
Author Name      : Kirti Patil
Team Lead        : Suraj Mohite

"""
def Question6(n):
    if n<=0:
        print("ERROR:Invalid Input")
        return
        
    k =  2 
    for row in range(1,n+1):
        for col in range(1,2*n):
            if row+col==n+1 or col-row==n-1 :
                print("*",end="")
            elif row==n and col!=k:
                print("*",end="")
                k=k+2
            else:
                print(end=" ")
        print()

#Test cases
n = -5
Question6(n)

n = 0
Question6(n)

n = 6
Question6(n)
