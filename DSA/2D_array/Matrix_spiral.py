"""[
    [10,20,30,41],
    [51,60,70,80],
    [90,44,22,33],
    [61,7,18,21]

]"""


def spiral_matrix(arr):
    iMin=0
    jMin=0
    iMax=len(arr)-1
    jMax=len(arr[0])-1
    n=(len(arr)*len(arr[0]))
    cnt=0
    i=0
    while(cnt<n):
        while i<=iMax and cnt<n:
            print(arr[i][jMin])
            cnt+=1
            i+=1
        else:
            jMin+=1
            i=jMin
        
        while i<=jMax and cnt<n:
            print(arr[iMax][i])
            cnt+=1
            i+=1
        else:
            iMax-=1
            i=iMax
        
        while i>=iMin and cnt<n:
            print(arr[i][jMax])
            cnt+=1
            i-=1
        else:
            jMax-=1
            i=jMax

        while i>=jMin and cnt<n:
            print(arr[iMin][i])
            cnt+=1
            i-=1
        else:
            iMin+=1
            i=iMin



#spiral_matrix([[10,20,30,41],[51,60,70,80],[90,44,22,33],[61,7,18,21]])
spiral_matrix([[10,20,30,41],
              [51,60,70,80]])
#spiral_matrix([[10],[51]])

        