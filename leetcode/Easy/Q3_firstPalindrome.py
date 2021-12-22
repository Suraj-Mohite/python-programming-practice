def firstPalindrome(l1):
    res=""
    for i in l1:
        if i==i[::-1]:
            res=i
            break
    return res

print(firstPalindrome(["abc","car","ada","racecar","cool"]))
        