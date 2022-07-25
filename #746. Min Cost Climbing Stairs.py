class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for k in range(2, len(cost)):
            dp[k] = min(dp[k-1], dp[k-2])+cost[k]

        return min(dp[-1], dp[-2])
