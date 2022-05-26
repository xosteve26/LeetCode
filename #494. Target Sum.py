class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def helper(index, total):
            if(index == len(nums)):
                return 1 if total == target else 0

            if((index, total) in dp):
                return dp[(index, total)]

            v1 = helper(index+1, total+nums[index])
            v2 = helper(index+1, total-nums[index])

            dp[(index, total)] = v1+v2

            return dp[(index, total)]

        return helper(0, 0)
