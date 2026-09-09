class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l = r = 0
        max_length = 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            
            if len(seen) > max_length:
                max_length = len(seen)
            
            r += 1

        return max_length