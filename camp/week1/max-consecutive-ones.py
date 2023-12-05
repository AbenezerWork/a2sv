class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i]==1:
                curr+=1
            else:
                mx = max(mx,curr)
                curr = 0
        mx = max(mx,curr)
        return mx