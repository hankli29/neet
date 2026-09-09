class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = []
        for char in s:
            if char.isalnum():
                if char.isdigit():
                    chars.append(char)
                else:
                    chars.append(char.lower())
        
        l = 0
        r = len(chars) - 1

        while l < r:
            if chars[l] != chars[r]:
                return False
            
            l += 1
            r -= 1
        
        return True