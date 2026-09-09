class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        output = [0] * len(nums)
        l = 1
        r = 1

        for i in range(len(nums)):
            j = len(nums) - i - 1
            left[i] *= l
            l *= nums[i]
            right[j] *= r
            r *= nums[j]

        for i in range(len(left)):
            output[i] = left[i] * right[i]
        
        return output
        