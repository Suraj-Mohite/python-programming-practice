"""
Function Name    : Question2
Input_Type       : integer
return type      : -
Description      : This Function accepts one integer value and print the pattern.
Date             : 17/04/2021
Team             : Team-Extreme
Author Name      : Roshan Jha
Team Lead        : Suraj Mohite

"""


def Question2(rows):
    if rows<=0:
        print("ERROR:Invalid Input")
        return

    while rows>=0:
        print('*'*rows) 
        rows-=1

#Test cases
n = -5
Question2(n)

n = 0
Question2(n)

n = 6
Question2(n)