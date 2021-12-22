#Accept the string And pattern and return the index number of that pattern present in string. and count of that pattern present in string if not present then return -1

def Find_Pattern(Str,Pat):
    List=[]
    result=[]
    cnt=0
    i,j=0,0
    while j<len(Str):
        List.append(Str[j])
        if j-i+1<len(Pat):
            j+=1
        elif j-i+1==len(Pat):
            if "".join(List)==Pat:
                result.append(i)
                cnt+=1
            List.remove(List[0])
            j+=1
            i+=1
    if len(result)==0:
        return -1,cnt
    return result,cnt


print(Find_Pattern("ababaabababa","aba"))
print(Find_Pattern("ababaabababa","av"))
print(Find_Pattern("ababaabababa","aa"))
            