def Preferance(operator):
    if operator=="+" or operator=="-":
        return 1
    if operator=="*" or operator=="/":
        return 2

"""def Postfix(v1,v2,operator):
    return v1+v2+operator

def Prefix(v1,v2,operator):
    return operator+v1+v2"""
        

def infix_Conversion(Str):
    pre=[]                  #"5*(6-3)/5+4"
    post=[]
    operator=[]
    v1=""
    v2=""
    for i in Str:
        if i>="0" and i<="9":
            pre.append(i)
            post.append(i)
        elif i!=")":
            if len(operator)!=0 and i!="(" and operator[-1]!="(" and Preferance(operator[-1])>=Preferance(i):
                v2=pre[-1]
                pre.pop()
                v1=pre[-1]
                pre.pop()
                pre.append(operator[-1]+v1+v2)

                v2=post[-1]
                post.pop()
                v1=post[-1]
                post.pop()
                post.append(v1+v2+operator[-1])

                operator.pop()

            operator.append(i)
        elif i==")":
            while operator[-1]!="(":
                v2=pre[-1]
                pre.pop()
                v1=pre[-1]
                pre.pop()
                pre.append(operator[-1]+v1+v2)

                v2=post[-1]
                post.pop()
                v1=post[-1]
                post.pop()
                post.append(v1+v2+operator[-1])

                operator.pop()
            operator.pop()
    else:
        if len(operator)!=0:
            while len(operator)!=0:
                v2=pre[-1]
                pre.pop()
                v1=pre[-1]
                pre.pop()
                pre.append(operator[-1]+v1+v2)

                v2=post[-1]
                post.pop()
                v1=post[-1]
                post.pop()
                post.append(v1+v2+operator[-1])

                operator.pop()
    
    return pre[-1],post[-1]

print(infix_Conversion("5*(6-3)/5+4"))
print(infix_Conversion("5-6"))
print(infix_Conversion("(5+6)"))
print(infix_Conversion("(((9*(6-4))/6)*3)"))



