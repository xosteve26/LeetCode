class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        LENGTH = len(temperatures)
        if LENGTH == 1:
            return [0]

        monotonicDecreasingStack = []
        dailyTemperatures = [0 for _ in range(LENGTH)]
        for i in range(LENGTH):
            temp = temperatures[i]

            while monotonicDecreasingStack and temp > monotonicDecreasingStack[-1][0]:
                val, idx = monotonicDecreasingStack.pop()
                dailyTemperatures[idx] = i-idx
            monotonicDecreasingStack.append((temp, i))

        return dailyTemperatures
