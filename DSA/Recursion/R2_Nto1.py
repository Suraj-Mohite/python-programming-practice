#print N to 1

def displayRevNum(N):
    if N==0:
        return
    print(N)
    displayRevNum(N-1)

displayRevNum(10)