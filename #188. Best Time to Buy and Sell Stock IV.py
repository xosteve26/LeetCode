class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        LENGTH = len(prices)
        #Raw Recursion
        # def recursion(i,canBuy,maxTransaction):
        #     if i==LENGTH or maxTransaction>=k:
        #         return 0
        #     if canBuy:
        #         profit=max(
        #             recursion(i+1,False,maxTransaction)-prices[i],
        #             recursion(i+1,True, maxTransaction)
        #         )
        #     else:
        #         profit=max(
        #             recursion(i+1,True,maxTransaction+1)+prices[i],
        #             recursion(i+1,False, maxTransaction)
        #         )
        #     return profit

        # return recursion(0,True,0)

        #Recursion with Memoization
        # memo={}
        # def recursion(i,canBuy,maxTransaction):
        #     if (i,canBuy,maxTransaction) in memo:
        #         return memo[(i,canBuy,maxTransaction)]
        #     if i==LENGTH or maxTransaction>=k:
        #         return 0
        #     if canBuy:
        #         profit=max(
        #             recursion(i+1,False,maxTransaction)-prices[i],
        #             recursion(i+1,True, maxTransaction)
        #         )
        #     else:
        #         profit=max(
        #             recursion(i+1,True,maxTransaction+1)+prices[i],
        #             recursion(i+1,False, maxTransaction)
        #         )
        #     memo[(i,canBuy,maxTransaction)]=profit
        #     return memo[(i,canBuy,maxTransaction)]

        # return recursion(0,True,0)

        #2D Dynamic Programming Solution
        dp = [[[0 for _ in range(k+1)] for _ in range(2)]
              for _ in range(LENGTH+1)]

        for i in range(LENGTH-1, -1, -1):
            for canBuy in range(2):
                for limit in range(1, k+1):
                    if canBuy:
                        profit = max(
                            dp[i+1][0][limit]-prices[i],
                            dp[i-1][1][limit]
                        )
                    else:
                        profit = max(
                            dp[i+1][1][limit-1]+prices[i],
                            dp[i+1][0][limit]
                        )
                    dp[i][canBuy][limit] = profit
        print(dp[0])
        return dp[0][1][2]
