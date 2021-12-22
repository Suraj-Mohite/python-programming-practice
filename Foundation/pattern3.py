""" input:7

      1       
    2 3 2
  3 4 5 4 3
4 5 6 7 6 5 4
  3 4 5 4 3
    2 3 2
      1

"""

def Pattern3(no):
    if no%2==0:
        return
    n=(no//2)+1
    for i in range(1,no+1):
        if i<=n:
            val=i
        else:
            val=2*n-i
        for j in range(1,no+1):
            if i<=n and j<n and j>=(n-i)+1 and j<=n+(i-1):
                print(val,end=" ")
                val+=1
            elif i<=n and j>=n and j>=(n-i)+1 and j<=n+(i-1):
                print(val,end=" ")
                val-=1
            elif i>n and j<n and j>(i-n) and j<=no-(i-n):
                print(val,end=" ")
                val+=1
            elif i>n and j>=n and j>(i-n) and j<=no-(i-n):
                print(val,end=" ")
                val-=1
            else:
                print(" ",end=" ")
        print()

Pattern3(7)
            