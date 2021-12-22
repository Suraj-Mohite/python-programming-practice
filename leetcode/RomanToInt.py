def RomanToInteger(Str):
    Str=Str.upper()
    Dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    i=0
    sum=0
    while(i<len(Str)):
        if Dict[Str[i]]<Dict[Str[i+1]]:
            sum=sum+(Dict[Str[i+1]]-Dict[Str[i]])
            i+=1
        else:
            sum+=(Dict[Str[i]])
        i+=1
    return sum

print(RomanToInteger("CCXLIii"))
