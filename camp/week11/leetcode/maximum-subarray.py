class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, ans = -float('inf'),-float("inf")
        for i in range(len(nums)):
            curr=curr+nums[i] if curr>0 else nums[i]
            ans = max(curr, ans)
        return ans