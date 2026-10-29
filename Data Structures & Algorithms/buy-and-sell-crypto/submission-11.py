class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_product_price = prices[0]

        for i in range(len(prices)):

            if (prices[i] - min_product_price) > max_profit:
                max_profit = max(max_profit, (prices[i] - min_product_price))

            if min_product_price > prices[i]:
                min_product_price = prices[i]

        return max_profit
