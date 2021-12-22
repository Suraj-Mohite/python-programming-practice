#accept number and print decrease and increase order

def displayDecreaseIncrease(N):
    if N==0:
        return
    print(N)
    displayDecreaseIncrease(N-1)
    print(N)

displayDecreaseIncrease(10)