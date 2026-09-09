class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complements = dict()

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in complements:
                return [complements[diff], i]
            
            complements[nums[i]] = i
