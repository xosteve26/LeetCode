class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            if(prices[left] < prices[right]):
                maxProfit = max(prices[right]-prices[left], maxProfit)
            else:
                left = right
            right += 1
        return maxProfit
