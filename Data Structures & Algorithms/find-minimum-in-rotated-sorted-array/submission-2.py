class Solution:
    def findMin(self, nums: List[int]) -> int:

        min_num = nums[0]
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if nums[l] < nums[r]:
                return min(min_num, nums[l])

            mid = int((l + r) / 2)
            cur = nums[mid]

            if cur < min_num:
                min_num = cur

            if cur >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return min_num