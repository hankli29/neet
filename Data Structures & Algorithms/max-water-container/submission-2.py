class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max = 0

        while l < r:
            cur = min(heights[l], heights[r]) * (r - l)

            if cur > max:
                max = cur

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max

            