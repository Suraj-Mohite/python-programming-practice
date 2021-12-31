def mostFrequentElement(arr):
    map={}
    for i in arr:
        map[i]=map.get(i,0)+1
    k=list(map.keys())
    v=list(map.values())
    print(k[v.index(max(v))])

mostFrequentElement([2,7,8,1,1,6,7,4,4,4,5,6,1,2,3,4,5,7,5,6,4,9,88,45,6,3,77])