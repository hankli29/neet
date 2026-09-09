class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums: # potential start of a sequence
                count = 1
                while num + 1 in nums:
                    count += 1
                    num += 1
            
                if count > longest:
                    longest = count
        
        return longest
            