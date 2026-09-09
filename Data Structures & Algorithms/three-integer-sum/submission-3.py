class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums):
            l = i+1
            r = len(nums)-1
            while l < r:
                if -(nums[l] + nums[r]) == nums[i]:
                    answer.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif -(nums[l] + nums[r]) < nums[i]:
                    r -= 1
                else:
                    l += 1
            i += 1
        return list(answer)
        