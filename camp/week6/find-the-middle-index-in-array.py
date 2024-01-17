class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        j = len(nums)-1
        ls = rs = 0
        pre = [0]
        suff = [0]
        for i in range(len(nums)):
            pre.append( pre[i]+nums[i])
            suff.append( suff[i]+nums[j-i])
        for i in range(len(nums)):
            if pre[i] == suff[j-i]:
                return i
        return -1