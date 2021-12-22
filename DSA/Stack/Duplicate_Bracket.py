# Check whether entered equetion contains duplicate brackets or not. if yes then return true else false
#Assumption Equation is balanced

def Duplicate_Bracket(Str):
    stack=[]
    Result=False
    for i in Str:
        if i!=")":
            stack.append(i)
        else:
            if stack[-1]=="(":
                Result=True
                break
            while stack[-1]!="(":
                stack.pop()
            stack.pop()
    return Result

print(Duplicate_Bracket("((6+9)+9*((5/7)))"))
print(Duplicate_Bracket("((6+9)+9*(5/7))"))