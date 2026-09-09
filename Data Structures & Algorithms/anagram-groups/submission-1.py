class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - 97] += 1
            
            if tuple(count) in d:
                d[tuple(count)].append(word)
            else:
                d[tuple(count)] = [word]

        l = list()
        for v in d.values():
            l.append(v)
        return l   
        
        