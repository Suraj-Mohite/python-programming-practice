
def printKeypadComb(String,ans):
    if String=="":
        print(ans,end=" ")
        return
    dict1={0:'abc',1:'def',2:'ghij',3:'klmno',4:'pqrst',5:'uvw'}
    for i in dict1[int(String[0])]:
        printKeypadComb(String[1:],ans+i)
    
printKeypadComb("543210","")
