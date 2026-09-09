class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []

        for i in range(len(sorted_nums)):
            base = sorted_nums[i]
            if i > 0 and base == sorted_nums[i - 1]:
                continue

            complement = 0 - base

            l = i + 1
            r = len(sorted_nums) - 1

            while l < r:
                left = sorted_nums[l]
                right = sorted_nums[r]

                sum = left + right

                if sum > complement:
                    r -= 1
                elif sum < complement:
                    l += 1
                else:
                    res.append([base, left, right])
                    l += 1
                    r -= 1

                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1
        return res