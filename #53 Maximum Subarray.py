
def maxSubArray(nums) -> int:
    maxSum = nums[0]
    sum = 0
    for i in nums:
        if(i > sum+i):
            sum = 0
        sum += i
        maxSum = max(sum, maxSum)
    return maxSum
