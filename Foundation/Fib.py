# accept the number from user and print N number of Fibonacci numbers 

def Fib(n):
    if n<=0:
        return
    if n==1:
        print(0)
        return
    i=0
    j=1
    print(i,end=" ")
    print(j,end=" ")
    for Num in range (n-2):
        k=i+j
        print(k,end=" ")
        i,j=j,k
    print()
Fib(0)
Fib(1)
Fib(2)
Fib(12)
Fib(-3)
Fib(21)