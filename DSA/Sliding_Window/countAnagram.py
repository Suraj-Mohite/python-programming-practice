def search(Str,pat):
    count=0
    i=0
    j=0
    dict1={}
    for item in pat:
        dict1[item]=dict1.get(item,0)+1
    dict2={}
    while j<len(Str):
        dict2[Str[j]]=dict2.get(Str[j],0)+1
        print(dict2)
        if j-i+1<len(pat):
            j+=1
        elif j-i+1==len(pat):
            if dict2==dict1:
                count+=1
            j+=1
            if dict2[Str[i]]==1:
                del dict2[Str[i]]
            else:
                dict2[Str[i]]=dict2.get(Str[i],0)-1
            i+=1
    return count

print(search("forxxorfxdofr","for"))
print(search("aabaabaa","aaba"))


