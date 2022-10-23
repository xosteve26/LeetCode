class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Recursion with memoization

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total//2
#         cache={}
#         def helper(i,goal):
#             if(i,goal) in cache:
#                 return cache[(i,goal)]
#             if goal==0:
#                 return True
#             if i >= len(nums):
#                 if goal == 0:
#                     return True
#                 return False

#             cache[(i,goal)]=helper(i+1,goal) or helper(i+1,goal-nums[i])

#             return cache[(i,goal)]

#         return helper(0,target)

        #DP Solution
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1, -1, -1):
            value = nums[i]
            newDP = set(dp)
            for t in dp:
                if t+value == target or value == target:
                    return True

                newDP.add(t+value)
            dp = newDP

        return True if target in dp else False
