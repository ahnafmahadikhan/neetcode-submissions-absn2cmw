class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        value = prices[0]
        max_profit = 0
        for price in prices:
            if price < value:
                value = price
            elif price - value > max_profit:
                max_profit = price - value
        return max_profit
            