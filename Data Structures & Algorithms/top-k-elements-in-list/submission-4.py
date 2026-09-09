class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        all_freqs = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        for num, freq in freqs.items():
            all_freqs[freq].append(num)
        
        print(all_freqs)
        count = 0
        for i in range(len(nums), -1, -1):
            for element in all_freqs[i]:
                res.append(element)
                count += 1

                if count == k:
                    return res