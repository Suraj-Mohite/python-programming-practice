def firstNonRepeatingElement(arr):
    ans=[]
    for i in arr:
        if i not in ans:
            ans.append(i)
        else:
            ans.remove(i)
    if len(ans)!=0:
        return ans[0]
    return None

def firstNonRepeatingElement1(arr):
    map={}
    for i in arr:
        map[i]=map.get(i,0)+1
    print(map)
    for i in map:
        if map[i]==1:
            return i
    return -1

# print(firstNonRepeatingElement([-1,2,-1,3,2]))
print(firstNonRepeatingElement1([-1,2,-1,3,2]))
# print(firstNonRepeatingElement([9,4,9,6,6,7,7,4]))
# print(firstNonRepeatingElement([9,4,9,6,7,4]))
print(firstNonRepeatingElement1([9,4,9,6,7,4]))