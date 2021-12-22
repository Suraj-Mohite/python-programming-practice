def uni(List1):
    Dict={}
    l1=[]
    for i in List1:
        Dict[i]=Dict.get(i,0)+1    #creating map
    print(Dict)
    for i in List1:
        if Dict[i]==1:
            l1.append(i)
    return l1

def Set1(List1):
    l1=[]
    for i in List1:
        if i not in l1:
            l1.append(i)
    return l1

print(uni([1,1,1,2,3,4,4,5,5,6]))
print(Set1([1,1,1,2,3,4,4,5,5,6]))