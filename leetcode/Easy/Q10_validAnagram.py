# #case sensitive
# def validAnagram(str1,str2):
#     dict1={}
#     dict2={}
#     for i in str1:
#         dict1[i]=dict1.get(i,0)+1

#     for j in str2:
#         dict2[j]=dict2.get(j,0)+1
    
#     if dict1==dict2:
#         return True
#     return False

#case insensitive
# def validAnagram(str1,str2):
#     if len(str1)!=len(str2):
#         return False
        
#     dict1={}
#     dict2={}
#     for i in str1:
#         i=i.lower()
#         dict1[i]=dict1.get(i,0)+1

#     for j in str2:
#         j=j.lower()
#         dict2[j]=dict2.get(j,0)+1
    
#     if dict1==dict2:
#         return True
#     return False

def validAnagram(str1,str2):
    if len(str1)!=len(str2):
        return False

    dict1={}
    dict2={}
    for i in range(len(str1)):
        dict1[str1[i]]=dict1.get(str1[i],0)+1
        dict2[str2[i]]=dict2.get(str2[i],0)+1

    if dict1==dict2:
        return True
    return False
    
print(validAnagram("suraj","suraj"))
print(validAnagram("surajj","suraj"))
print(validAnagram("surdj","suraj"))