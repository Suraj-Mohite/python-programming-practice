"""def Question5(rows):
    #if input is 0 then it will not print anything
    if rows==0:
        return
    #if input is negative then it will convert it into positive number 
    if rows<0:
        rows=-rows
    # It is used to print space  
    k = 2 * rows - 2  
    # Outer loop in reverse order  
    for i in range(rows, -1, -1):  
    # Inner loop will print the number of space.  
        for j in range(k, 0, -1):  
            print(end=" ")  
        k = k + 1  
        # This inner loop will print the number o stars  
        for j in range(0, i + 1):
            print("*", end=" ")  
        print("")  

rows = int(input("Enter the number of rows: "))

Question5(rows)"""


"""#this fun() function accept one integer value and print the pattern.if input is negative then function make it positive and prints pattern
def fun(n):
    if n==0:
        print("ERROR:Invalid Input")
        return
    if n<0:
        n=-n

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



Function Name:Question2
Input_Parameters : integer
return type: -
Description:this function accept one integer value and print the pattern.if input is negative then function make it positive and prints pattern
Date: 17/04/2021
Author Name: Roshan Jha


def Question2(rows):
    if rows<0:
        rows=-rows
    while rows>=0:
        print('*'*rows) 
        rows-=1

rows=int(input("enter the no of rows: "))#Taking inputs from the user
Question2(rows)"""

"""
Function Name:Question1
Input_Parameters : integer,integer
return type: -
Description:this function accept two integer value and print the pattern.
Date: 17/04/2021
Author Name: Kirti Patil

def Question1(row,col):
    if row<=0 or col<=0:
        print("ERROR:Invalid Input")
    for i in range(row):  #it will take range from 0 t0 3 
        for j in range(col):   #loop for column
            if i == 0 or i==(row-1) or j==0 or j==(col-1): 
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("")
    
#test cases

row = -5   
col = 6   
Question1(row,col)

row = 5   
col = 6   
Question1(row,col)

row = 6   
col = 6   
Question1(row,col)

row = 0   
col = 0   
Question1(row,col)


n = int(input("enter the number of rows"))
for row in range (n):
  for col in range(n):
    if col==0 or row==0 or row+col==(n-1):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

 
n = 6
for row in range (n):
  for col in range(n):
    if col==0 or row==0 or row+col==(n-1):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()



def Question3(n):
    if n<=0:
        print("ERROR:Invalid Input")
        return
    for row in range (n):
        for col in range(n):
            if col==0 or row==0 or row+col==(n-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
n = int(input("enter the number of rows"))
Question3(n)"""

"""
Function Name    : Question4
Input_Parameters : integer
return type      : -
Description      : This Function accepts one integer value and print the pattern.
Date             : 17/04/2021
Team             : Team-Extreme
Author Name      : Mansee Bhandari
Team Lead        : Suraj Mohite

"""
def Question4(n):
    if n<=0:
        print("ERROR:Invalid Input")
        return

    for i in range(1,n+1):
        # It is used for number of spaces
        for j in range((n+1)-i):
            print(end=" ")
        # It is used for printing star
        for k in range(0,i):
            print("*",end=" ")
        print(" ")

#Test cases
n = 6
Question4(n)

n = -5
Question4(n)

n=0
Question4(n)