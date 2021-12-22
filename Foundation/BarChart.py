def Barchart(arr):
    no=max(arr)
    for i in range(1,no+1):
        for j in range(len(arr)):
            if i>=(no-arr[j]+1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

if __name__=="__main__":
    Barchart([3,1,0,7,5])
    Barchart([2,0,1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,0,2])
    Barchart([2,0,1,2,7,6,3,1,0,2])