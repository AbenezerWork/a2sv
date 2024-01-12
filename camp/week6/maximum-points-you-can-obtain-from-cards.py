class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        curr= j=0
        mx = float("inf")
        for i in range(len(nums)):
            curr+=nums[i]
            while i-j+1>len(nums)-k:
                curr-=nums[j]
                j+=1
            if i-j+1==len(nums)-k:
                mx = min(curr,mx)
        return sum(nums)-mx