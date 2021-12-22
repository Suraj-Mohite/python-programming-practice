def getSubsequence(String):
    if String=="":
        return [""]
    result=getSubsequence(String[1:])
    ans=[]
    for i in result:
        ans.append(String[0]+i)
        ans.append(i)
    
    return ans

print(getSubsequence("suraj"))
