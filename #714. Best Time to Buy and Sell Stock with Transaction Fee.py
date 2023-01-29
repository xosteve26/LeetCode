class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        LENGTH = len(prices)

        #Raw Recursion
        # def recursion(i,canBuy):
        #     if i==LENGTH:
        #         return 0

        #     if canBuy:
        #         profit=max(
        #             recursion(i+1,False)-prices[i],
        #             recursion(i+1,True)
        #         )
        #     else:
        #         profit=max(
        #             recursion(i+1,True)+prices[i]-fee,
        #             recursion(i+1,False)
        #         )
        #     return profit

        # return recursion(0,True)

        #Recursion with Memoization
        memo = {}

        def memoization(i, canBuy):
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]
            if i == LENGTH:
                return 0

            if canBuy:
                profit = max(
                    memoization(i+1, False)-prices[i],
                    memoization(i+1, True)
                )
            else:
                profit = max(
                    memoization(i+1, True)+prices[i]-fee,
                    memoization(i+1, False)
                )
            memo[(i, canBuy)] = profit
            return memo[(i, canBuy)]

        return memoization(0, True)
