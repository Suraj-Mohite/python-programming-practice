# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1

#SOLUTION 1

def singleNumber(nums):
    temp=[]
    for i in nums:
        if i in temp:
            temp.remove(i)
        else:
            temp.append(i)
    return temp[0]

# print(singleNumber([4,1,2,1,2]))

#SOLUTION 2

def singleNumber1(nums):
    temp={}
    res="No single number"
    for num in nums:
        temp[num]=temp.get(num,0)+1
    
    for key,val in temp.items():
        if val==1:
            res=key
            break
    return res

# print(singleNumber1([4,1,2,1,2]))

#SOLUTION 3

def singleNumber3(nums):
    return 2*(sum(set(nums)))-sum(nums)

# print(singleNumber3([4,1,2,1,2]))

#SOLUTION 4

def singleNumber4(nums):
    res=0

    for num in nums:
        res=res^num
    return res

# print(singleNumber4([4,1,2,1,2]))


#solution 5
from functools import reduce
def singleNumber5(nums):
    return reduce(lambda x,y:x^y,nums)

print(singleNumber5([4,1,2,1,2]))