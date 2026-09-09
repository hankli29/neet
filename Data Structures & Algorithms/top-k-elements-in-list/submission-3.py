class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        count = [[] for i in range(len(nums) + 1)]
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        # key is number itself, v is count
        for key, v in d.items():
            count[v].append(key)

        r = []
        for j in range(len(count) - 1, -1, -1):
            for freq in count[j]:
                r.append(freq)
                if (len(r) == k):
                    return r
