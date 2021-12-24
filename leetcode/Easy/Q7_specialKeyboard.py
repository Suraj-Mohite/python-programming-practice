#Leetcode question Link : https://leetcode.com/contest/biweekly-contest-59/problems/minimum-time-to-type-word-using-special-typewriter/

def key(prev,letter):
    a=abs(ord(prev)-ord(letter))
    b=26-a
    return min(a,b)

def specialKeyboard(String):
    prev='a'
    step=0
    for letter in String:
        step+=(key(prev,letter)+1)
        prev=letter
    return step

print(specialKeyboard("abc"))
print(specialKeyboard("bza"))
print(specialKeyboard("zjpc"))

