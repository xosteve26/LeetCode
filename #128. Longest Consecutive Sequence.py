class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Identify the starting of evey sequence

        seq = set(nums)
        longest = 0
        for val in nums:
            if val-1 not in seq:
                cSequence = 0

                while (val+cSequence) in seq:
                    cSequence += 1

                longest = max(longest, cSequence)

        return longest
