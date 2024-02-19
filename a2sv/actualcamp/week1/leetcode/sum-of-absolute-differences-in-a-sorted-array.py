class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        tsum = sum(nums)
        cumm = 0
        ans  =[]
        for i in range(len(nums)):

            before = cumm
            after = tsum-cumm-nums[i]
            ans.append( nums[i]*i-before + abs(nums[i]*(len(nums)-(i+1))-after))
            cumm+=nums[i]
        return ans