class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        r = len(s1) - 1

        substring_freq = {}
        for c in s1:
            substring_freq[c] = substring_freq.setdefault(c, 0) + 1
        

        window_freq = {}
        for i in range(r + 1):
            window_freq[s2[i]] = window_freq.setdefault(s2[i], 0) + 1

        while r < len(s2) - 1:

            if window_freq == substring_freq:
                return True
            
            r += 1
            window_freq[s2[r]] = window_freq.setdefault(s2[r], 0) + 1
            window_freq[s2[l]] -= 1

            if window_freq[s2[l]] == 0:
                window_freq.pop(s2[l])

            l += 1
        
        if window_freq == substring_freq:
            return True

        return False