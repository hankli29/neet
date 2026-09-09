class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        2*4*6
        4*6
        6

        1
        1*2
        1*2*4

        2*4*6
        4*6*1
        6*1*2
        1*2*4
        '''
        pre = [1]
        for i in range(len(nums)-1):
            pre.append(pre[-1] * nums[i])
        suf = [1]
        for i in range(len(nums)-1, 0, -1):
            suf.append(suf[-1] * nums[i])
        suf = suf[::-1]
        result = []
        for i in range(len(pre)):
            result.append(pre[i] * suf[i])
        return result

        