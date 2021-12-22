"""
[0,0,1,0],
[1,0,0,0],
[0,0,0,0],
[1,0,1,0]
"""


def exitPoint(arr):
    i=0
    j=0
    direction=0
    while(True):
        if direction==0:
            while j<len(arr[0]):
                if arr[i][j]==1:
                    i+=1
                    direction+=1
                    break
                j+=1
            else:
                j-=1
                break

        if direction==1:
            while i<len(arr):
                if arr[i][j]==1:
                    j-=1
                    direction+=1
                    break
                i+=1
            else:
                i-=1
                break     

        if direction==2:
            while j>-1:
                if arr[i][j]==1:
                    i-=1
                    direction+=1
                    break
                j-=1
            else:
                j+=1
                break

        if direction==3:
            while i>-1:
                if arr[i][j]==1:
                    j+=1
                    direction=0
                    break
                i-=1
            else:
                i+=1
                break
    
    return i,j


print(exitPoint([[0,0,0,1],[1,0,0,0],[0,0,0,0],[1,0,1,0]]))
