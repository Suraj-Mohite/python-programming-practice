
"""
      *        
      *  *
*  *  *  *  *
      *  *
      *

"""


def pattern5(no):
    if no%2==0:
        return
    n=(no//2)+1
    for i in range(1,no+1):
        for j in range(1,no+1):
            if i<n and j>=n and j<n+i:
                print("*",end="  ") #two spaces for broad pattern
            elif i==n:
                print("*",end="  ")
            elif i>n and j>=n and j<=no-(i-n):
                print("*",end="  ")
            else:
                print(" ",end="  ")
        print()
pattern5(5)
