class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer approach
        # left represents buy, right represents sell
        l, r = 0, 1

        max = 0
        while r < len(prices):
            cur = prices[r] - prices[l]
            if cur > max:
                max = cur
            
            if prices[r] < prices[l]:
                l = r
            
            r += 1

        return max