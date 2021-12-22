#Time Limit Exceeded errror in this logic

def smoothDescentPeriodOfStock(List):
    n=len(List)
    cnt=0
    for i in range(n):
        cnt+=1
        for j in range(i+1,n):
            if List[j-1]-List[j]==1:
                cnt+=1
            else:
                break
    
    return cnt


print(smoothDescentPeriodOfStock([3,2,1,4]))
print(smoothDescentPeriodOfStock([4,3,2,1]))
print(smoothDescentPeriodOfStock([8,6,7,7]))
print(smoothDescentPeriodOfStock([5]))