class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        search = {}
        for i in nums:
            search[i] = 0
        answer = 0
        print(search)
        for i in nums:
            if i-1 not in search:
                print(i)
                count = 1
                while i + count in search:
                    print(i+count)
                    count += 1
                answer = max(answer, count)
                print(answer)
        return answer