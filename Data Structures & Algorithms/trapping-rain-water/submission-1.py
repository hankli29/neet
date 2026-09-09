class Solution:
    def trap(self, height: List[int]) -> int:

        # area = min(height[l], height[r]) - height[i]

        total = 0

        max_l = [] 
        cur_max_l = 0

        max_r = []
        cur_max_r = 0

        for i in range(len(height)):
            max_l.append(cur_max_l)

            if height[i] > cur_max_l:
                cur_max_l = height[i]
        
        for i in range(len(height) - 1, -1, -1):
            max_r.append(cur_max_r)

            if height[i] > cur_max_r:
                cur_max_r = height[i]
        
        for i in range(len(height)):
            l = max_l[i]
            r = max_r[len(height) - 1 - i]

            area = min(l, r) - height[i]

            if area < 0:
                continue
            
            total += area



        return total