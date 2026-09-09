class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods = [1] * len(nums)
        right_prods = [1] * len(nums)
        res = [0] * len(nums)

        for i in range(1, len(nums)):
            left_prods[i] = nums[i - 1] * left_prods[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            right_prods[i] = nums[i + 1] * right_prods[i + 1]
        for i in range(len(nums)):
            res[i] = left_prods[i] * right_prods[i]
        
        return res