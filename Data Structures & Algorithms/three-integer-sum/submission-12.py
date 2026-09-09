class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums)):
            base = nums[i]

            if i > 0 and base == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            target = -base

            while l < r:
                sum = nums[l] + nums[r]

                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    res.append([base, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res