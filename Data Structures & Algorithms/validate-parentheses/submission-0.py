class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {"}": "{", ")": "(", "]": "["}
        openings = {"{", "(", "["}
        seen_openings = []

        for char in s:

            if char in openings:
                seen_openings.append(char)
                continue
            
            # else, char is a closing

            if len(seen_openings) == 0:
                return False
            
            cur = seen_openings.pop()
            if close_to_open[char] != cur:
                return False
        
        if len(seen_openings) > 0:
            return False
        
        return True