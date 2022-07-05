class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [nums[i]-nums[i-1]
              for i in range(1, len(nums)) if nums[i]-nums[i-1] != 0]
        if not dp:
            return 1

        print(dp)
        count = 2
        for j in range(1, len(dp)):
            if((dp[j] < 0 and dp[j-1] > 0) or (dp[j] > 0 and dp[j-1] < 0)):
                count += 1

        return count
