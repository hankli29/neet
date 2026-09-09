class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        search = {}
        for i in range(len(numbers)):
            search[numbers[i]] = i
        answer = []
        for i in range(len(numbers)):
            if target - numbers[i] in search and search[target - numbers[i]] != i:
                return [i+1, search[target-numbers[i]]+1] 
        