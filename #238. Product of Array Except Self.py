class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]*len(nums)
        pre = 1
        for i in range(len(nums)):
            l[i] = pre
            pre *= nums[i]

        post = 1
        for j in range(len(nums)-1, -1, -1):
            l[j] *= post
            post *= nums[j]

        return l
