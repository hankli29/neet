import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max rate is when rate = size of largest pile
        # then each pile will take 1 hour to finish

        # min possible rate is 1 when given enough hours

        # given rate k, num hours to finish pile = math.ceil(size / k)
            # sum of math.ceil(size / k) for all piles must be <= h

        max_possible_rate = max(piles)

        
        l = 1
        r = max_possible_rate
        min_rate = max_possible_rate

        while l <= r:
            rate = int((l + r) / 2)
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / rate)
            
            # no need for and rate < min_rate check
            # bc after finding a rate, we narrow down search scope
            # to only consider smaller rates
            if total_hours <= h:
                min_rate = rate
                r = rate - 1
            else:
                l = rate + 1

        
        return min_rate

