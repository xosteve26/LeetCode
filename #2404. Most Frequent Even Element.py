class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        majFreq = 0
        majEle = float("-inf")
        for val in nums:
            if val % 2 == 0:
                if(val not in d):
                    d[val] = 1
                else:
                    d[val] += 1

                if d[val] > majFreq:
                    majFreq = d[val]
                    majEle = val
                elif d[val] == majFreq:
                    majEle = min(majEle, val)

        return majEle if majEle != float("-inf") else -1
