class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        d = {}

        def helper(sum):
            if sum in d:
                return d[sum]

            if sum == target:
                return 1

            if(sum > target):
                return 0

            total = 0
            for x in nums:
                total += helper(sum+x)
                d[sum] = total

            return total
        return helper(0)
