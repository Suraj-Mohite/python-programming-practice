i=0
def printArr(arr):
    global i
    if i==len(arr)-1:
        print(arr[i])
        return
    print(arr[i])
    i+=1
    printArr(arr)

def printArrx(arr,i): #without globel
    if len(arr)==0:
        return
    i-=1
    if i==0:
        print(arr[i])
        return
    printArrx(arr,i)
    print(arr[i])
    i+=1
    

#printArr([10,20,30,45,6,0,50,60])
arr=[10,20,30,45,6,0,50,60]
a=[5]
printArrx(arr,len(arr))
printArrx(a,len(a))