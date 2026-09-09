class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for word in strs:
            counts = [0] * 26

            for char in word:
                counts[ord(char) - ord('a')] += 1
            
            counts = tuple(counts)
            
            res.setdefault(counts, []).append(word)

        
        return list(res.values())

        
        
