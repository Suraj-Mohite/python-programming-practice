#Accept two strings from user and check it is Anagram or Not
#Eg. pool=polo --> True, Add=dad-->true, game=map-->false

def Check_Anagram(str1,str2):
    str1=(str1.strip()).upper()  #to handle case sensitive and extra spaces
    str2=(str2.strip()).upper()  #to handle case sensitive and extra spaces

    List1=list(str1)
    for i in str2:
        if i in List1:
            List1.remove(i)
        else:
            List1.append(i)
    
    if List1==[]:
        return True
    else:
        return False
    
str1=input("Enter first String :")
str2=input("Enter Second String :")

if (Check_Anagram(str1,str2))==True:
    print("\nEntered Strings are Anagram.\n")
else:
    print("\nEntered Strings are NOT Anagram.\n")
