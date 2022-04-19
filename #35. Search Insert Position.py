class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(target in nums):
            return nums.index(target)
        else:
            left = 0
            right = len(nums)-1
            mid = (left+right)//2
            while right >= left:
                mid = (left+right)//2

                if(nums[mid] < target):
                    left = mid+1
                elif(target < nums[mid]):
                    right = mid-1

            return left
