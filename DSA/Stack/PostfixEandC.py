#Postfix Evaluation and conversion
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

def Postfix_EandC(Str):
    Prefix=[]
    Infix=[]
    value=[]
    for i in Str:
        if i>="0" and i<="9":
            Prefix.append(i)
            Infix.append(i)
            value.append(i)
        else:
            v2=Prefix[-1]
            Prefix.pop()
            v1=Prefix[-1]
            Prefix.pop()
            Prefix.append(i+v1+v2)

            v2=Infix[-1]
            Infix.pop()
            v1=Infix[-1]
            Infix.pop()
            Infix.append("("+v1+i+v2+")")

            v2=value[-1]
            value.pop()
            v1=value[-1]
            value.pop()
            value.append(Evaluation(v1,v2,i))

    return Prefix[-1],Infix[-1],value[-1]

print(Postfix_EandC("964-*6/3*"))
print(Postfix_EandC("563-*2/4+"))
print(Postfix_EandC("96+"))
print(Postfix_EandC("60/"))

    