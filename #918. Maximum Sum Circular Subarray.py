class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        SUM = sum(nums)

        def kdAlgoMAX():
            currSum = 0
            maxSum = float("-inf")

            for i in range(LENGTH):
                if currSum < 0:
                    currSum = 0
                currSum += nums[i]
                maxSum = max(maxSum, currSum)
            return maxSum

        def kdAlgoMIN():
            currSum = 0
            minSum = float("inf")
            maximumElement = float("-inf")
            negCounter = 0
            for i in range(LENGTH):
                if nums[i] < 0:
                    negCounter += 1
                    maximumElement = max(maximumElement, nums[i])
                if currSum > 0:
                    currSum = 0
                currSum += nums[i]
                minSum = min(minSum, currSum)

            if negCounter != LENGTH:
                return minSum, False
            else:
                return maximumElement, True

        LENGTH = len(nums)
        maxSubArray = kdAlgoMAX()
        minSubArray, isAllNegative = kdAlgoMIN()

        result = max(maxSubArray, SUM-minSubArray)
        return result if not isAllNegative else minSubArray
