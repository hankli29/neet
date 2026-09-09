class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods = [1] * (len(nums) + 1)
        right_prods = [1] * (len(nums) + 1)
        res = [0] * len(nums)

        for i in range(len(nums)):
            left_prods[i + 1] = left_prods[i] * nums[i]
        for i in range(len(nums) - 1, -1, -1):
            right_prods[i - 1] = right_prods[i] * nums[i]
        
        for i in range(len(nums)):
            res[i] = left_prods[i] * right_prods[i]
        
        return res