class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0

        for right, price in enumerate(prices):
            profit = prices[right] - prices[left]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                left = right
        return maxProfit
