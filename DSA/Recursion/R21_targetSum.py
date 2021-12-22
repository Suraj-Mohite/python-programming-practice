# def targetSum(arr,index,ans,sum,target):
#     if sum==target:
#         print(ans)
#         return
#     if sum>target or index==len(arr):
#         return
#     ans1=[]
#     for i in ans:
#         ans1.append(i)
#     ans1.append(arr[index])
#     targetSum(arr,index+1,ans1,sum+arr[index],target)
#     targetSum(arr,index+1,ans,sum,target)

def targetSum(arr,index,ans,target):
    if sum(ans)==target:
        print(ans)
        return
    if sum(ans)>target or index==len(arr):
        return
    ans.append(arr[index])
    targetSum(arr,index+1,ans,target)
    ans.pop()
    targetSum(arr,index+1,ans,target)


# targetSum([10,20,30,40,50,60],0,[],0,60)
targetSum([10,20,30,40,50,60],0,[],30)
# targetSum([10,20,30],0,[],0,30)
# targetSum([30,20,10],0,[],0,30)
# targetSum([30,20,10],0,[],0,300)
# targetSum([],0,[],0,3)