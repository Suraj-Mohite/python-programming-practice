"""
You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

Return the number of smooth descent periods.

 

Example 1:

Input: prices = [3,2,1,4]
Output: 7
Explanation: There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.
Example 2:

Input: prices = [8,6,7,7]
Output: 4
Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.
Example 3:

Input: prices = [1]
Output: 1
Explanation: There is 1 smooth descent period: [1]

"""

# def smoothDescentPeriodOfStock(List):
#     n=len(List)
#     cnt=0
#     p1=0                            #[3,2,1,4]
#     ans=0
#     for p2 in range(n):
#         if p1==p2 or List[p2-1]-List[p2]==1:
#             cnt+=1
#         else:
#             p1=p2
#             ans+=((cnt*(cnt+1))//2)
#             cnt=1
#     ans+=((cnt*(cnt+1))//2)
#     return ans

def smoothDescentPeriodOfStock(List):
    n=len(List)
    cnt=0
    i=0
    ans=0
    while i<n:
        cnt=1
        while((i+1)<n and List[i+1]-List[i]==-1):
            cnt+=1
            i+=1
        ans+=((cnt*(cnt+1))//2)
        i+=1
    return ans


print(smoothDescentPeriodOfStock([3,2,1,4]))
print(smoothDescentPeriodOfStock([4,3,2,1,5,4,2,1]))
print(smoothDescentPeriodOfStock([8,6,7,7]))
print(smoothDescentPeriodOfStock([5]))
print(smoothDescentPeriodOfStock([]))