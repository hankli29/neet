class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_seen = {}
        t_seen = {}

        for char in s:
            s_seen[char] = s_seen.setdefault(char, 0) + 1
        
        for char in t:
            t_seen[char] = t_seen.setdefault(char, 0) + 1
        
        return s_seen == t_seen
            