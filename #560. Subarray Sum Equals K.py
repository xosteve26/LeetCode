class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preFix = defaultdict(int)
        preFix[0] = 1
        rollingSum = 0
        subArraysEqualToK = 0
        for val in nums:
            rollingSum += val

            if rollingSum-k in preFix:
                subArraysEqualToK += preFix[rollingSum-k]

            preFix[rollingSum] += 1

        return subArraysEqualToK
