def Matrix_Multiplication(arr1,arr2):
    if len(arr1[0])!=len(arr2):
        print("ERROR:Invalid Input")
        return
    result=[[None]*len(arr2[0]) for i in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[i])):
            mult=0
            for k in range(len(arr2)):
                mult+=(arr1[i][k]*arr2[k][j])
            result[i][j]=mult

    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j],end=" ")
        print()


Matrix_Multiplication([[2,6,5],[2,2,6]],[[7,5,3,0],[3,1,4,0],[6,5,0,1]])
print()
Matrix_Multiplication([[2,6,5]],[[7,5,3,0],[3,1,4,0],[6,5,0,1]])
Matrix_Multiplication([[2,6,5,564]],[[7,5,3,0],[3,1,4,0],[6,5,0,1]])