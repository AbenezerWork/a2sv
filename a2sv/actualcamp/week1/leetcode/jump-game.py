class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        target = 0
        for i in range(len(nums)):
            if target>=i:
                if nums[i]+i >= target:
                    target = nums[i]+i
        
        return target>=len(nums)-1
            