class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        numbers = set(nums)
        longest = 1

        for num in numbers:
            cur = 1
            if num - 1 in numbers:
                continue
                # only start counting length of sequence from lowest num
            
            while num + 1 in numbers:
                cur += 1
                num += 1
            
            if cur > longest:
                longest = cur
        
        return longest