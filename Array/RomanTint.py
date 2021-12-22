#Accept roman number and convert it into integer "MDCXCV"

def RomanToInt(Str):
    ans=0
    i=0
    Dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    if len(Str)==1:
        return Dict[Str[0]]
    while i<(len(Str)-1):
        if Dict[Str[i+1]]<=Dict[Str[i]]:
            ans+=Dict[Str[i]]
            if i+1==len(Str)-1:
                ans+=Dict[Str[i+1]]
        else:
            ans+=(Dict[Str[i+1]]-Dict[Str[i]])
            i+=1
            if i+1==len(Str)-1:
                ans+=Dict[Str[i+1]]
        i+=1
    return ans

print(RomanToInt("XXV"))            
print(RomanToInt("XXIII"))            
print(RomanToInt("XIX"))            
print(RomanToInt("III"))            
print(RomanToInt("IV"))            
print(RomanToInt("IX"))            
print(RomanToInt("LVIII"))            
print(RomanToInt("MCMXCIV"))            
print(RomanToInt("M"))            
print(RomanToInt("CM"))            
print(RomanToInt("CD"))            
print(RomanToInt("D"))            
print(RomanToInt("I"))            
print(RomanToInt("MCMXCVII"))            
print(RomanToInt("MCMXCIV"))            

