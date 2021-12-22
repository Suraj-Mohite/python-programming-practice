# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-2)+fib(n-1)

fib=lambda n: n if n==0 or n==1 else fib(n-2)+fib(n-1)

# print(fib(9))

def productFib(no):
    result=[]
    m=1
    while(m):
        l=fib(m)
        r=fib(m+1)
        if(l*r==no):
            result=[l,r,True]
            break
        
        if(l*r>no):
            result=[l,r,False]
            break
        m+=1
    return result
        

print(productFib(714))
print(productFib(800))