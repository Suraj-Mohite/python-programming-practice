def pythagorian_tringle(no1,no2,no3):
    if no1==max(no1,no2,no3) and no1**2==no2**2+no3**2:
        return True
    elif no2==max(no1,no2,no3) and no2**2==no1**2+no3**2:
        return True
    elif no3==max(no1,no2,no3) and no3**2==no2**2+no1**2:
        return True
    else:
        return False

print(pythagorian_tringle(3,4,4))
print(pythagorian_tringle(3,4,5))
print(pythagorian_tringle(13,12,5))