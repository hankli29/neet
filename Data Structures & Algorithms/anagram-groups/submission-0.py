class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            freq = [0] * 26
            for j in i:
                freq[ord(j) - 97] += 1
            freq = tuple(freq)
            if freq in anagrams:
                anagrams[freq].append(i)
            else:
                anagrams[freq] = [i]
        return list(anagrams.values())