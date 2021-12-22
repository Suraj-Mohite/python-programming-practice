# def addSpaceToString(s,l1):
#     res=""
#     prev=0
#     for i in l1:
        
#         res+=(s[prev:i]+" ")
#         prev=i
#     return res

def addSpaceToString(s,l1):
    res=""
    j=0
    for i in range(len(s)):
        if j<len(l1) and l1[j]==i:
            res+=" "+s[i]
            j+=1
        else:
            res+=s[i]

    return res

print(addSpaceToString("LeetcodeHelpsMeLearn",[8,13,15]))
print(addSpaceToString("icodeinpython",[1,5,7,9]))
print(addSpaceToString("spacing",[0,1,2,3,4,5,6]))



