class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        longest = 1
        nums = set(nums)

        starts = []
        for n in nums:
            if (n - 1) not in nums:
                starts.append(n)
        
        for s in starts:
            cur = 1
            while (s + 1) in nums:
                cur += 1

                if cur > longest:
                    longest = cur
                
                s += 1
        
        return longest