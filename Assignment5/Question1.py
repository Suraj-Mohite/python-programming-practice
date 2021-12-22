"""Write a program that asks the user for a number n and prints the sum of the numbers 1 to n ."""

def Sum_Numbers(No):
    if No<0:
        return "Error:404 (Negative Number)"
    sum=0
    for i in range(1,No+1):
        sum=sum+i
    return sum

No=int(input("Enter the Number.\n"))
print(f"Sum of all numbers from 1 to {No} is : {Sum_Numbers(No)}")