class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LENGTH = len(prices)

        #Raw Recursion
        # def recursion(i,canBuy,cooldown):
        #     if i==LENGTH:
        #         return 0
        #     if cooldown:
        #         return recursion(i+1,True,False)

        #     if canBuy:
        #         profit=max(
        #             recursion(i+1,False,False)-prices[i],
        #             recursion(i+1,True,False)
        #         )

        #     else:
        #         profit=max(
        #             recursion(i+1,True,True)+prices[i],
        #             recursion(i+1,False,False)
        #         )

        #     return profit

        # return recursion(0,True,False)

        #Recursion With Memoization
        memo = {}

        def memoization(i, canBuy, cooldown):
            if(i, canBuy, cooldown) in memo:
                return memo[(i, canBuy, cooldown)]
            if i == LENGTH:
                return 0
            if cooldown:
                memo[(i, canBuy, cooldown)] = memoization(i+1, True, False)
                return memo[(i, canBuy, cooldown)]

            if canBuy:
                profit = max(
                    memoization(i+1, False, False)-prices[i],
                    memoization(i+1, True, False)
                )

            else:
                profit = max(
                    memoization(i+1, True, True)+prices[i],
                    memoization(i+1, False, False)
                )
            memo[(i, canBuy, cooldown)] = profit
            return memo[(i, canBuy, cooldown)]

        return memoization(0, True, False)

        #2D Dynamic Programming Solution
        dp = [[[0 for _ in range(2)] for _ in range(2)]
              for _ in range(LENGTH+1)]

        for i in range(LENGTH):
            for canBuy in range(2):
                for cooldown in range(2):