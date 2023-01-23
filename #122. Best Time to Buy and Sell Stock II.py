class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LENGTH = len(prices)
        maxProfit = 0

        #Raw Recursion
        # def recursion(i,canBuy):
        #     if i==LENGTH:
        #         return 0

        #     if canBuy:
        #         profit=max(
        #                     recursion(i+1,False)-prices[i],
        #                     recursion(i+1,True)
        #                 )
        #     else:
        #         profit=max(
        #                     prices[i]+recursion(i+1,True),
        #                     recursion(i+1,False)
        #                 )

        #     return profit

        # maxProfit=recursion(0,True)
        # return maxProfit

        #Recursion With Memoization
        # memo={}
        # def recursion(i,canBuy):
        #     if (i,canBuy) in memo:
        #         return memo[(i,canBuy)]

        #     if i==LENGTH:
        #         return 0

        #     if canBuy:
        #         profit=max(
        #                     recursion(i+1,False)-prices[i],
        #                     recursion(i+1,True)
        #                 )
        #     else:
        #         profit=max(
        #                     prices[i]+recursion(i+1,True),
        #                     recursion(i+1,False)
        #                 )
        #     memo[(i,canBuy)]=profit
        #     return memo[(i,canBuy)]

        # maxProfit=recursion(0,True)
        # return maxProfit

        #2D Dynamic Programming Solution
        dp = [[0 for _ in range(2)] for _ in range(LENGTH+1)]

        for i in range(LENGTH-1, -1, -1):
            for canBuy in range(2):
                profit = 0
                if canBuy:
                    profit = max(
                        dp[i+1][0]-prices[i],
                        dp[i+1][1]
                    )
                else:
                    profit = max(
                        prices[i]+dp[i+1][1],
                        dp[i+1][0]
                    )
                dp[i][canBuy] = profit

        return dp[0][1]
