def Infix_evaluation(Str):
    stack1=[]
    stack2=[]
    no1=0
    no2=0
    ans=0

    try:
        for i in Str:
            if i>="0" and i<="9":
                stack1.append(i)
            elif i!=")":
                if len(stack2)!=0 and ((i=="+" or i=="-") and stack2[-1]!="(") :
                    no2=float(stack1[-1])
                    stack1.pop()
                    no1=float(stack1[-1])
                    stack1.pop()
                    if stack2[-1]=="-":
                        ans=no1-no2
                    elif stack2[-1]=="+":
                        ans=no1+no2
                    elif stack2[-1]=="*":
                        ans=no1*no2
                    elif stack2[-1]=="/":
                        ans=no1/no2
                    stack1.append(ans)
                    stack2.pop()
                elif len(stack2)!=0 and ((i=="*" or i=="/") and (stack2[-1]=="*" or stack2[-1]=="/")) :
                    no2=float(stack1[-1])
                    stack1.pop()
                    no1=float(stack1[-1])
                    stack1.pop()
                    if stack2[-1]=="*":
                        ans=no1*no2
                    elif stack2[-1]=="/":
                        ans=no1/no2
                    stack1.append(ans)
                    stack2.pop()
                stack2.append(i)
            elif i==")":
                while stack2[-1]!="(":
                    no2=float(stack1[-1])
                    stack1.pop()
                    no1=float(stack1[-1])
                    stack1.pop()
                    if stack2[-1]=="-":
                        ans=no1-no2
                    elif stack2[-1]=="+":
                        ans=no1+no2
                    elif stack2[-1]=="*":
                        ans=no1*no2
                    elif stack2[-1]=="/":
                        ans=no1/no2
                    stack1.append(ans)
                    stack2.pop()
                stack2.pop()
        else:
            while len(stack2)!=0:
                no2=float(stack1[-1])
                stack1.pop()
                no1=float(stack1[-1])
                stack1.pop()
                if stack2[-1]=="-":
                    ans=no1-no2
                elif stack2[-1]=="+":
                    ans=no1+no2
                elif stack2[-1]=="*":
                    ans=no1*no2
                elif stack2[-1]=="/":
                    ans=no1/no2
                stack1.append(ans)
                stack2.pop()
    except ZeroDivisionError as e:
        return("ERROR:Cant Devide by 0")
    return ans
            
print(Infix_evaluation("(9+5)-4"))
print(Infix_evaluation("2+(5-3*6/2)"))
print(Infix_evaluation("2+(5-3)*6/2"))
print(Infix_evaluation("2*(5+7)/0"))
print(Infix_evaluation("2+2+5+4+5+8+9+8-9"))


        