class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights[i] == height of ith bar

        l = 0
        r = len(heights) - 1

        max_area = 0
            
        while l < r:
            new_area = (r - l) * min(heights[l], heights[r])
            if new_area > max_area:
                max_area = new_area
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area


            