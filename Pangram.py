def Check_Pangram(str1):
    str1=str1.upper()
    list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    for i in str1:
        if i in list1:
            list1.remove(i)

    if list1==[]:
        return True
    else:
        return False

str1=input("Enter the string.\n")
if Check_Pangram(str1)==True:
    print("It is Pangram")
else:
    print("It is NOT Pangram")