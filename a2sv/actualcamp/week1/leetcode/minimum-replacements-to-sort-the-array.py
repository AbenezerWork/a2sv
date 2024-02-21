class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        mn = nums[-1]

        for i in range(len(nums)-1,-1,-1):
            if mn<nums[i]:
                ans += ceil(nums[i]/mn)-1
                mn = nums[i]//ceil(nums[i]/mn)
            else:
                mn  = min(mn,nums[i])
        return ans