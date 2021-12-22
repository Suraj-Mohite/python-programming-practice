def towerOfHanoi(no,s,d,h):
    if no==0:
        return
    towerOfHanoi(no-1,s,h,d)
    print(f"plate {no} Moves from {s} to {d}.")
    towerOfHanoi(no-1,h,d,s)

towerOfHanoi(3,'A','B','C')

# find the number of moves required to move all plates from source to destination by fulfilling all the conditions
print()
def movesIntowerOfHanoi(no,s,d,h):
    if no==0:
        return 0
    i=movesIntowerOfHanoi(no-1,s,h,d)
    # steps=1
    j=movesIntowerOfHanoi(no-1,h,d,s)
    # return i+j+steps
    return i+j+1

print(movesIntowerOfHanoi(3,'A','B','C'))