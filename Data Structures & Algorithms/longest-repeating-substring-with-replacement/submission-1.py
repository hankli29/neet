class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        freq = {}
        max_length = 0

        #AAABABBAA
        #BASABB

        while r < len(s):
            freq[s[r]] = freq.setdefault(s[r], 0) + 1

            highest_freq = max(freq.values())
            # total window size - highest frequency
            num_replacements = (r - l + 1) - highest_freq
            while num_replacements > k:
                freq[s[l]] -= 1
                l += 1

                num_replacements = (r - l + 1) - highest_freq

            
            if (r - l + 1) > max_length:
                max_length = (r - l + 1)

            r += 1
        
        return max_length 
