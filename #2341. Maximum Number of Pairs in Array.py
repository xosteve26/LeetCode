class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        length = len(nums)
        count = 0
        left = length
        i = 0
        j = 1
        while i < j and i < length and j < length:
            if nums[i] == nums[j]:
                print(nums[j], j)
                nums.pop(i)
                nums.pop(j-1)
                i = 0
                j = 1
                length = len(nums)
                count += 1
                left = length
            else:
                j += 1
            if j == len(nums):

                i += 1
                j = i+1

        return [count, left]
