# def maxWordsInString(List):
#     maxi=0
#     cnt=0
#     for sentence in List:
#         cnt=1
#         for j in sentence:
#             if j==" ":
#                 cnt+=1
#         maxi=max(maxi,cnt)
#     return maxi

def maxWordsInString(List):
    maxi=0
    cnt=0
    for sentence in List:
        cnt=sentence.count(" ")+1
        maxi=max(maxi,cnt)
    return maxi

print(maxWordsInString(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
print(maxWordsInString(["please wait", "continue to fight", "continue to win"]))
