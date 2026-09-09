class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts_list = [[] for i in range(len(nums))]
        counts = {}
        res = []

        for num in nums:
            counts[num] = counts.setdefault(num, 0) + 1
        
        for num in counts:
            counts_list[counts[num] - 1].append(num)
        
        for i in range(len(counts_list) - 1, -1, -1):
            if len(res) == k:
                return res
            
            for num in counts_list[i]:
                res.append(num)
        
        return res