"""
1               1 
1 2           2 1
1 2 3       3 2 1
1 2 3 4   4 3 2 1
1 2 3 4 5 4 3 2 1 

"""


def pattern4(no):
    if no<=0:
        print("Error: Invalid Input")
    for i in range(1,no+1):
        val=i
        if i==no:
            val=i-1
        for j in range(1,2*no):
            if j<=i:
                print(j,end=" ")
            elif j>i and j>=2*no-i:
                print(val,end=" ")
                val-=1
            else:
                print(" ",end=" ")
        print()

pattern4(5)
pattern4(0)
pattern4(-9)
