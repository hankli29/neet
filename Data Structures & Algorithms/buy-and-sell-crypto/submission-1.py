class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0] # want the lowest price
        cur_max = 0

        for i in range(1, len(prices)):
            new_price = prices[i]

            if new_price < buy:
                buy = new_price
            
            cur_max = max(cur_max, new_price - buy)
        
        return cur_max

