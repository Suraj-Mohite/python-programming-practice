def Balanced_Bracket(Str):
    stack=[]               #((a+b)+(c+d))
    Result=False
    for i in Str:
        if i!=")" and i!="]" and i!="}":
            stack.append(i)
        elif i==")":
            while len(stack)!=0 and stack[-1]!="(" and stack[-1]!="[" and stack[-1]!="{":
                stack.pop()
            if len(stack)==0:
                Result=True
                break
            elif stack[-1]=="(":
                stack.pop()
            elif stack[-1]=="[" or stack[-1]=="{":
                Result=True
                break
        elif i=="]":
            while len(stack)!=0 and stack[-1]!="(" and stack[-1]!="[" and stack[-1]!="{":
                stack.pop()
            if len(stack)==0:
                Result=True
                break
            elif stack[-1]=="[":
                stack.pop()
            elif stack[-1]=="(" or stack[-1]=="{":
                Result=True
                break
        elif i=="}":
            while len(stack)!=0 and stack[-1]!="(" and stack[-1]!="[" and stack[-1]!="{":
                stack.pop()
            if len(stack)==0:
                Result=True
                break
            elif stack[-1]=="{":
                stack.pop()
            elif stack[-1]=="[" or stack[-1]=="(":
                Result=True
                break
    else:
        if len(stack)==1 and (stack[-1]=="+" or stack[-1]=="-" or stack[-1]=="*" or stack[-1]=="/"):
            Result=False
        elif len(stack)!=0:
            Result=True
    return Result

print(Balanced_Bracket("(a+b)+(c+d)"))
print(Balanced_Bracket("(a+b)/(c+d)"))
print(Balanced_Bracket("((a+b)/(c+d))"))
print(Balanced_Bracket("[(a+b)+(c+d))"))
print(Balanced_Bracket("[(a+b)+(c+d)]"))
print(Balanced_Bracket("[(a+b)+(c+d)"))
print(Balanced_Bracket("(a+b)+(c+d)]"))
print(Balanced_Bracket("{[k+(a+b)+(c+d)}]"))
