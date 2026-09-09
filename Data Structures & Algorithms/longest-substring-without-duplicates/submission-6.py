class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0

        seen = set()

        while r < len(s):
            char = s[r]

            if char not in seen:
                seen.add(char)
                cur = r - l + 1
                if cur > longest:
                    longest = cur
            else: #repeat char
                while char in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(char)
            
            r += 1
        
        return longest