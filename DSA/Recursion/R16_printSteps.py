"""def printSteps(no,ans):
    if no==0:
        print(ans,end=" ")
        return
    if no<0:
        return
    printSteps(no-1,ans+"1")
    printSteps(no-2,ans+"2")
    printSteps(no-3,ans+"3")"""

def printSteps(no,ans):
    if no==0:
        print(ans,end=" ")
        return
    if no<0:
        return
    for i in range(1,4):
        printSteps(no-i,ans+str(i))
    


printSteps(4,"")