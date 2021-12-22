def calculatePower(x,n):
    if n==0:
        return 1
    return x*calculatePower(x,n-1)

print(calculatePower(2,5))