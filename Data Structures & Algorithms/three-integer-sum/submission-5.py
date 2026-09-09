class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # [-4, -1, -1, 0, 1, 2]
        # [-1, 0, 1, 0, -1] -> [-1, -1, 0, 0, 1]

        nums.sort()
        triplets = []
        bases = set()

        for b in range(len(nums) - 2):
            base = nums[b]
            if base not in bases:

                l = b + 1
                r = len(nums) - 1

                while l < r:
                    cur_sum = base + nums[l] + nums[r]

                    if cur_sum > 0:
                        r -= 1
                    elif cur_sum < 0:
                        l += 1
                    else:
                        bases.add(base)
                        triplets.append([base, nums[l], nums[r]])
                        while l < r and (nums[l] == nums[l + 1]):
                            l += 1
                        l += 1

        return triplets