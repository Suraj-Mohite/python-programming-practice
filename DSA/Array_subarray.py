def printSubarray(array1):
    for i in range(len(array1)):
        for j in range(i,len(array1)):
            lst=[]
            for k in range(i,j+1):
                lst.append(array1[k])
            print(lst)


printSubarray([10,20,30,54])