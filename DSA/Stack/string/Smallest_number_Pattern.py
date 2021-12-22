#fuction accepting pattern which contain only d and i in it whose max length is 8 . create smallest number by using that pattern where d means decrement and i means increament numbers should not be repeted and in between 1 to 9

def Smallest_No_Pat(Str):
    if len(Str)>8:
        result="ERROR:String size shouldent be more than 8"
        return result
    stack=[1]
    result=[]

    for j in range(len(Str)):
        if Str[j]=="d":
            stack.append(j+2)
        else:
            while len(stack)!=0:
                result.append(str(stack[-1]))
                stack.pop()
            if (j!=len(Str)-1 and Str[j+1]=="i") or (j==len(Str)-1):
                result.append(str(j+2))
            else:
                stack.append(j+2)
    else:
        if len(stack)!=0:
            while len(stack)!=0:
                result.append(str(stack[-1]))
                stack.pop()
    return "".join(result)

print(Smallest_No_Pat("d"))
print(Smallest_No_Pat("i"))
print(Smallest_No_Pat("dd"))
print(Smallest_No_Pat("didi"))
print(Smallest_No_Pat("iiid"))
print(Smallest_No_Pat("ddddidii"))
print(Smallest_No_Pat("ddddidiiddddi"))

