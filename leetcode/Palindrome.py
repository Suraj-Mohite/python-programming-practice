'''
Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false

Input: x = Suraj
Output: false

Input: x = SOS
Output: True

Input: x = NitIN #shouldent be case sensitive
Output: True
'''


def Check_Palindrome(Str):
    Str=Str.upper()
    List=list(Str)
    List2=list(Str)

    for i in range(len(Str)//2):
        List[i],List[(len(Str)-1)-i]=List[(len(Str)-1)-i],List[i]
    
    if List==List2:
        return True
    else:
        return False

Str=input("Enter the string: ")
if Check_Palindrome(Str)==True:
    print("Palindrome")
else:
    print("NOT Palindrome")