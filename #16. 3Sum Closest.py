class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = float("inf")
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            while l < r:
                sum = nums[l] + nums[r] + nums[i]
                if(sum == target):
                    return sum

                if (abs(target - sum) < abs(target-result)):
                    result = sum

                if(sum > target):
                    r -= 1
                else:
                    l += 1

        return result
