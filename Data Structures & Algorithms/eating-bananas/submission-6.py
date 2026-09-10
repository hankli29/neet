import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        min_rate = r
        
        while l <= r:
            rate = int((l + r) / 2)

            total_hrs = 0
            for pile in piles:
                hrs_needed = math.ceil(pile / rate)
                total_hrs += hrs_needed

            if total_hrs <= h:
                if rate < min_rate:
                    min_rate = rate
                r = rate - 1
            else:
                l = rate + 1
        
        return min_rate