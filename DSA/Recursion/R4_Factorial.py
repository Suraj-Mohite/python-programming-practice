def factorial(N):
    if N==0:
        return 1
    return N * factorial(N-1)

print(factorial(0))
print(factorial(5))
print(factorial(10))
print(factorial(15))