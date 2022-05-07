class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = {}
        for i in nums:
            if i not in l:
                l[i] = 0
            else:
                return i
