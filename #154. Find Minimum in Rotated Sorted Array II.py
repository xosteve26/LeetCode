class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]

        if len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]

        if nums[0] < nums[-1]:
            return nums[0]

        def findPivot():
            start, end = 0, len(nums)-1

            while start <= end:
                mid = (start+end)//2
                if nums[mid] < nums[end]:
                    end = mid
                elif(nums[mid] > nums[end]):
                    start = mid+1
                else:
                    end -= 1

            return min(nums[start], nums[end])

        return findPivot()
