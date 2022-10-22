class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = int(len(nums)/3)
        d = {}
        result = set()
        for val in nums:
            if val not in d:
                d[val] = 1
            else:
                d[val] += 1

            if(d[val] > k):
                result.add(val)

        return result
