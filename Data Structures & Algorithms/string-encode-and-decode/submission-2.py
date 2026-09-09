class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += str(len(i)) + ":" + i
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != ':':
                length += s[i]
                i += 1
            length: int = int(length) + 1
            result.append(s[i+1: i + length])
            i += length
        return result

