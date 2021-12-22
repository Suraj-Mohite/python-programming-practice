#prefix Evaluation and conversion

def Evaluation(v1,v2,operator):
    try:
        v1=float(v1)
        v2=float(v2)
        if operator=="+":
            return v1+v2
        if operator=="-":
            return v1-v2
        if operator=="*":
            return v1*v2
        if operator=="/":
            return v1/v2
    except ZeroDivisionError as e:
        return("ERROR: Cant devide Number by 0")

def PrefixEandC(Str):
    Postfix=[]
    Infix=[]
    value=[]

    for i in Str[::-1]:
        if i>="0" and i<="9":
            Postfix.append(i)
            Infix.append(i)
            value.append(i)
        else:
            v1=Postfix[-1]
            Postfix.pop()
            v2=Postfix[-1]
            Postfix.pop()
            Postfix.append(v1+v2+i)

            v1=Infix[-1]
            Infix.pop()
            v2=Infix[-1]
            Infix.pop()
            Infix.append("("+v1+i+v2+")")

            v1=value[-1]
            value.pop()
            v2=value[-1]
            value.pop()
            value.append(Evaluation(v1,v2,i))

    return Postfix[-1],Infix[-1],value[-1]

print(PrefixEandC("*/*9-6463"))
print(PrefixEandC("+/*5-6324"))
print(PrefixEandC("+96"))
print(PrefixEandC("/96"))
print(PrefixEandC("/90"))


