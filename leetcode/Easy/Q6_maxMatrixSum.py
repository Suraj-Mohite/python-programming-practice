def maxMatrixSum(arr):
    sum=0
    cnt=0
    mini=10**9
    for i in arr:
        for j in i:
            sum+=abs(j)
            mini=min(mini,abs(j))
            if j<0:
                cnt+=1
    if cnt%2==0:
        return sum
    return sum-2*mini


print(maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))