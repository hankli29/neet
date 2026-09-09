class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}
        l = 0
        r = 0
        longest = 0
        most_freq = 0

        while r < len(s):
            char = s[r]
            frequencies[char] = frequencies.setdefault(char, 0) + 1

            if frequencies[char] > most_freq:
                most_freq = frequencies[char]

            window = r - l + 1
            num_rep = window - most_freq

            if num_rep <= k and window > longest:
                longest = window
            else: # requires more replacements than allowed
                while r - l + 1 - most_freq > k:
                    char = s[l]
                    frequencies[char] -= 1
                    l += 1
        
            r += 1
    
        return longest