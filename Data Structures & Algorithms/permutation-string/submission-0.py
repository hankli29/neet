class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        freq = {}
        win = {}
        count = 0

        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        
        l = r = 0
        while r < len(s2):
            win[s2[r]] = win.get(s2[r], 0) + 1
            count += 1

            if count == len(s1):
                print(win)
                if freq == win:
                    return True
                
                win[s2[l]] -= 1
                if win[s2[l]] == 0:
                    win.pop(s2[l])
                
                l += 1
                count -= 1

            r += 1
        
        return False
        
