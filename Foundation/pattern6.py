"""
* * * * * * * * * 
  *           *
    *       *
      *   *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

"""


def pattern6(no):
    
    if no<=0 or no%2==0:
        print("Error: invalid input")
        return
    n=(no//2)+1
    for i in range(1,no+1):
        for j in range(1,no+1):
            if i==1 or i==no:
                print("*",end=" ")
            elif i<=n and(j==i or j==2*n-i):
                print("*",end=" ")
            elif i>n and j>=2*n-i and j<=i:
                print("*",end=" ")
            else:
                print(" ",end=" ")

        print()
pattern6(9)