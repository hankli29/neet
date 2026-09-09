class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        potential_starts = set()
        max_count = 0

        for num in nums:
            if (num - 1) not in nums:
                potential_starts.add(num)
        
        for num in potential_starts:
            cur = 1
            while (num + 1) in nums:
                cur += 1
                num += 1
            if cur > max_count:
                max_count = cur
        
        return max_count