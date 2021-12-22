# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

#Solutin1

def reverseString1(s):
    return s[::-1]

ans=reverseString1(["h","e","l","l","o"])

print(ans)

#Solution 2

def reverseString2(s):
    l=len(s)

    for i in range(l//2):
        # print(s[~i])
        # s[i],s[-(i+1)]=s[-(i+1)],s[i]
        s[i],s[~i]=s[~i],s[i]
    return s

print(reverseString2(["h","e","l","l","o","w"]))

#Solution3

def reverseStringRecursion(s):
    l=len(s)
    if l<2:
        return s
    return reverseStringRecursion(s[l//2:])+reverseStringRecursion(s[:l//2])

print(reverseStringRecursion(["h","e","l","l","o","o"]))

