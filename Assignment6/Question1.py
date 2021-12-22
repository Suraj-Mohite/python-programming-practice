'''
1. Complete the solution so that the function will break up camel casing, using a space between words.

Example
solution("camelCasing")  ==>  "camel Casing"
'''


def Space_Saperate(Str):
    if(Str==""):
        return -1
    Str_Temp=""
    for letter in Str:
        if(letter==" "):
            continue        #this line is to skip extra spaces
        if letter>='A' and letter<='Z':
            Str_Temp+=" "
        Str_Temp+=letter
    return Str_Temp.lstrip() #lstrip will ignore initial space


Str=input("Enter the sentence: ")
Output=Space_Saperate(Str)

if Output==-1:
    print("ERROR:Please Enter the Valid Input")
else:
    print(Output)