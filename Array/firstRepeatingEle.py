def firstRepeatingElement(arr):
    ans={}
    for i in arr:
        ans[i]=ans.get(i,0)+1
    
    for i in ans:
        if ans[i]==2:
            return i
    return -1

print(firstRepeatingElement([10, 5, 3, 4, 3, 5, 6]))
print(firstRepeatingElement([6, 10, 5, 9, 120, 4]))