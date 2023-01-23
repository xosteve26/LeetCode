class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LENGTH = len(prices)
        maxProfit = 0

        #Raw Recursion
        # def recursion(i,canBuy,limit):
        #     if i==LENGTH or limit>=2:
        #         return 0

        #     if canBuy:
        #         profit=max(
        #                     recursion(i+1,False,limit)-prices[i],
        #                     recursion(i+1,True,limit)
        #                 )
        #     else:
        #         profit=max(
        #                     prices[i]+recursion(i+1,True,limit+1),
        #                     recursion(i+1,False,limit)
        #                 )

        #     return profit

        # maxProfit=recursion(0,True,0)
        # return maxProfit

        #Recursion With Memoization
        # memo={}
        # def recursion(i,canBuy,limit):
        #     if (i,canBuy,limit) in memo:
        #         return memo[(i,canBuy,limit)]

        #     if i==LENGTH or limit>=2:
        #         return 0

        #     if canBuy:
        #         profit=max(
        #                     recursion(i+1,False,limit)-prices[i],
        #                     recursion(i+1,True,limit)
        #                 )
        #     else:
        #         profit=max(
        #                     prices[i]+recursion(i+1,True,limit+1),
        #                     recursion(i+1,False,limit)
        #                 )

        #     memo[(i,canBuy,limit)]=profit
        #     return memo[(i,canBuy,limit)]

        # maxProfit=recursion(0,True,0)
        # return maxProfit

        #2D Dynamic Programming Solution
        dp = [[[0 for _ in range(3)] for _ in range(2)]
              for _ in range(LENGTH+1)]

        for i in range(LENGTH-1, -1, -1):
            for canBuy in range(2):
                for limit in range(1, 3):
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
