class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l

            cur_area = height * width
            if cur_area > max_area:
                max_area = cur_area
            
            # when moving l/r, it is only possible for new area to be larger
            # than max area if new height is > min(l height, r height)
                # preserve the larger height
            
            if heights[l] < heights[r]:
                # move left pointer
                l += 1
            else:
                # move right pointer
                r -= 1

        return max_area
