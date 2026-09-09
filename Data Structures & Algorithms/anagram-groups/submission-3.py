class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            char_count = [0] * 26

            for c in word:
                char_count[ord(c) - 97] += 1
            
            char_count = tuple(char_count)
            if char_count in anagrams:
                anagrams[char_count].append(word)
            else:
                anagrams[char_count] = [word]
        
        return list(anagrams.values())