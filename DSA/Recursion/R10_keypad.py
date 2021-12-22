dict1={0:'abc',1:'def',2:'ghij',3:'klmno',4:'pqrst',5:'uvw'}

def keyPad(no):
    if no=="":
        arr=[]
        arr.append("")
        return arr

    result=keyPad(no[1:])
    arr1=[]
    for i in dict1[int(no[0])]:
        for j in result:
            arr1.append(i+j)
    return arr1

print(keyPad('015'))
# print(keyPad('543'))
# print(keyPad('3'))
# print(keyPad(''))
# print(keyPad('5432105432'))

