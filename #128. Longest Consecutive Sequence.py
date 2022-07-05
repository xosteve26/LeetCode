class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        SET = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in SET:
                length = 0
                while n+length in SET:
                    length += 1

                longest = max(longest, length)

        return longest
