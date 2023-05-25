class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        LENGTH=len(temperatures)
        monotonicDecreasingStack=[]
        DAILY_TEMPERATURES=[0 for _ in range(LENGTH)]

        for i in range(LENGTH):
            temperature = temperatures[i]
            while monotonicDecreasingStack and temperature > monotonicDecreasingStack[-1][0]:
                lowTemperatureIndex = monotonicDecreasingStack.pop()[1]
                DAILY_TEMPERATURES[lowTemperatureIndex] = i - lowTemperatureIndex
            monotonicDecreasingStack.append((temperature, i))

        return DAILY_TEMPERATURES

    # TC: O(N^2)


#     for temperatureIdx in range(LENGTH):
#         temperature = temperatures[temperatureIdx]
#         for nextTempIdx in range(temperatureIdx + 1, LENGTH):
#             nextTemperature = temperatures[nextTempIdx]
#             if nextTemperature > temperature:
#                 DAILY_TEMPERATURES[temperatureIdx] = nextTempIdx - temperatureIdx
#                 break
#
#     return DAILY_TEMPERATURES