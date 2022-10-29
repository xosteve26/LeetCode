class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]

        if len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]

        def findPivot():
            start, end = 0, len(nums)-1

            while start <= end:
                mid = (start+end)//2
                if mid > 0 and mid < end and nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                    return mid
                if mid < end and nums[mid] > nums[mid+1]:
                    return mid+1
                if nums[0] > nums[mid]:
                    end = mid-1
                else:
                    start = mid+1

            return -1

        if findPivot() == -1:
            return nums[0]
        else:
            return nums[findPivot()]
