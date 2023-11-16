class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]

        for day in range(len(prices)):
            lowest_price = min(prices[day],lowest_price)
            price_diffrance = prices[day] - lowest_price

            max_profit = max(price_diffrance,max_profit)

        return max_profit
        