def permutationString(Str,ans):
    if Str=="":
        print(ans)
        return
    
    for i in range(len(Str)):
        Str1=Str[:i]+Str[i+1:]
        permutationString(Str1,ans+Str[i])

permutationString("ab","")