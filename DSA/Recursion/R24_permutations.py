#this function will print all permutations

# def permutation(Str,ans):
#     if(Str==""):
#         print(ans)
#         return
#     for i in range(len(Str)):
#         permutation(Str[:i]+Str[i+1:],ans+Str[i])

# permutation("aab","")

# this code will give list of all permutations with duplicates

def permutations(Str):
    if(Str==""):
        return [""]
    arr=[]
    for i in range(len(Str)):
        l=permutations(Str[:i]+Str[i+1:])
        for ele in l:
            arr.append(Str[i]+ele)
    return arr

print(permutations("aab"))

# this function will give list of all permutations without duplicates

# def getpermutations(Str):
#     if(Str==""):
#         return[""]
#     arr=[]
#     for i in range(len(Str)):
#         l=getpermutations(Str[:i]+Str[i+1:])
#         for ele in l:
#             arr.append(Str[i]+ele)
    
#     return list(set(arr))

# ans=[]
# def getpermutationsX(Str):
#     if(Str==""):
#         return[""]
#     arr=[]
#     for i in range(len(Str)):
#         l=getpermutationsX(Str[:i]+Str[i+1:])
#         for ele in l:
#             arr.append(Str[i]+ele)
    
#     return list(set(arr))

# print(getpermutationsX("aab"))
# print(getpermutations("a"))
# print(getpermutations("ab"))