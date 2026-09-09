class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        l_prods = [1] * len(nums)
        r_prods = [1] * len(nums)

        l_prev = 1
        r_prev = 1
        for i in range(1, len(nums)):
            r_idx = len(nums) - 1 - i

            l_prods[i] = l_prev * nums[i - 1]
            l_prev = l_prods[i]

            r_prods[r_idx] = r_prev * nums[r_idx + 1]
            r_prev = r_prods[r_idx]

        for i in range(len(nums)):
            output[i] = l_prods[i] * r_prods[i]
        
        return output