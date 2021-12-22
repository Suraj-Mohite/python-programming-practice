"""
*           *  
*           *
*     *     *
*  *     *  *
*           *

"""
def pattern8(no):
    if no<=0 or no%2==0:
        print("error: invalid input")
        return
    n=(no//2)+1
    for i in range(1,no+1):
        for j in range(1,no+1):
            if j==1 or j==no or (i>=n and (j==2*n-i or j==i)):
                print("*",end="  ") #two spaces for broad pattern
            else:
                print(" ",end="  ")
        print()
pattern8(5)
pattern8(6)