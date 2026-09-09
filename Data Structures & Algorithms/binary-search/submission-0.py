class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            idx = int((r + l) / 2)
            mid = nums[idx]

            if target > mid:
                l = idx + 1
            elif target < mid:
                r = idx - 1
            else:
                return idx
        
        return -1