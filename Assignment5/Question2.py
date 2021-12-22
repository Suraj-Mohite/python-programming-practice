"""
Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
"""

def Sum_Numbers(No):
    if No<0:
        return "Error:404 (Negative Number)"
    sum=0
    for i in range(1,No+1):
        if i%3==0 or i%5==0:
            sum=sum+i
    return sum

No=int(input("Enter the Number.\n"))
print(f"Sum of all numbers from 1 to {No} is of multiple of 3 and 5 numbers is : {Sum_Numbers(No)}")