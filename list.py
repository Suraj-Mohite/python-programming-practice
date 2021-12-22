def uniquelist(list1):
    temp=list1[0]
    l1=[]
    for i in list1:
        if i not in l1:
            l1.append(i)
    return l1
        
print(uniquelist([2,6,6,5,6,3]))


def dd(l1):
    return list(set(l1))


print(dd([2,6,6,5,6,3]))
    