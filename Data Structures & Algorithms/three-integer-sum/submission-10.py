class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # no duplicate triplets

        res = []
        
        nums.sort()

        seen_bases = set()

        for b in range(len(nums)):
            if b > 0 and nums[b] == nums[b - 1]:
                continue

            target = -nums[b]

            l = b + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r]

                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    res.append([nums[b], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and (nums[l] == nums[l - 1]):
                        l += 1
                    while l < r and (nums[r] == nums[r + 1]):
                        r -= 1
        
        return res




