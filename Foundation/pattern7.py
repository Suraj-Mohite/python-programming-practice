"""
*  *  *     *  
      *     *
*  *  *  *  *
*     *
*     *  *  *

"""

def pattern7(no):
    if no<=0 or no%2==0:
        print("ERROE:Invalid input")
        return
    n=(no//2)+1
    for i in range(1,no+1):
        for j in range(1,no+1):
            if i==n or j==n or (i==1 and j<n) or (i==no and j>n) or (j==no and i<n) or (j==1 and i>n):
                print("*",end="  ")#two spaces for broad pattern
            else:
                print(" ",end="  ")
        print()
pattern7(5)
pattern7(6)