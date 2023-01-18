class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        LENGTH = len(coins)

        #Raw Recursion
        # def helper(i,target):
        #     if target==0:
        #         return 1
        #     if i<0:
        #         return 0

        #     notTake=helper(i-1,target)
        #     take=0
        #     if coins[i]<=target:
        #         take=helper(i,target-coins[i])

        #     return notTake+take

        # return helper(LENGTH-1,amount)

        #Recursion With Memoization
        # memo={}
        # def memoization(i,target):
        #     if (i,target) in memo:
        #         return memo[(i,target)]
        #     if target==0:
        #         return 1
        #     if i<0:
        #         return 0

        #     notTake=memoization(i-1,target)
        #     take=0
        #     if coins[i]<=target:
        #         take=memoization(i,target-coins[i])

        #     memo[(i,target)]=notTake+take
        #     return memo[(i,target)]

        # return memoization(LENGTH-1,amount)

        #2D Dynamic Programming Solution
        dp = [[0 for _ in range(amount+1)] for _ in range(LENGTH)]

        for target in range(amount+1):
            if target % coins[0] == 0:
                dp[0][target] = 1

        for row in range(LENGTH):
            dp[row][0] = 1

        for i in range(1, LENGTH):
            for target in range(amount+1):
                notTake = dp[i-1][target]
                take = 0
                if coins[i] <= target:
                    take = dp[i][target-coins[i]]

                dp[i][target] = notTake+take

        return dp[LENGTH-1][amount]
