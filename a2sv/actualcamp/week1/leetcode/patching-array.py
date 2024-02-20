class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        i = ans = 0
        while miss<=n:
            if i<len(nums) and nums[i]<=miss:
                miss+=nums[i]
                i+=1
            else:
                miss*=2
                ans+=1
        return ans