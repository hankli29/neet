class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        bucket = [[]] * 10000
        for i in freq:
            if len(bucket[freq[i]]) == 0:
                bucket[freq[i]] = [i]
            else:
                bucket[freq[i]].append(i)
        answer = []
        j = len(bucket) - 1
        while j >= 0 and len(answer) < k:
            if len(bucket[j]) > 0:
                answer += bucket[j]
            j -= 1
        return answer
