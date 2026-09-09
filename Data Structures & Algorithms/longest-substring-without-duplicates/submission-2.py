class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l, r = 0, 0

        longest = 1

        seen = dict()

        while r < len(s):
            if s[r] not in seen or seen[s[r]] < l:
                seen[s[r]] = r
            else:
                l = seen[s[r]] + 1
                seen[s[r]] = r
            
            if (r - l) + 1 > longest:
                    longest = r - l + 1
            r += 1

        return longest