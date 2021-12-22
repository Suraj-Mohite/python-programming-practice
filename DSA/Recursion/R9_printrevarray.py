#print reverse array by recursion:

def revArray(arr,size):
    if size==0:
        return
    print(arr[size-1])
    revArray(arr,size-1)

def revArrayx(arr,idx):
    if idx==len(arr):
        return
    revArrayx(arr,idx+1)
    print(arr[idx])
    

arr=[10,20,30,4,5,6,7,22,9,8]
arr1=[]
# revArray(arr,len(arr))
# revArray(arr1,len(arr1))
revArrayx(arr,0)