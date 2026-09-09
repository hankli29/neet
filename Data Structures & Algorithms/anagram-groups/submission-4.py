class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # dictionary for each word in strs
        # each dict keeps track of char: count
        
        # keep another dict, value is the dict from above (of char: count)
        # and key is list containing words corresponding to dict

        # cannot have dict as key, key must be immutable

        ags = {}

        for word in strs:
            char_counts = [0] * 26

            for c in word:
                char_counts[ord(c) - 97] += 1
            
            char_counts = tuple(char_counts)
            if char_counts not in ags:
                ags[char_counts] = [word]
            else:
                ags[char_counts].append(word)
        
        return list(ags.values())