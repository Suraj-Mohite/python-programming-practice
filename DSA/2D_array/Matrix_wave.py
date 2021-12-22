"""
[7,5,3,0]
[3,1,4,0]
[6,65,0,1]
"""


def Wave_Matrix(arr1):
    for i in range(len(arr1[0])):
        if i%2==0:
            for j in range(len(arr1)):
                print(arr1[j][i])
        else:
            for j in range(len(arr1)-1,-1,-1):
                print(arr1[j][i])

Wave_Matrix([[6,65,0,1],[7,5,3,0],[3,1,4,0],[6,65,0,1]])
print()
Wave_Matrix([[7,5,3,0]])
Wave_Matrix([[]])