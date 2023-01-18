class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        LENGTH = len(coins)

        #Raw Recursion
        # def helper(idx,target):
        #     if idx==0:
        #         if target%coins[0]==0:
        #             return target//coins[0]
        #         return float("inf")

        #     notTake=0+helper(idx-1,target)
        #     take=float("inf")
        #     if coins[idx]<=target:
        #         take=1+helper(idx,target-coins[idx])

        #     return min(notTake,take)
        # result=helper(LENGTH-1,amount)
        # return result if result!=float("inf") else -1

        #Recursion With Memoization
        # memo={}
        # def helper(idx,target):
        #     if (idx,target) in memo:
        #         return memo[(idx,target)]
        #     if idx==0:
        #         if target%coins[0]==0:
        #             return target//coins[0]
        #         return float("inf")

        #     notTake=0+helper(idx-1,target)
        #     take=float("inf")
        #     if coins[idx]<=target:
        #         take=1+helper(idx,target-coins[idx])

        #     memo[(idx,target)]=min(notTake,take)
        #     return memo[(idx,target)]

        # result=helper(LENGTH-1,amount)
        # return result if result!=float("inf") else -1

        #2D Dynamic Programming Solution
        dp = [[0 for _ in range(amount+1)] for _ in range(LENGTH)]

        for target in range(amount+1):
            if target % coins[0] == 0:
                dp[0][target] = target//coins[0]
            else:
                dp[0][target] = float("inf")

        for i in range(1, LENGTH):
            for target in range(amount+1):
                notTake = 0+dp[i-1][target]
                take = float("inf")
                if coins[i] <= target:
                    take = 1+dp[i][target-coins[i]]

                dp[i][target] = min(notTake, take)

        return dp[LENGTH-1][target] if dp[LENGTH-1][target] != float("inf") else -1
