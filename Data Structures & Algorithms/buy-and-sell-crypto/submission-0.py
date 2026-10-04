class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest_price = float('inf')
        max_profit = 0

        for p in prices:
            if lowest_price > p:
                lowest_price = p

            current_profit = p - lowest_price
            if current_profit > max_profit:
                max_profit = current_profit
            
        return max_profit

