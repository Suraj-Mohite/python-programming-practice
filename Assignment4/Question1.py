"""
1.	Declare a variable in Python and assign a string. Declare 2 more variables and store the reverse version of the upper-case version of the first string in one variable and store the reverse version of the lower-case version of the string in the second variable. Perform concatenation between those two variables and print the result.
"""

#code logic in saperate Function
def Reverse(Str):
    var1=Str[::-1].upper()
    var2=Str[::-1].lower()
    return var1+var2

var="Suraj"

print(Reverse(var))