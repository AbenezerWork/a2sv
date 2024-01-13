class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j =curr= 0
        ans = float("inf")
        for i in range(len(nums)):
            curr+=nums[i]
            while curr-nums[j]>=target:
                curr-=nums[j]
                j+=1
            if curr>=target:
                ans = min(ans,i-j+1)
        if ans > 10**9+1:
            return 0
        return ans