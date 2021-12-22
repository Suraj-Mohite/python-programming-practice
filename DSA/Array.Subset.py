def decimalToBinary(no):
    result=[]
    while no!=0:
        result.append(no%2)
        no//=2
    return result[::-1]

def printSubset(arr1):
    for i in range(2**len(arr1)):
        lst=["-"]*len(arr1)
        ans=decimalToBinary(i)
        k=-1
        for j in ans[::-1]:
            if j==1:
                lst[k]=str(arr1[k])
            k-=1
        print(" ".join(lst))

def printSubsetX(arr1):
    for i in range(2**len(arr1)):
        lst=[]
        ans=decimalToBinary(i)
        k=-1
        for j in ans[::-1]:
            if j==1:
                lst.append(arr1[k])
            k-=1
        print(lst)

#printSubset([10,20,30,40,50])
printSubsetX([10,20,30])
#printSubsetX(['a','b','c'])
#printSubset([])