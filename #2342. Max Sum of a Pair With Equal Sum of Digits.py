class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {}
        maximum = -1

        def digit(n):
            sum = 0
            while n:
                sum += (n % 10)
                n = n//10
            return sum

        for i in nums:
            d[digit(i)] = []

        for j in nums:
            d[digit(j)].append(j)

        maximum = -1
        for i in d:
            sRt = sorted(d[i])
            if(len(sRt) > 1):
                maximum = max(maximum, sRt[-1]+sRt[-2])

        return maximum
