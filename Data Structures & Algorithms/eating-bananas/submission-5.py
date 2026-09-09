import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h >= num piles
        # time needed for pile with x nanas = math.ceil(x / k)

        # time for all piles = sum(math.ceil(x / k)) <= h
        # want min k eating rate to finish all bananas within h hours

        # upper bound for k = size of largest pile (max(piles))
        # lower bound for k = 1

        l = 1
        r = max(piles)
        min_rate = r

        while l <= r:

            cur_rate = int((l + r) / 2)
            total_hours = 0
            
            for pile in piles:
                time_needed = math.ceil(pile / cur_rate)
                total_hours += time_needed
            
            if total_hours > h:
                l = cur_rate + 1
            else:
                if cur_rate < min_rate:
                    min_rate = cur_rate
                
                r = cur_rate - 1
        

        return min_rate




