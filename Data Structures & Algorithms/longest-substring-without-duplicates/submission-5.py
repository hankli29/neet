class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        seen = {}

        while r < len(s):
            char = s[r]

            if char not in seen or seen[char] < l:
                seen[char] = r
            else:
            # otherwise, char is a repeat
                l = seen[char] + 1
                seen[char] = r

            cur = r - l + 1
            r += 1
            if cur > longest:
                longest = cur
            
        
        return longest
            
            