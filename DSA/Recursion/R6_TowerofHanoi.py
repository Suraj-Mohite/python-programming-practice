def towerOfHanoi(N,s,d,h):
    if N==1:
        print(f"{N}->[{s} to {d}]")
        return

    towerOfHanoi(N-1,s,h,d)
    print(f"{N}->[{s} to {d}]")
    towerOfHanoi(N-1,h,d,s)


towerOfHanoi(4,1,2,3)
