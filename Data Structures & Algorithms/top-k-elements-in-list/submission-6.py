class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        res = []

        for num in nums:
            counts[num] = counts.setdefault(num, 0) + 1
        

        buckets = [[] for i in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)
        
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
            
            if len(res) == k:
                return res