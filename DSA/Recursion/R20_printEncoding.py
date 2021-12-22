def Dictonary():
    Dict={}
    for i in range(1,27):
        Dict[i]=chr((ord('a')-1)+i)
    return(Dict)

def printEncoding(Str,ans):
    if Str=="":
        print(ans)
        return
    Dict=Dictonary()
    if Str[0]!='0':
        printEncoding(Str[1:],ans+Dict[int(Str[0])])
        
    if Str[0]!='0' and len(Str)>=2 and int(Str[:2])<=26:
        printEncoding(Str[2:],ans+Dict[int(Str[:2])])

# printEncoding("123","")
# printEncoding("101","")
# printEncoding("103","")
# printEncoding("303","")
# printEncoding("0312","")
# printEncoding("993","")
# printEncoding("72","")
# printEncoding("7654321","")
printEncoding("1234567","")